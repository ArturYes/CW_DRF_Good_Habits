from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатор пользователя"""

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'telegram_chat_id', 'avatar',]


class UserRetrieveSerializer(serializers.ModelSerializer):
    """Класс сериализатор отображения профиля пользователя"""

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_active', 'telegram_chat_id', 'avatar', ]
