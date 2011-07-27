from django.conf.urls.defaults import patterns, include, url
from django.contrib.sitemaps import Sitemap
from forms import RegistrationFormUtfUsername


from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUtfUsername})

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^qna/', include('qna.urls')),
    url(r'^profile/', include('profile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^account/', include(authopenid_urlpatterns)),
)
