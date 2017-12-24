"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from forum import views
from django.conf.urls import include, url
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from cbot.views import ChatterBotAppView

app_name="chatterbot"

urlpatterns = [
    url(r'admin/', admin.site.urls),
    #url(r'^time/$', views.current_datetime),
    #url(r'^time/(\d{1,2})/$', views.page_counter),
    url(r'^$', views.homepage),
    #url(r'^scripts/(?P<path>.*)$', serve, {'document_root': './scripts'}),
    url(r'^board/$', views.index),
    url(r'^board/writeSubject/$', views.writeSubject),
    url(r'^postSubject/$', views.postSubject),
    url(r'^(?P<subject_id>\d+)/$', views.readSubject),
    url(r'^(?P<subject_id>\d+)/add/$', views.addComment),
    url(r'^(?P<subject_id>\d+)/postComment/$', views.postComment),
    url(r'^chatterBot/$', ChatterBotAppView.as_view(), name='cbot_main'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^tourist2\.csv$', views.tourist),
    url(r'^data/$', views.data),

    #url(r'^api/chatterbot/', chatterbot_urls, namespace='chatterbot'),
    #url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot', app_name='chatterbot')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


