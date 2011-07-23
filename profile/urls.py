from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('profile.view',

    url(r'^profile/$', 'profile_home'),
    url(r'^profile/update/$', 'profile_update'),

)
