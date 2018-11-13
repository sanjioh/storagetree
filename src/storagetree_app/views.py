from rest_framework.viewsets import ModelViewSet

from . import filters, models, serializers


class WarehouseViewSet(ModelViewSet):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer


class UnitViewSet(ModelViewSet):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    filterset_class = filters.UnitFilter


class ShelfViewSet(ModelViewSet):
    queryset = models.Shelf.objects.all()
    serializer_class = serializers.ShelfSerializer
    filterset_class = filters.ShelfFilter


class BoxViewSet(ModelViewSet):
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer
    # filterset_class
