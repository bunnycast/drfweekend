from rest_framework.routers import SimpleRouter

from users.views import UserViewset

router = SimpleRouter(trailing_slash=False)
router.register(r'api/users', UserViewset)

urlpatterns = router.urls
