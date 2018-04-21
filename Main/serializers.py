from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Main.models import Object


class ObjectSerializer(ModelSerializer):
    name = serializers.ReadOnlyField(source='name')
    path = serializers.ReadOnlyField(source='path')

    class Meta:
        model = Object
        fields = ('name', 'path')
