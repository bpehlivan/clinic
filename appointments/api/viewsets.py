from rest_framework import mixins

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
        Appointment.objects.create_appointment(
            doctor=serializer.validated_data.get("doctor"),
            start_at=serializer.validated_data.get("start_at"),
            patient_full_name=serializer.validated_data.get("patient_full_name"),
            patient_identity_number=serializer.validated_data.get(
                "patient_identity_number"
            ),
        )
