from django.conf.urls import patterns, include, url

from .views import home, overview, detail, index, well

dataset_q = r'(?P<dataset_id>[0-9]+)'
well_q = r'/well/(?P<well>[0-9]+)'
dye_q = r'/dye/(?P<dye>\w+)'

urlpatterns = patterns('',
                       url(r'^$', home, name='home'),
                       url(r'^(?P<dataset_id>[0-9]+)/$',
                           overview, name='overview'),
                       url(r'^(?P<dataset_id>[0-9]+)/detail/$',
                           detail, name='detail'),
                       url(r'^api/index$', index, name='index'),
                       url(r'^' + dataset_q + well_q + dye_q, well,
                           name='well'),
                       url(r'^api/model/' + dataset_q + well_q + dye_q, well,
                           name='model')
                       )
