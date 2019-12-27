from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, serializers


class BaseFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        old = request.GET._mutable
        request.GET._mutable = True
        if 'deleted' not in request.query_params:
            request.query_params['deleted'] = 0
        request.GET._mutable = old
        return super().filter_queryset(request, queryset, view)


class BaseViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    filter_backends = (BaseFilter,)
    filterset_fields = ('deleted',)


class BaseModelSerialize(serializers.ModelSerializer):
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
