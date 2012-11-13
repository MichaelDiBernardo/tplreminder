from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^thanks/$', 'thanks', name='thanks'),
)
