from django.db import models
from rest_framework.exceptions import APIException


class AppointmentManager(models.Manager):
    def get_filled_timeslots(self, doctor, date) -> set:
        appointments = self.filter(doctor=doctor, duration__startswith__date=date)
        timeslots = set()

        slot_duration = doctor.get_timeslot_duration()

        for appointment in appointments:
            start_time = appointment.duration.lower
            end_time = appointment.duration.upper
            while start_time < end_time:
                timeslots.add(start_time.time().strftime("%H.%M"))
                start_time += slot_duration

        return timeslots

    def is_appointment_available(self, doctor, start_at, end_at) -> bool:
        existing_appointments = self.filter(
            doctor=doctor, duration__overlap=(start_at, end_at)
        )
        if existing_appointments.exists():
            return False
        return True

    def create_appointment(
        self, doctor, start_at, patient_full_name, patient_identity_number=None
    ):
        slot_duration = doctor.get_timeslot_duration()
        slot_as_minutes = slot_duration.total_seconds() // 60

        if start_at.minute % slot_as_minutes != 0:
            raise APIException(
                "Appointment start does not match with timeslot options."
            )

        end_at = start_at + slot_duration

        is_appointment_available = self.is_appointment_available(
            doctor=doctor,
            start_at=start_at,
            end_at=end_at,
        )

        if not is_appointment_available:
            raise APIException(
                "Appointment slot is not available for given doctor and the date."
            )

        self.create(
            doctor=doctor,
            duration=(start_at, end_at),
            patient_full_name=patient_full_name,
            patient_identity_number=patient_identity_number,
        )
