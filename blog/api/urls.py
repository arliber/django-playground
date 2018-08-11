from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.posts, name='posts'),
    path('authors', views.authors, name='authors'),
    path('new-post', views.new_post, name='new_post'),
    path('recently-published', views.recently_published_posts, name='recently_published_posts'),
]