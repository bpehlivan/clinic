from datetime import timedelta, datetime
from typing import Optional

from django.db import models
from rest_framework.exceptions import ValidationError

from doctors.choices import (
    AppointmentSlotChoices,
    SpecializationChoices,
)
from main.models import BaseModel
from main.utils import timeslot_duration


class Doctor(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    license_number = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)

    start_hour = models.TimeField()
    end_hour = models.TimeField()

    is_active = models.BooleanField(default=True)

    appointment_slot_choices: AppointmentSlotChoices = models.CharField(
        choices=AppointmentSlotChoices.choices,
        default=AppointmentSlotChoices.fifteen_minutes,
        max_length=32,
    )
    specialization: Optional[SpecializationChoices] = models.CharField(
        choices=SpecializationChoices.choices,
        max_length=64,
        null=True,
        blank=True,
    )

    def get_timeslot_duration(self) -> timedelta:
        return timeslot_duration[self.appointment_slot_choices]

    def get_daily_empty_appointment_timeslots(self):
        timeslots = set()

        slot_duration = self.get_timeslot_duration()
        time_index = self.start_hour
        while time_index < self.end_hour:
            timeslots.add(time_index.strftime("%H.%M"))
            time_index = (
                datetime.combine(
                    date=datetime.today(),
                    time=time_index,
                )
                + slot_duration
            ).time()

        return timeslots

    def clean(self):
        if self.start_hour >= self.end_hour:
            raise ValidationError("Start hour must be earlier than end hour.")
