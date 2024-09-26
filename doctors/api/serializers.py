from rest_framework import serializers
from rest_framework.exceptions import APIException

from doctors.models import Doctor


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "full_name",
            "email",
            "phone_number",
            "address",
            "license_number",
            "biography",
            "is_active",
            "created_at",
            "updated_at",
            "specialization",
        )


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "full_name",
            "specialization",
            "start_hour",
            "end_hour",
        )


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "full_name",
            "email",
            "phone_number",
            "address",
            "license_number",
            "biography",
            "is_active",
            "start_hour",
            "end_hour",
            "appointment_slot_choices",
            "specialization",
        )

    def validate_start_hour(self, start_hour):
        if start_hour.minute != 0:
            raise APIException("Only hours can be selected like '08:00'")

        return start_hour

    def validate_end_hour(self, end_hour):
        if end_hour.minute != 0:
            raise APIException("Only hours can be selected like '17:00'")

        return end_hour

    def to_internal_value(self, data):
        start_hour = data.get("start_hour")
        end_hour = data.get("end_hour")

        if start_hour >= end_hour:
            raise APIException("Start hour must be earlier than end hour.")


        return super().to_internal_value(data=data)


class AvailableAppointmentSlotsForDoctorSerializer(serializers.Serializer):
    date = serializers.DateField()
    available_timeslots = serializers.ListField(child=serializers.CharField())
