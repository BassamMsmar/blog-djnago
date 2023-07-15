from django.urls import path
from .views import posts, post_detail, post_delete, post_edit, post_new

urlpatterns = [
    path('', posts, name='posts' ),
    path('post/new', post_new, name='post_new' ),
    path('post/<int:post_id>', post_detail, name='post_detail' ),
    path('post/<int:post_id>/edit', post_edit, name='post_edit' ),
    path('post/<int:post_id>/delete', post_delete, name='post_delete' ),
]
