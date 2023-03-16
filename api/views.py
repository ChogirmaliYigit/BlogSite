from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from blog.models import Post, SocialLink, Skill, Service, Portfolio, Feedback, Tag, Reply, Comment, ContactUser
from blog.serializers import PostSerializer, SocialLinkSerializer, SkillSerializer, ServiceSerializer, PortfolioSerializer, FeedbackSerializer, TagSerializer, CommentSerializer, ReplySerializer, ContactUserSerializer

class PostsAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

class SocialLinksAPIView(ListCreateAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

class SocialLinkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    lookup_field = 'pk'

class SkillsAPIView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'pk'

class ServicesAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'

class PortfoliosAPIView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = 'pk'

class FeedbacksAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'

class TagsAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'

class ReplysAPIView(ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    lookup_field = 'pk'

class CommentsAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

class ContactUsersAPIView(ListCreateAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer

class ContactUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer
    lookup_field = 'pk'
