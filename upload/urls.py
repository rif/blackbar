from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from models import Photo

urlpatterns = patterns('',
    url(r'^$',  ListView.as_view(
            queryset=Photo.objects.order_by('-pub_date'),
            context_object_name='latest_photo_list',
            template_name='upload/index.html',
            paginate_by = 1),
        name='index'),
    url(r'^upload/$', 'upload.views.upload', name='upload'),
    url(r'^fullcaption/(?P<id>\d+)/$', 'upload.views.get_full_caption', name='get_full_caption'),
)
