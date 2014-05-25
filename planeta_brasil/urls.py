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
	
	
	url(r'^api/matches_by_groups/$', 'planeta_brasil.api_copa.views.api_matches_by_groups', name='api_matches_by_groups'),
	url(r'^api/guesses/$', 'planeta_brasil.api_copa.views.api_guesses', name='api_guesses'),
	url(r'^api/photos/$', 'planeta_brasil.api_copa.views.api_photos', name='api_photos'),
	url(r'^api/news/(?P<pk>\d)/$', 'planeta_brasil.api_copa.views.api_news_detail', name='api_news_detail'),
	url(r'^api/news/$', 'planeta_brasil.api_copa.views.api_news', name='api_news'),
	url(r'^api/last_games/$', 'planeta_brasil.api_copa.views.api_last_games', name='api_last_games'),
	url(r'^api/venue/(?P<pk>\d)/$', 'planeta_brasil.api_copa.views.api_venue_detail', name='api_venue_detail'),
	url(r'^api/finals/$', 'planeta_brasil.api_copa.views.api_finals', name='api_finals'),
	url(r'^api/home/$', 'planeta_brasil.api_copa.views.api_home', name='api_home'),

	#url(r'^api/home/$', 'planeta_brasil.api_copa.views.home', name='api_home'),
	
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
