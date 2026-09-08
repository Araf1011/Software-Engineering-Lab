from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    roll = serializers.IntegerField()
    section = serializers.CharField(max_length= 20)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)