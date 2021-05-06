from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'menu_item', views.MenuItemViewSet)

urlpatterns = router.urls
