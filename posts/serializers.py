from rest_flex_fields import FlexFieldsModelSerializer
from .models import PostItem, CommentItem, ImageItem
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer


class PostItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PostItem
        fields = ['pk', 'title', 'content', 'created', 'updated', 'user_id']
        expandable_fields = {
            # 'category': ('reviews.CategorySerializer', {'many': True}),
            # 'sites': ('reviews.ProductSiteSerializer', {'many': True}),
            'post': 'posts.CategorySerializer',
            'user_id': 'posts.UserSerializer',
            'comments': ('posts.CommentSerializer', {'many': True}),
            'image': ('posts.ImageSerializer', {'many': True})
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CommentItem
        fields = ['pk', 'title', 'created', 'updated']
        expandable_fields = {
            'post': 'posts.CategorySerializer',
            'user': 'posts.UserSerializer'
        }


class ImageItemSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = ImageItem
        fields = ['pk', 'name', 'image']

