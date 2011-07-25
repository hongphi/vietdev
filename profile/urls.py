from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('profile.views',

    url(r'^profile/$', 'profile_home'),
    url(r'^profile/update/$', 'profile_update'),

)
