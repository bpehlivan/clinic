from rest_framework.routers import DefaultRouter


urlpatterns = []


router = DefaultRouter(trailing_slash=True)


urlpatterns += router.urls
