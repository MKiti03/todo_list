from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from authentication.models import User
from .serializers import UserListSerializer
from rest_framework import permissions



class UserListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserListSerializer
    queryset = User.objects.all()