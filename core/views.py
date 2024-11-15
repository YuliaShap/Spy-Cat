from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SpyCat, Target, Mission
from .serializers import SpyCatSerializer, TargetSerializer, MissionSerializer
from rest_framework.exceptions import ValidationError


class SpyCatViewSet(ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_destroy(self, instance):
        if instance.spy_cat is not None:
            raise ValidationError("Cannot delete mission as it is assigned to a cat.")
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TargetViewSet(ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
