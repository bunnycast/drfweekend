from django.contrib.auth.models import User
from django.db import models


class Cards(models.Model):
    class CHOICE(models.TextChoices):
        shinhan = 'sh'
        kookmin = 'km'
        hana = 'hn'
        kakaobank = 'kkb'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")  # related name?
    cardname = models.CharField(max_length=32, choices=CHOICE.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    is_credit = models.BooleanField(default=True)
