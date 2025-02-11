from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login: Get Access & Refresh Tokens
    TokenRefreshView,  # Refresh Access Token
    TokenVerifyView,  # Verify if Token is Valid
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify Token
]
