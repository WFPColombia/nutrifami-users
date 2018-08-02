# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from usuarios.models import User, Familiar, Avance, CapacitacionInscrita, Training, Trainee, TraineeAdvance
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'


class AvanceSerializer(serializers.ModelSerializer):

    usuario = serializers.ReadOnlyField(source='usuario.id')

    class Meta:
        model = Avance
        exclude = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):

    avances = AvanceSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ('user_permissions', 'password',
                   'is_superuser', 'is_active')
        #fields = '__all__'
        read_only_fields = ('date_created', 'date_modified',)

    def update(self, instance, validated_data):

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class UserCreateSerializer(serializers.ModelSerializer):

    avances = AvanceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ('user_permissions',
                   'is_superuser', 'is_staff', 'is_active')
        read_only_fields = ('date_created', 'date_modified',)

    def create(self, validated_data):
        if 'is_trainee' in validated_data.keys():
          trainee = validated_data['is_trainee']
        else:
          trainee = False
        user = User.objects.create(
            username=validated_data['username'],
            terminos=validated_data['terminos'],
            is_trainee=trainee
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserCheckSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class FamiliarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Familiar
        fields = '__all__'


class CapacitacionInscritaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CapacitacionInscrita
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = '__all__'


class TraineeAdvanceSerializer(serializers.ModelSerializer):

    #trainee_document = serializers.ReadOnlyField(source='trainee.document')

    class Meta:
        model = Avance
        exclude = ('id',)


class TraineeSerializer(serializers.ModelSerializer):

    trainee_advance = TraineeAdvanceSerializer(many=True, read_only=True)

    class Meta:
        model = Trainee
        fields = ('id', 'name', 'document', 'trainee_advance')
