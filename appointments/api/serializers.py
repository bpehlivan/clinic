from calendar import month
from sys import modules

from rest_framework import serializers

from appointments.models import Appointment
from doctors.api.serializers import DoctorDetailSerializer


class AppointmentCreateSerializer(serializers.ModelSerializer):
    start_at = serializers.DateTimeField()

    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "patient_full_name",
            "patient_identity_number",
        )


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "duration",
            "patient_full_name",
            "patient_identity_number",
        )


class AppointmentDetailSerializer(serializers.ModelSerializer):
    doctor = DoctorDetailSerializer()

    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "duration",
            "patient_full_name",
            "patient_identity_number",
        )
