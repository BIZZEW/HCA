from django.conf.urls import url
from . import views

app_name = 'health'

urlpatterns = [
    # /health/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /health/hdata/add/
    url(r'hdata/add/$', views.HdataCreate.as_view(), name='hdata-add'),

    # /health/hdata/2/
    url(r'hdata/(?P<pk>[0-9]+)/$', views.HdataUpdate.as_view(), name='hdata-update'),

    # /health/album/2/delete
    url(r'hdata/(?P<pk>[0-9]+)/delete/$', views.HdataDelete.as_view(), name='hdata-delete'),

    # /health/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

