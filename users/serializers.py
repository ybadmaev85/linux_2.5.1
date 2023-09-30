from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели юзеров
    '''

    class Meta:
        model = User
        fields = (
            'user',
            'avatar',
            'phone_num',
            'country',
        )