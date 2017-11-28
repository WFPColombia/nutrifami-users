# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from usuarios.models import User, Familiar, Avance, CapacitacionInscrita


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'user_permissions')


class FamiliarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Familiar
        fields = '__all__'


class AvanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avance
        fields = '__all__'


class CapacitacionInscritaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CapacitacionInscrita
        fields = '__all__'
