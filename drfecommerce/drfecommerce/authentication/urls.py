from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r"register", RegisterView.as_view(), name="register")


urlpatterns = [
    # path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register")
]
