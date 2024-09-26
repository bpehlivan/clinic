from datetime import timedelta

from doctors.choices import AppointmentSlotChoices

timeslot_duration = {
    AppointmentSlotChoices.fifteen_minutes: timedelta(minutes=15),
    AppointmentSlotChoices.thirty_minutes: timedelta(minutes=30),
    AppointmentSlotChoices.hourly: timedelta(hours=1),
}
