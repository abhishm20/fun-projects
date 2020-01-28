from rest_framework import generics, permissions


from .serializers import UserSerializer
from .models import User


class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(UserMixin, generics.RetrieveAPIView):
    lookup_field = 'username'

