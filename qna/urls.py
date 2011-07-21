from django.conf.urls.defaults import *

urlpatterns = patterns('qna.views',
    url(r'^$', 'home', name='home-page'),

)