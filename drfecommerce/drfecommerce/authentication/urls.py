from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

# router = DefaultRouter()
# router.register(r"register", RegisterView.as_view(), name="register")


urlpatterns = [
    # path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verify/", VerifyEmailView.as_view(), name="email-verify"),
    path("login/", LoginAPIView.as_view(), name="login")
]
