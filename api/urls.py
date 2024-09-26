from rest_framework.routers import DefaultRouter

from doctors.api.viewsets import DoctorViewSet

urlpatterns = []


router = DefaultRouter(trailing_slash=True)

router.register("doctors", DoctorViewSet, basename="doctors")


urlpatterns += router.urls
