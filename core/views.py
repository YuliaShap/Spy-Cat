from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SpyCat, Target, Mission
from .serializers import SpyCatSerializer, TargetSerializer, MissionSerializer


class SpyCatViewSet(ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class TargetViewSet(ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
