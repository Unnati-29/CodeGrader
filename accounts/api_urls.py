from django.urls import path
from .api_views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='api-register'),
    path('auth/login/', LoginView.as_view(), name='api-login'),
    path('auth/profile/', ProfileView.as_view(), name='api-profile'),
]