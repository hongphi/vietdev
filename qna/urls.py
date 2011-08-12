from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('qna.views',
    #url(r'^$', 'home', name = 'home-page'),
    url(r'^$','home_list'),
    url(r'^page/(?P<page>\d+)/$','list_question'),
    url(r'^ask/$','ask'),
    url(r'unlike/(?P<type>\w+)/(?P<id>\d+)/$','unlike'),
    url(r'^question/(?P<id>\d+)/$','show_question'),
    url(r'^answer/(?P<id_question>\d+)/$','answer'),
    url(r'like/(?P<type>\w+)/(?P<id>\d+)/$','like'),
    url(r'tags/$','tags_all'),
    url(r'tags/(?P<name>\w+)/$','question_by_tag'),
    url(r'tags/edit-tag-wiki/(?P<id>\d+)/$', 'edit_tag_wiki'),
    url(r'tags/edit-tag-wiki/submit/(?P<id>\d+)/$', 'edit_tag_wiki_submit'),
)
