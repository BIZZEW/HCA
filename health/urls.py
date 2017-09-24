from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'health'

urlpatterns = [
    # /health/login/
    url(r'^login/$', login, {'template_name': 'health/login.html'}, name='login'),

    # /health/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /health/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /health/hdata/add/
    url(r'hdata/add/$', views.HdataCreate.as_view(), name='hdata-add'),

    # /health/hdata/2/
    url(r'hdata/(?P<pk>[0-9]+)/$', views.HdataUpdate.as_view(), name='hdata-update'),

    # /health/album/2/delete/
    url(r'hdata/(?P<pk>[0-9]+)/delete/$', views.HdataDelete.as_view(), name='hdata-delete'),

    # /health/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

