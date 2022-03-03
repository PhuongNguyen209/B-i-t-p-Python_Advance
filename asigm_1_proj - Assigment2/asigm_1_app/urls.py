from django.conf.urls import url
from . import views

app_name = "asigm1"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
]