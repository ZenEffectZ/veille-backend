from django.contrib import admin

# Register your models here.
from .models import PostItem

admin.site.register(PostItem)