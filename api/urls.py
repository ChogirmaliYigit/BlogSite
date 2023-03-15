from django.urls import path
from .views import PostsAPIView

urlpatterns = [
    path('posts/', PostsAPIView.as_view(), name='posts'),
]
