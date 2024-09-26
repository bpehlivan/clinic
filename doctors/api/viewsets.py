import copy
from datetime import datetime, timedelta

from django.utils.dateparse import parse_date
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import mixins

from api.viewsets import BaseGenericViewSet
from appointments.models import Appointment
from doctors.api.serializers import (
    DoctorListSerializer,
    DoctorDetailSerializer,
    DoctorCreateSerializer,
    AvailableAppointmentSlotsForDoctorSerializer,
)
from doctors.models import Doctor


class DoctorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    BaseGenericViewSet,
):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    serializer_classes = {
        "list": DoctorListSerializer,
        "retrieve": DoctorDetailSerializer,
        "create": DoctorCreateSerializer,
        "available_appointment_slots": AvailableAppointmentSlotsForDoctorSerializer,
    }

    @action(methods=["GET"], detail=True, url_name="available_appointment_slots")
    def available_appointment_slots(self, request, pk=None):
        # Get start_date and end_date from query parameters
        start_date_str = request.query_params.get("start_date", None)
        end_date_str = request.query_params.get("end_date", None)

        # Parse the dates
        start_date = (
            parse_date(start_date_str) if start_date_str else datetime.now().date()
        )
        end_date = (
            parse_date(end_date_str) if end_date_str else start_date + timedelta(days=7)
        )

        doctor = self.queryset.filter(pk=pk).first()
        if not doctor:
            raise APIException("Doctor with the given pk does not exist.")

        empty_timeslots: set = doctor.get_daily_empty_appointment_timeslots()

        daily_timeslots = []

        index_date = start_date
        while index_date < end_date:
            all_slots = copy.deepcopy(empty_timeslots)
            filled_timeslots = Appointment.objects.get_filled_timeslots(
                doctor=doctor, date=index_date
            )
            available_timeslots = list(all_slots - filled_timeslots)
            available_timeslots.sort()
            daily_timeslots.append(
                {
                    "date": index_date,
                    "available_timeslots": available_timeslots,
                }
            )
            index_date += timedelta(days=1)

        serializer = self.get_serializer(data=daily_timeslots, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
