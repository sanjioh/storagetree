from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'warehouses', views.WarehouseViewSet, basename='warehouse')
router.register(r'units', views.UnitViewSet, basename='unit')
router.register(r'shelves', views.ShelfViewSet, basename='shelf')
router.register(r'boxes', views.BoxViewSet, basename='box')
urlpatterns = router.urls
