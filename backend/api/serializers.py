"""Настройки сериализатора."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Настройки класса."""

    class Meta:
        """Настройки класса."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
