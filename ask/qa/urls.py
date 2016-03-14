from django.conf.urls import patterns, include, url

from qa.views import test

urlpatterns = patterns('qa.views',
   url(r'^$', 'mainpage', name='index'),
   url(r'^login/', 'test', name='login'),
   url(r'^signup/', 'test', name='signup'),
   url(r'^question/(?P<slug>\w+)/$', 'qs_ans', name='question'),
   url(r'^ask/', 'qs_add', name='ask'),
   url(r'^answer/', 'ans_add', name='ans'),
   url(r'^popular/', 'pop', name='popular'),   
   url(r'^new/', 'test', name='new'),  
)

