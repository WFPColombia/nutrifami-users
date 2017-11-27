# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from usuarios.models import User, Familiar


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ('password', 'user_permissions')


class FimiliarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Familiar
		fields = '__all__'
