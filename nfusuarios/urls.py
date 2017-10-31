"""nfusuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as views_rest
from rest_framework.routers import DefaultRouter

from usuarios import views

urlpatterns = [
    url(r'^$', views.HomeTokenView.as_view(), name='home'),
    url(r'^token/$', views.HomeTokenView.as_view(), name='home_token'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', views_rest.obtain_auth_token),
    #url(r'^api-token-generate/', views.get_all_tokens),
    url(r'^api-token-auth/', views.CustomObtainAuthToken.as_view()),

    url(r'^api/login/', include('rest_social_auth.urls_token')),
    url(r'^api/login/', include('rest_social_auth.urls_session')),

    url(r'^api/logout/session/$',
        views.LogoutSessionView.as_view(), name='logout_session'),
    url(r'^api/user/session/', views.UserSessionDetailView.as_view(),
        name="current_user_session"),
    url(r'^api/user/token/', views.UserTokenDetailView.as_view(),
        name="current_user_token"),
    url(r'^api/user/jwt/', views.UserJWTDetailView.as_view(), name="current_user_jwt"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/password_reset/$', auth_views.password_reset,
        name='admin_password_reset'),
    url(r'^admin/password_reset/done/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
]
