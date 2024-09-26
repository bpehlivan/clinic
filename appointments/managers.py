from django.db import models


class AppointmentManager(models.Manager):
    def get_filled_timeslots(self, doctor, date) -> set:
        appointments = self.filter(doctor=doctor, duration__contains=date)
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
