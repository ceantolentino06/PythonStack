from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_user$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^register_user$', views.register),
]