"""
URL configuration for pylog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pylog.views import index
from blog.views import post_list

from django.conf import settings
from django.conf.urls.static import static

from blog.views import post_list, post_detail, post_add

# --- Swagger 관련 라이브러리 import ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="블로그 API 서비스 문서",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail),
    path('posts/add/',post_add),
    path('api/', include('blog.urls')),
# --- Swagger URL patterns ---
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
# 이미지 출력시 필요한 설정 추가
urlpatterns += static(
    # URL의 접두어가 MEDIA_URL 일 때는 정적파일을 돌려준다.
    prefix=settings.MEDIA_URL,
    # 돌려줄 디렉터리는 MEDIA_ROOT 를 기준으로 한다.
    document_root=settings.MEDIA_ROOT
)
