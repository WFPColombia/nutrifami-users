import json
from django.views.generic import TemplateView
from django.contrib.auth import logout, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_social_auth.serializers import UserSerializer
from rest_social_auth.views import JWTAuthMixin
from django.core import serializers
from usuarios.serializers import CustomUserSerializer
from usuarios.models import CustomUser


class HomeSessionView(TemplateView):
    template_name = 'home_session.html'

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super(HomeSessionView, self).get(request, *args, **kwargs)


class HomeTokenView(TemplateView):
    template_name = 'home_token.html'


class HomeJWTView(TemplateView):
    template_name = 'home_jwt.html'


class LogoutSessionView(APIView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseDetailView(generics.RetrieveAPIView):
    permission_classes = IsAuthenticated,
    serializer_class = UserSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserSessionDetailView(BaseDetailView):
    authentication_classes = (SessionAuthentication, )


class UserTokenDetailView(BaseDetailView):
    authentication_classes = (TokenAuthentication, )


class UserJWTDetailView(JWTAuthMixin, BaseDetailView):
    pass


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = CustomUser.objects.get(pk=token.user_id)
        serializer = CustomUserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
