from rest_framework.serializers import ModelSerializer

from . import models


class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = ('__all__')


class UnitSerializer(ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('__all__')


class ShelfSerializer(ModelSerializer):
    class Meta:
        model = models.Shelf
        fields = ('__all__')


class BoxSerializer(ModelSerializer):
    class Meta:
        model = models.Box
        fields = ('__all__')
