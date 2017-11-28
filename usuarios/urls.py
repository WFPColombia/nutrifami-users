from django.conf.urls import url, include
from rest_framework.authtoken import views as views_rest
from rest_framework.routers import DefaultRouter
from usuarios import views

router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'familiares', views.FamiliarViewSet)
router.register(r'avances', views.AvanceViewSet)
router.register(r'capacitaciones-inscritas',
                views.CapacitacionInscritaViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views_rest.obtain_auth_token),
    #url(r'^api-token-generate/', views.get_all_tokens),
    url(r'^token-auth/', views.CustomObtainAuthToken.as_view()),
    url(r'^login/', include('rest_social_auth.urls_token')),
    url(r'^logout/session/$', views.LogoutSessionView.as_view(), name='logout_session'),
    url(r'^user/token/', views.UserTokenDetailView.as_view(),
        name="current_user_token"),
]
