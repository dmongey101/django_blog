from django.urls import path
from blog.views import get_unpublished_posts, write_post, read_post, edit_post, publish_post

urlpatterns = [
    path('unpublished', get_unpublished_posts, name='get_unpublished_posts'),
    path('write/', write_post, name='write_post'),
    path('<int:id>/', read_post, name='read_post'),
    path('<int:id>/edit/', edit_post, name='edit_post'),
    path('<int:id>/publish/', publish_post, name='publish_post')
]