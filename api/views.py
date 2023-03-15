from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post
from .serializers import PostSerializer, SocialLinkSerializer

class PostsAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-id').values()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)