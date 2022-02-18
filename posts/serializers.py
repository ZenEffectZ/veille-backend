from rest_flex_fields import FlexFieldsModelSerializer
from .models import PostItem, CommentItem, ImageItem
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
import base64, uuid
from django.core.files.base import ContentFile
from rest_framework import serializers

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class PostItemSerializer(FlexFieldsModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)
    # image = VersatileImageFieldSerializer(
    #     sizes=[
    #         ('full_size', 'url'),
    #         ('thumbnail', 'thumbnail__100x100'),
    #     ]
    # )
    class Meta:
        model = PostItem
        fields = ['pk', 'content', 'created', 'updated', 'user_id', 'image']
        # expandable_fields = {
        #     # 'category': ('reviews.CategorySerializer', {'many': True}),
        #     # 'sites': ('reviews.ProductSiteSerializer', {'many': True}),
        #     'post': 'posts.CategorySerializer',
        #     'user_id': 'posts.UserSerializer',
        #     'comments': ('posts.CommentSerializer', {'many': True}),
        #     'image': ('posts.ImageSerializer', {'many': True})
        # }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CommentItem
        fields = ['pk', 'title', 'created', 'updated']
        expandable_fields = {
            'post_id': 'posts.CategorySerializer',
            'user_id': 'posts.UserSerializer'
        }


class ImageItemSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = ImageItem
        fields = ['pk', 'name', 'image']
