from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Admin, SocialLink, Portfolio, Feedback, ContactUser, Post
from .forms import ContactUserForm, CommentForm, ReplyForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexPage(View):
    def get(self, request):
        user = Admin.objects.get(email='chogirmali.yigit@gmail.com')
        skills = user.skills.all()
        services = user.services.all()
        portfolios = user.portfolios.all()
        feedbacks = Feedback.objects.filter(show=True)
        posts = user.posts.all()[:9]
        socials = user.socials.all()
        return render(
            request=request,
            template_name='blog/index.html',
            context={
                'user': user,
                'skills': skills,
                'services': services,
                'portfolios': portfolios,
                'feedbacks': feedbacks,
                'posts': posts,
                'socials': socials,
            }
        )

    def post(self, request):
        form = ContactUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Your message has been sent. Thank you!')
            return redirect('index')
        return redirect('index')

class PortfolioDetailPage(View):
    def get(self, request, portfolio_id):
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)
        return render(request=request, template_name='blog/portfolio-details.html', context={'portfolio': portfolio})

    def post(self, request):
        pass

class PostDetailPage(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all()
        posts = Post.objects.all().order_by('-id')[:10]
        return render(request=request, template_name='blog/blog-single.html', context={'post': post, 'comments': comments, 'posts': posts})

    def post(self, request, post_id):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Your Comment successfully added!')
            return redirect('post', post_id)
        form_reply = ReplyForm(request.POST, request.FILES)
        print(form_reply.errors)
        if form_reply.is_valid():
            form_reply.save()
            messages.success(request=request, message='Your Reply successfully added!')
            return redirect('post', post_id)
        return redirect('post', post_id)

class ProfilePage(View):
    def get(self, request):
        user = Admin.objects.get(email='chogirmali.yigit@gmail.com')
        skills = user.skills.all()
        socials = user.socials.all()
        feedbacks = Feedback.objects.filter(show=True)
        return render(
            request=request,
            template_name='blog/profile.html',
            context={
                'user': user,
                'socials': socials,
                'skills': skills,
                'feedbacks': feedbacks,
            }
        )

    def post(self, request):
        pass

class AllPostsView(View):
    def get(self, request):
        user = Admin.objects.get(email='chogirmali.yigit@gmail.com')
        posts = Post.objects.all().order_by('-id')
        recent_posts = Post.objects.all().order_by('-id')[:3]
        socials = user.socials.all()
        paginator = Paginator(posts, 6)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(
            request=request,
            template_name='blog/all-posts.html',
            context={
                'posts': posts,
                'recent_posts': recent_posts,
                'socials': socials,
                'user': user,
            }
        )

    def post(self, request):
        pass
