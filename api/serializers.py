from rest_framework import serializers
from blog.models import Post, SocialLink, Skill, Service, Portfolio, Feedback, Tag, Comment, Reply, ContactUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'author', 'tags')

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = ('id', )

