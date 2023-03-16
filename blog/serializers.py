from rest_framework import serializers
from .models import Post, SocialLink, Skill, Service, Portfolio, Feedback, Tag, Comment, Reply, ContactUser, Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        read_only_fields = ('id', )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id', )

class PostSerializer(serializers.ModelSerializer):
    author = AdminSerializer()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'author', 'tags')

class SocialLinkSerializer(serializers.ModelSerializer):
    user = AdminSerializer()

    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = ('id', )

class SkillSerializer(serializers.ModelSerializer):
    user = AdminSerializer()

    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ('id', )

class ServiceSerializer(serializers.ModelSerializer):
    user = AdminSerializer()

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('id', )

class PortfolioSerializer(serializers.ModelSerializer):
    user = AdminSerializer()

    class Meta:
        model = Portfolio
        fields = '__all__'
        read_only_fields = ('id', )

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('id', )

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', )

class ReplySerializer(serializers.ModelSerializer):
    comment = CommentSerializer()

    class Meta:
        model = Reply
        fields = '__all__'
        read_only_fields = ('id', )

class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUser
        fields = '__all__'
        read_only_fields = ('id', )