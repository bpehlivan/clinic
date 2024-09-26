from rest_framework.routers import DefaultRouter

from appointments.api.viewsets import AppointmentViewSet
from doctors.api.viewsets import DoctorViewSet

urlpatterns = []


router = DefaultRouter(trailing_slash=True)

router.register("doctors", DoctorViewSet, basename="doctors")
router.register("appointments", AppointmentViewSet, basename="appointments")


urlpatterns += router.urls
