import json
from django.views.generic import TemplateView
from django.contrib.auth import logout, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route
#from rest_social_auth.serializers import UserSerializer
from rest_social_auth.views import JWTAuthMixin
from django.core import serializers
from usuarios.serializers import UserSerializer, UserCreateSerializer, FamiliarSerializer, AvanceSerializer, CapacitacionInscritaSerializer
from usuarios.models import User, Familiar, Avance, CapacitacionInscrita
from usuarios.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'usuarios': reverse('usuarios-list', request=request, format=format),
        'avances': reverse('avance-list', request=request, format=format)
    })


class HomeView(TemplateView):
    template_name = 'home.html'


class LogoutSessionView(APIView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseDetailView(generics.RetrieveAPIView):
    permission_classes = permissions.IsAuthenticated,
    serializer_class = UserSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserTokenDetailView(BaseDetailView):
    authentication_classes = (TokenAuthentication, )


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(pk=token.user_id)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    serializer_class = UserCreateSerializer


class FamiliarViewSet(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AvanceViewSet(viewsets.ModelViewSet):
    queryset = Avance.objects.all()
    serializer_class = AvanceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AvanceUserView(generics.ListAPIView):
    serializer_class = AvanceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Avance.objects.filter(usuario=user)


class CapacitacionInscritaViewSet(viewsets.ModelViewSet):
    queryset = CapacitacionInscrita.objects.all()
    serializer_class = CapacitacionInscritaSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
