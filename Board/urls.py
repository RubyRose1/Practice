from django.conf.urls import url,  include
import Board
from Board import views

urlpatterns = [
    url(r'^$', Board.views.home, name='home'),
    url(r'^about/$', Board.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', Board.views.show_article, name='article'),
]
