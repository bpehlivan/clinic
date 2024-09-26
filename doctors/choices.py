from django.db import models


class AppointmentSlotChoices(models.TextChoices):
    fifteen_minutes = "fifteen_minutes", "fifteen minutes"
    thirty_minutes = "thirty_minutes", "thirty minutes"
    hourly = "hourly", "hourly"


class SpecializationChoices(models.TextChoices):
    internal_medicine = "internal_medicine", "Internal Medicine"
    family_medicine = "family_medicine", "Family Medicine"
    pediatrics = "pediatrics", "Pediatrics"
    cardiology = "cardiology", "Cardiology"
    dermatology = "dermatology", "Dermatology"
    neurology = "neurology", "Neurology"
    psychiatry = "psychiatry", "Psychiatry"
    surgery = "surgery", "Surgery"
