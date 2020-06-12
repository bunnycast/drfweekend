from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
