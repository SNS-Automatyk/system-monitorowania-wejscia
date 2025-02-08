from rest_framework import serializers
from .models import Door

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = ['id', 'state']
        read_only_fields = ['id']

    def create(self, validated_data):
        raise serializers.ValidationError("Creation of Door instances is not allowed.")

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance
    
    def delete(self, instance):
        raise serializers.ValidationError("Deletion of Door instances is not allowed.")
