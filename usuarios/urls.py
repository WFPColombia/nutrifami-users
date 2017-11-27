from django.conf.urls import url, include
from usuarios import views

urlpatterns = [
    url(r'^$', views.HomeTokenView.as_view(), name='home'),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', views_rest.obtain_auth_token),
    #url(r'^api-token-generate/', views.get_all_tokens),
    #url(r'^token-auth/', views.CustomObtainAuthToken.as_view()),
    #url(r'^login/', include('rest_social_auth.urls_token')),
    #url(r'^logout/session/$',views.LogoutSessionView.as_view(), name='logout_session'),
    #url(r'^user/token/', views.UserTokenDetailView.as_view(),name="current_user_token"),    
]