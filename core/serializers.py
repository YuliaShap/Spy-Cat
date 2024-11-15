from rest_framework import serializers
from .models import SpyCat, Target, Mission
import requests
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = '__all__'

    def update(self, instance, validated_data):
        targets_data = self.context['request'].data.get('targets', [])
        is_complete = validated_data.get('is_complete', instance.is_complete)

        if not targets_data:
            raise ValidationError("No targets provided for update.")

        for target_data in targets_data:
            target_id = target_data.get('id')
            if not target_id:
                raise ValidationError("Target ID is required for updates.")

            try:
                target = instance.targets.get(id=target_id)
            except Target.DoesNotExist:
                raise ValidationError(f"Target with id {target_id} does not exist in this mission.")

            target.notes = target_data.get('notes', target.notes)
            target.save()

        instance.is_complete = is_complete
        instance.save()

        return instance


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
