from django.conf.urls.defaults import *
from cijug.news import views

urlpatterns = patterns('news',
    url(r'^$', views.index, name="index"),
)