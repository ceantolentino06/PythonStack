from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<id>[0-9]+)$', views.view),
    url(r'^add_book_author$', views.add_book_author),
    url(r'^add_author$', views.add_author),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<id>[0-9]+)$', views.view_author),
    url(r'^add_author_book$', views.add_author_book),
]