from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('profile.views',

    url(r'^$', 'profile_home'),
    url(r'^update/$', 'profile_update'),

)
