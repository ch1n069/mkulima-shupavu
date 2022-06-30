from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.Serializer):

    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'contact')
