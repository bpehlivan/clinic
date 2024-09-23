from rest_framework import serializers

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
            "specialization",
            "license_number",
            "biography",
            "is_active",
            "created_at",
            "updated_at",
        )


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "full_name",
            "specialization",
        )
