from django.conf.urls.defaults import *
from cijug.microblog import views

urlpatterns = patterns('',
    (r'^$', views.index),    
)