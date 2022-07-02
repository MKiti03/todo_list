from authentication.models import User
from rest_framework import serializers

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"