from django.db import models


# Create your models here.
class PostItem(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    # image = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now=True)
