from psycopg2.pool import AbstractConnectionPool
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from api.viewsets import BaseGenericViewSet
from appointments.api.serializers import (
    AppointmentCreateSerializer,
    AppointmentSerializer,
    AppointmentDetailSerializer,
)
from appointments.models import Appointment


class AppointmentViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, BaseGenericViewSet
):
    serializer_class = AppointmentSerializer
    serializer_classes = {
        "list": AppointmentSerializer,
        "create": AppointmentCreateSerializer,
        "detail": AppointmentDetailSerializer,
    }
    queryset = Appointment.objects.all()

    def perform_create(self, serializer):
        doctor = serializer.validated_data.get("doctor")
        slot_duration = doctor.get_timeslot_duration()

        start_at = serializer.validated_data.get("start_at")
        end_at = start_at + slot_duration

        is_appointment_available = self.queryset.is_appointment_available(
            doctor=doctor,
            start_at=start_at,
            end_at=end_at,
        )

        if not is_appointment_available:
            raise APIException(
                "Appointment slot is not available for given doctor and the date."
            )

        Appointment.objects.create(
            doctor=doctor,
            duration=(start_at, end_at),
            patient_full_name=serializer.validated_data.get("patient_full_name"),
            patient_identity_number=serializer.validated_data.get(
                "patient_identity_number"
            ),
        )
