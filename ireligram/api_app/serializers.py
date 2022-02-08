from rest_framework import serializers
from .models import PostItem


class PostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostItem
        fields = '__all__'
