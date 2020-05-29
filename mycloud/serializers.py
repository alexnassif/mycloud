from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['video_url', 'title', 'description', 'created_at']