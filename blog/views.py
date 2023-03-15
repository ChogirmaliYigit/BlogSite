from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Admin, SocialLink, Portfolio, Feedback, ContactUser, Post
from .forms import ContactUserForm, CommentForm, ReplyForm, FeedbackForm, LoginForm
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .generate_pin import generate

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
            messages.success(request=request, message='Your Message has been sent. Thank you!')
            return redirect('index')
        
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Your Feedback has been sent. Thank you!')
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

class LoginAdmin(View):
    def get(self, request):
        form = LoginForm()
        user = Admin.objects.first()
        subject = "Login to Cho'girmali Blog as Admin"
        email_template_name = 'auth/pin-for-admin-email.txt'
        global data
        data = {
            'email': user.email,
            'user': user,
            'pin': generate()
        }
        message = render_to_string(email_template_name, data)
        try:
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request=request, template_name='auth/login.html', context={'form': form, 'data': data})

    def post(self, request):
        pin = data.get('pin')
        if pin == int(request.POST.get('pin')):
            return redirect('index')
        else:
            return redirect('login_admin')
