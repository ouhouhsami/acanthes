from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'archives.views.home', name='home'),
    url(r'(?P<pk>[-\w]+)$', 'archives.views.detail', name='detail'),
)