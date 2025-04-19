from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
]