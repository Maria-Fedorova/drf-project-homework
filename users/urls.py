from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

from users.views import PaymentViewSet, UserViewSet

app_name = UsersConfig.name
router = SimpleRouter()
router.register("user", UserViewSet)
router.register(r"payment", PaymentViewSet)

urlpatterns = []

urlpatterns += router.urls
