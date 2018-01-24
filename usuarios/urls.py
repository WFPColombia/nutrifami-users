from django.conf.urls import url, include
from rest_framework.authtoken import views as views_rest
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from usuarios import views

router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'familiares', views.FamiliarViewSet)
router.register(r'avances', views.AvanceViewSet)
router.register(r'capacitaciones-inscritas',
                views.CapacitacionInscritaViewSet)
router.register(r'training', views.TrainingViewSet)
router.register(r'trainees', views.TraineeViewSet)
router.register(r'trainee-advance', views.TraineeAdvanceViewSet)

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),  # <-  Borrar
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    #url(r'^api-token-generate/', views.get_all_tokens),
    url(r'^token-auth/', views.CustomObtainAuthToken.as_view()),
    url(r'^create-user/', views.CreateUserView.as_view()),
    url(r'^avance-user/', views.AvanceUserView.as_view()),
    url(r'^login/', include('rest_social_auth.urls_token')),
    url(r'^logout/session/$', views.LogoutSessionView.as_view(), name='logout_session'),
    url(r'^user/token/', views.UserTokenDetailView.as_view(),
        name="current_user_token"),
]
