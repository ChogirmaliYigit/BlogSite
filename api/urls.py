from django.urls import path
from .views import PostsAPIView, PostRetrieveUpdateDestroyAPIView, SocialLinksAPIView, SocialLinkRetrieveUpdateDestroyAPIView, SkillsAPIView\
, SkillRetrieveUpdateDestroyAPIView, ServicesAPIView, ServiceRetrieveUpdateDestroyAPIView, PortfoliosAPIView, PortfolioRetrieveUpdateDestroyAPIView\
, FeedbacksAPIView, FeedbackRetrieveUpdateDestroyAPIView, TagsAPIView, TagRetrieveUpdateDestroyAPIView, CommentsAPIView, CommentRetrieveUpdateDestroyAPIView\
    , ReplysAPIView, ReplyRetrieveUpdateDestroyAPIView, ContactUsersAPIView, ContactUserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PostsAPIView.as_view(), name='posts'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),
    path('socials/', SocialLinksAPIView.as_view(), name='socials'),
    path('social/<int:pk>/', SocialLinkRetrieveUpdateDestroyAPIView.as_view(), name='social_detail'),
    path('skills/', SkillsAPIView.as_view(), name='skills'),
    path('skill/<int:pk>/', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill_detail'),
    path('services/', ServicesAPIView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service_detail'),
    path('portfolioes/', PortfoliosAPIView.as_view(), name='portfolioes'),
    path('portfolio/<int:pk>/', PortfolioRetrieveUpdateDestroyAPIView.as_view(), name='portfolio_detail'),
    path('feedbacks/', FeedbacksAPIView.as_view(), name='feedbacks'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback_detail'),
    path('tags/', TagsAPIView.as_view(), name='tags'),
    path('tag/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag_detail'),
    path('comments/', CommentsAPIView.as_view(), name='comments'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment_detail'),
    path('replies/', ReplysAPIView.as_view(), name='replies'),
    path('reply/<int:pk>/', ReplyRetrieveUpdateDestroyAPIView.as_view(), name='reply_detail'),
    path('contactusers/', ContactUsersAPIView.as_view(), name='contactusers'),
    path('contactuser/<int:pk>/', ContactUserRetrieveUpdateDestroyAPIView.as_view(), name='contactuser_detail'),
]

