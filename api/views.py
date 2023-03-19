from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from blog.models import Post, SocialLink, Skill, Service, Portfolio, Feedback, Tag, Reply, Comment, ContactUser
from blog.serializers import PostSerializer, SocialLinkSerializer, SkillSerializer, ServiceSerializer, PortfolioSerializer, FeedbackSerializer, TagSerializer, CommentSerializer, ReplySerializer, ContactUserSerializer
from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET')

class ReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
        )


class PostsAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ReadOnly]

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permission_classes = [ReadOnly]

class SocialLinksAPIView(ListCreateAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [ReadOnly]

class SocialLinkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    lookup_field = 'pk'

class SkillsAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'pk'

class ServicesAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'

class PortfoliosAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = 'pk'

class FeedbacksAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    # queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    def get_queryset(self):
        return Feedback.objects.filter(show=True)

class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    # queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        return Feedback.objects.filter(show=True)

class TagsAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'

class ReplysAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    lookup_field = 'pk'

class CommentsAPIView(ListCreateAPIView):
    permission_classes = [ReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

class ContactUsersAPIView(ListCreateAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer
    permission_classes = [ReadOnly]

class ContactUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer
    lookup_field = 'pk'
    permission_classes = [ReadOnly]
