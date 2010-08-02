from django.conf.urls.defaults import *
from cijug.microblog import views

urlpatterns = patterns('microblog',
    url(r'^/?$', views.index, name="index"),
    url(r'^edit/(?P<id>\d+)/?', views.edit, name="edit"),
    url(r'^add/?', views.add, name="add"),
    url(r'^save_edit/(?P<id>\d+)/?', views.save_edit, name="save_edit"),
    url(r'^save_add/?', views.save_add, name="save_add"),
    url(r'^delete/(?P<id>\d+)/?', views.delete, name="delete"),
)