# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from usuarios.models import User, Familiar, Avance, CapacitacionInscrita
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'


class AvanceSerializer(serializers.ModelSerializer):

    #usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Avance
        exclude = ('usuario', 'id')


class UserSerializer(serializers.ModelSerializer):

    avances = AvanceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        #exclude = ('user_permissions',)
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class FamiliarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Familiar
        fields = '__all__'


class CapacitacionInscritaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CapacitacionInscrita
        fields = '__all__'
