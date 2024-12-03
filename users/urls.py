from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

from users.views import UserViewSet, UserCreateAPIView, PaymentCreateAPIView, PaymentListAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name
router = SimpleRouter()
router.register("user", UserViewSet)


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payment/list/", PaymentListAPIView.as_view(), name="payment_list"),
]

urlpatterns += router.urls
