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
            "start_at",
        )


class AppointmentSerializer(serializers.ModelSerializer):
    appointment_start = serializers.DateTimeField(source="duration.lower", read_only=True)
    appointment_end = serializers.DateTimeField(source="duration.upper", read_only=True)

    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "appointment_start",
            "appointment_end",
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
