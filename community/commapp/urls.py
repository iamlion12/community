from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'^community/(?P<pk>\d+)/$', views.community, name='community'),
    url(r'^post/new/$', views.new_post, name='new_post'),
]
