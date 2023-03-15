from django.urls import path
from .views import PostsAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PostsAPIView.as_view(), name='posts'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),
]

