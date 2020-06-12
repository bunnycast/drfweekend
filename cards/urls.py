from rest_framework.routers import SimpleRouter

from cards.views import CardsViewset

router = SimpleRouter(trailing_slash=False)
router.register(r'api/cards', CardsViewset)

urlpatterns = router.urls
