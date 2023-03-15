from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from blog.models import Post
from blog.serializers import PostSerializer, SocialLinkSerializer, SkillSerializer, ServiceSerializer, PortfolioSerializer, FeedbackSerializer, TagSerializer, CommentSerializer, ReplySerializer, ContactUserSerializer

class PostsAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

