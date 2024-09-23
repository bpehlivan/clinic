from rest_framework import viewsets


class SerializersByActionMixin:
    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action,
            self.serializer_class,
        )


class BaseGenericViewSet(SerializersByActionMixin, viewsets.GenericViewSet):
    pass


class BaseModelViewSet(SerializersByActionMixin, viewsets.ModelViewSet):
    pass
