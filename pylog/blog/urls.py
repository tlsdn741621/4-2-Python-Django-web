# DefaultRouter를 생성합니다.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet

router = DefaultRouter()
# 'post'라는 URL prefix에 PostViewSet을 등록합니다.
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]