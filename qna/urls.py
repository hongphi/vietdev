from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('qna.views',
    #url(r'^$', 'home', name = 'home-page'),
    url(r'^$','ask'),
    url(r'list/','list'),
)
