from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from cards.serializers import CardsSerializer


class UserSerializer(ModelSerializer):
    cards = CardsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cards',)
