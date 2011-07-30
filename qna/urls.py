from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('qna.views',
    #url(r'^$', 'home', name = 'home-page'),
    url(r'^$','list_question'),
    url(r'^ask/$','ask'),
    url(r'^question/(?P<id>\d+)/$','show_question'),
    url(r'^answer/(?P<id_question>\d+)/$','answer'),
    url(r'like_answer/(?P<id>\d+)/$','like_answer'),
    url(r'like_question/(?P<id>\d+)/$','like_question'),
)
