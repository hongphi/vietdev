from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('profile.views',

    url(r'^$', 'profile_home'),
    url(r'^(?P<username>\w+)/$', 'view_profile'),
    url(r'^(?P<username>\w+)/update/$', 'profile_update'),

)
