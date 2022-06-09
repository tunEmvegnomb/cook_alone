from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.view_detail, name='view-detail' ),
    path('detail/like/<int:id>', views.like_post, name='like-post'),
    path('detail/comment/<int:id>', views.comment_post, name='comment-post'),
    path('detail/comment/delete/<int:id>', views.comment_delete, name='comment-delete'),
    path('detail/comment/update/<int:id>', views.comment_update, name='comment-update'),
    path('detail/comment/update_end/<int:id>', views.comment_update_end, name='comment-update-end'),
]