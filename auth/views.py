from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

class RegisterUser(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request=request, template_name='auth/register.html', context={'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return redirect('register')

class LoginUser(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name='auth/login.html', context={'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print(form.errors)
                return redirect('login')
        else:
            print(form.errors)
            return redirect('login')

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('index')
