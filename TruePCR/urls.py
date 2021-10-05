from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TruePCR.views.home', name='home'),
    #url(r'^$', 'TruePCR.views.dashboard', name='dashboard'),
    #url(r'^$', 'TruePCR.apps.datasets.views.home', name='datasets'),
    url(r'^', include('TruePCR.apps.datasets.urls',
                       namespace='datasets',
                       app_name='datasets')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
