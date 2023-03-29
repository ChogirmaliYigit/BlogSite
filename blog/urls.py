from django.urls import path
from .views import IndexPage, PortfolioDetailPage, PostDetailPage, AllPostsView, LoginAdmin

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('portfolio/<int:portfolio_id>/', PortfolioDetailPage.as_view(), name='portfolio'),
    path('post/<int:post_id>/', PostDetailPage.as_view(), name='post'),
    # path('profile/', ProfilePage.as_view(), name='profile'),
    path('posts/', AllPostsView.as_view(), name='all_posts'),
    path('login/admin/', LoginAdmin.as_view(), name='login_admin'),
]
