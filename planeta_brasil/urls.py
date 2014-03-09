#coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
	#url(r'^$', 'planeta_brasil.api_copa.views.home', name='home'),
    url(r'^api-copa/news/$', 'planeta_brasil.api_copa.views.api_copa_news', name='api_copa_news'),
    url(r'^api-copa/videos/$', 'planeta_brasil.api_copa.views.api_copa_news', name='api_copa_videos'),
    url(r'^api-copa/register-push-device/$', 'planeta_brasil.api_copa.views.register_push_device', name='register_push_device'),

    

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
