from django.urls import path
from .views import posts, post_detail

urlpatterns = [
    path('', posts, name='posts' ),
    path('detail/<int:post_id>', post_detail, name='post_detail' ),
]
