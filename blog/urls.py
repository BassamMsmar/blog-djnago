from django.urls import path
from .views import  PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('blog/', PostList.as_view(), name='posts' ),
    path('blog/<int:pk>', PostDetail.as_view(), name='post_detail' ),
    path('blog/new', PostCreate.as_view(), name='post_create' ),
    path('blog/<int:pk>/ubdate', PostUpdate.as_view(), name='post_update' ),
    path('blog/<int:pk>/delete', PostDelete.as_view(), name='post_delete' ),
]
