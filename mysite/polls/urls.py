from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="Index"),
    url(r'^(?P<questionid>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<questionid>[0-9]+)/result$', views.result, name="result"),
    url(r'^(?P<questionid>[0-9]+)/vote$', views.vote, name="vote"),


]
