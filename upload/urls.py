from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from models import Photo

urlpatterns = patterns('',
    url(r'^$',  ListView.as_view(
            queryset=Photo.objects.order_by('-pub_date')[:5],
            context_object_name='latest_photo_list',
            template_name='upload/index.html'),
        name='index'),
    url(r'^upload/$', 'upload.views.upload', name='upload'),
)
