from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views as acc_view
from posts import views as posts_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

posts_router = DefaultRouter()
posts_router.register('tweet', posts_view.TweetViewSet)
posts_router.register('comment', posts_view.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/accounts/', include(acc_router.urls)),
    path('api/posts/', include(posts_router.urls)),
]
