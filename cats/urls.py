from rest_framework.routers import DefaultRouter
from .views import CatViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cats')

urlpatterns = router.urls