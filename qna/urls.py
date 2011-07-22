from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('qna.views',
    url(r'^$', 'home', name = 'home-page'),

)
