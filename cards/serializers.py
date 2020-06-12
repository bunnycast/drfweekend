from rest_framework.serializers import ModelSerializer

from cards.models import Cards


class CardsSerializer(ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id', 'user', 'cardname', 'created_at', 'is_credit',)
