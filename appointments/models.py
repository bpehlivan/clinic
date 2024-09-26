from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models

from appointments.managers import AppointmentManager
from main.models import BaseModel


class Appointment(BaseModel):
    doctor = models.ForeignKey(
        to="doctors.Doctor",
        related_name="appointments",
        related_query_name="appointments",
        limit_choices_to={"is_active": True},
        on_delete=models.DO_NOTHING,
    )

    duration = DateTimeRangeField()

    patient_full_name = models.CharField(max_length=255)
    patient_identity_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    objects = AppointmentManager()
