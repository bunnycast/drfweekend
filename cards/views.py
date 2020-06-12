from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from cards.models import Cards
from cards.serializers import CardsSerializer


class CardsViewset(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

    authentication_classes = [TokenAuthentication]
