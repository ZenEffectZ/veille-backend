from django.urls import path
from .views import PostItemViews

urlpatterns = [
    path('posts/', PostItemViews.as_view()),
    path('posts/<int:id>', PostItemViews.as_view())
]