from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.test_views),
    url(r'^node/(?P<pk>[\d\-]+)/$', views.node_detail),
    url(r'^app/(?P<pk>[\d\-]+)/$', views.app_detail),
    url(r'^size/(?P<pk>[\d\-]+)/$', views.size),
    url(r'^operation/(?P<pk>[\d\-]+)/$', views.op_detail),
    url(r'^state/(?P<pk>[\d\-]+)/$', views.state_detail),
    url(r'^finishApp/(?P<pk>[\d\-]+)/$', views.finish_application),
]
