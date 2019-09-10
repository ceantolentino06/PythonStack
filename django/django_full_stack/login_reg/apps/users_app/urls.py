from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_user$', views.login),
    url(r'^success$', views.wall),
    url(r'^logout$', views.logout),
    url(r'^register_user$', views.register),
    url(r'^wall/post_message$', views.post_message),
    url(r'^wall/post_comment$', views.post_comment),
    url(r'^wall/(?P<id>[0-9]+)/delete_message$', views.delete_message),
]