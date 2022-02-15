from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet
from posts.views import PostItemViewSet, PostItemDetailApiView, PostsUserApiView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'reviews', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')
# router.register(r'posts', PostItemViewSet, basename='PostItem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('api/', include(router.urls)),
    path('posts/', PostItemViewSet.as_view()),
    path('posts/<int:post_id>', PostItemDetailApiView.as_view()),
    path('user/<int:user_id>', PostsUserApiView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
