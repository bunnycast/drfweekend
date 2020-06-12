from django.apps import AppConfig

from cards.models import Cards


class CardsConfig(AppConfig):
    name = Cards
    fields = ('id', 'user', )
