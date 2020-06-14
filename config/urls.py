"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# 8.4 장고에서의 세팅 임포팅
from django.conf import settings
from django.conf.urls.static import static

# 8.4
# 10.0 : 장고가 url을 서치할 때 config의 array 순서대로 검색함
urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]
# 디버깅 상태일 때만 사용, static이나 업로드파일을 서버에서 사용하면 서버과부하가 많아서 절대 사용안함. db.sqlite3도 사용안할 거임
# AWS에 올릴때 이를 분리하여 DB전용 서버로업로드하는 방법을 알려줄거임
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 8.4
