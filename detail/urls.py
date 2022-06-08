from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.view_detail, name='view-detail' ),
    path('detail/like/<int:id>', views.like_post, name='like-post'),
]