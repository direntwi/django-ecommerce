from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

# router = DefaultRouter()
# router.register(r"register", RegisterView.as_view(), name="register")


urlpatterns = [
    # path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verify/", VerifyEmailView.as_view(), name="email-verify"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<str:uidb64>/<str:token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]
