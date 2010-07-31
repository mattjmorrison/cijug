from django.conf.urls.defaults import *
from cijug.microblog import views

urlpatterns = patterns('microblog',
    url(r'^$', views.index, name="index"),
)