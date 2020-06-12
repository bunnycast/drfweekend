from rest_framework.viewsets import ModelViewSet

from cards.models import Cards
from cards.serializers import CardsSerializer


class CardsViewset(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

