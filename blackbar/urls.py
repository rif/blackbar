from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('', include('upload.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
