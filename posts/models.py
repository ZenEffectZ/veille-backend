from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField


class PostItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postitems', related_query_name='postitem')
    image = models.CharField(max_length=100, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class CommentItem(models.Model):
    title = models.CharField(max_length=255)
    post = models.ForeignKey(PostItem, on_delete=models.CASCADE, related_name='commentsitems', related_query_name='commentitem')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentsitems', related_query_name='commentitem')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ImageItem(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='postimages/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name