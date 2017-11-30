from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$', views.page, name='page'),
    url(r'api/update-tag/$', views.update_tag),
]
