from django_filters import rest_framework as filters

from . import models


class UnitFilter(filters.FilterSet):
    class Meta:
        model = models.Unit
        fields = ['organization']

    @property
    def qs(self):
        qs = super().qs
        user = self.request.user
        ids = user.memberships.all().values_list('organization', flat=True)
        return qs.filter(organization__in=ids)


class ShelfFilter(filters.FilterSet):
    class Meta:
        model = models.Shelf
        fields = ['unit']

    @property
    def qs(self):
        qs = super().qs
        user = self.request.user
        ids = user.memberships.all().values_list('organization', flat=True)
        return qs.filter(unit__organization__in=ids)
