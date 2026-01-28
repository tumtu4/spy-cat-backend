from rest_framework.routers import DefaultRouter
from .views import MissionViewSet, TargetViewSet

router = DefaultRouter()
router.register(r'missions', MissionViewSet, basename='missions')
router.register(r'targets', TargetViewSet, basename='targets')

urlpatterns = router.urls
