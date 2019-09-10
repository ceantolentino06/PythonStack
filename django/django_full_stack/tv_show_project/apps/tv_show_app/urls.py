from django.conf.urls import url
from . import views
                    
urlpatterns = [
    ######### ridirect to index #######
    url(r'^$', views.root),

    ######### index route #########
    url(r'^shows$', views.index),

    ######### render create show page ############
    url(r'^shows/new$', views.add_show_render),

    ######### show profile #############
    url(r'^shows/(?P<id>[0-9]+)$', views.show),

    ######### create show process #########
    url(r'^shows/add_show$', views.add_show),

    ######### render edit show page ##########
    url(r'^shows/(?P<id>[0-9]+)/edit$', views.edit_show_render),

    ######### edit show process ##############
    url(r'^shows/edit_process$', views.edit_show),

    ######### delete show process ############
    url(r'^shows/(?P<id>[0-9]+)/destroy$', views.delete_show),
]