from django.contrib import admin
from django.urls import path, include
import homeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # home 앱 URL
    path('', homeapp.views.home, name="home"),
    path('about/', homeapp.views.about, name="about"),

    # 나머지 앱 URL 관리를 위해 include 사용
    path('writeapp/', include('writeapp.urls')),
    path('accountsapp/', include('accountsapp.urls')),
    path('communityapp/', include('communityapp.urls')),
]
