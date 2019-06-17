"""yybzuoye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from douban import views
from dj.views import JdShow
from login12306.views import Index
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
                  # url(r'^admin/', admin.site.urls),
                  url(r'^pachong/$', views.deal),
                  url(r'^$', views.MovieShow.as_view(), name='movie_list'),
                  url(r'^download/$', views.download_img),
                  url(r'^jd/$', JdShow.as_view(), name='jd_list'),
                  url(r'^12306/$', Index.as_view(), name='code'),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
                  url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加入这个才能显示media文件
