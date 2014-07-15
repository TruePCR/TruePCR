from django.conf.urls import patterns, include, url

from .views import home, detail

urlpatterns = patterns('',
                       url(r'^$', home, name='home'),
                       url(r'^(?P<dataset_id>[0-9]+)/$', detail, name='detail')
                       )
