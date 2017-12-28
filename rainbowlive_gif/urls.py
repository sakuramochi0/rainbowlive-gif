from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(\d+)/$', views.page, name='page'),
    url(r'^tag/([^/]+)/$', views.tag, name='tag'),
    url(r'^tag/([^/]+)/(\d+)/$', views.tag, name='tag'),
    url(r'api/update-tag/$', views.update_tag),
]
