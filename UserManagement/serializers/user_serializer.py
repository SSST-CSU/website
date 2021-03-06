from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'pwd', 'stat', 'name_used_before', 'sex', 'birthday', 'qq', 'email',
                  'political', 'native_place', 'id_number', 'phone_number', 'country_and_region', 'creator']