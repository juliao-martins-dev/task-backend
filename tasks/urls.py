from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)
from .views import UserViewSet, TaskViewSet, CustomTokenObtainPairView


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"tasks", TaskViewSet, basename="task")


urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refres")
]