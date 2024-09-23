from api.viewsets import BaseModelViewSet
from doctors.api.serializers import DoctorListSerializer, DoctorDetailSerializer
from doctors.models import Doctor


class DoctorViewSet(BaseModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    serializer_classes = {
        "list": DoctorListSerializer,
        "retrieve": DoctorDetailSerializer,
    }
