from rest_framework import serializers
from habits.serializers import HabitSerializer
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""
    habits = HabitSerializer(source="users_habits", many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"