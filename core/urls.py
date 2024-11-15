from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpyCatViewSet, MissionViewSet, TargetViewSet

router = DefaultRouter()
router.register('spy_cats', SpyCatViewSet)
router.register('missions', MissionViewSet)
router.register('targets', TargetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
