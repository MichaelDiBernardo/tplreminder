from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^page/(?P<page>.+)/$', 'page', name='page'),
    url(r'^unsubscribe/(?P<card_number>.*)/$', 'unsubscribe', name='unsubscribe'),
)
