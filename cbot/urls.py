from django.conf.urls import include, url
from django.contrib import admin
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import ChatterBotAppView

app_name="chatterbot"


urlpatterns = [
    url(r'^chatterBot/$', ChatterBotAppView.as_view(), name='cbot_main'),
    #url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)