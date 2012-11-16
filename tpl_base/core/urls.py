from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^thanks/$', 'thanks', name='thanks'),
    url(r'^unsubscribe/done/$', 'unsubscribe_done', name='unsubscribe_done'),
    url(r'^unsubscribe/(?P<card_number>.*)/$', 'unsubscribe', name='unsubscribe'),
)
