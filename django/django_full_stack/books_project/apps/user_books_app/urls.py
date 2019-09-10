from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_user$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^register_user$', views.register),
    url(r'^books/(?P<book_id>[0-9]+)$', views.show),
    url(r'^books/add_book$', views.add_book),
    url(r'^books/(?P<book_id>[0-9]+)/add_to_fav_success$', views.add_to_fav_success),
    url(r'^books/(?P<book_id>[0-9]+)/add_to_fav_view$', views.add_to_fav_view),
    url(r'^books/(?P<book_id>[0-9]+)/update$', views.update),
    url(r'^books/(?P<book_id>[0-9]+)/delete$', views.delete),
    url(r'^books/(?P<book_id>[0-9]+)/remove_to_fav$', views.remove_to_fav),
]