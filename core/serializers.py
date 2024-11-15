from rest_framework import serializers
from .models import SpyCat, Target, Mission
import requests
from rest_framework.exceptions import ValidationError


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    targets = serializers.PrimaryKeyRelatedField(queryset=Target.objects.all(), many=True)

    class Meta:
        model = Mission
        fields = '__all__'


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'

    def validate_breed(self, value):
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code == 200:
            breeds = [breed['name'] for breed in response.json()]
            if value not in breeds:
                raise ValidationError(f"{value} is not a valid breed.")
        return value
