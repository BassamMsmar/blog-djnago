from django.urls import path
from .views import  PostList, post_detail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='posts' ),
    path('blog/<int:pk>', post_detail, name='post_detail' ),
    path('blog/new', PostCreate.as_view(), name='post_create' ),
    path('blog/<int:pk>/ubdate', PostUpdate.as_view(), name='post_update' ),
    path('blog/<int:pk>/delete', PostDelete.as_view(), name='post_delete' ),
]
