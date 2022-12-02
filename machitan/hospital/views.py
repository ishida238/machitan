from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView #テンプレートタグ
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "U_logout_check.html"

'''
def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'signup.html', param)

def login_view(request):
    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect('hospital:login-success')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'login.html', param)

def logout_view(request):
    logout(request)

    return render(request, 'logout.html')

def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'user.html', params)

def other_view(request):
    users = User.objects.exclude(username=request.user.user_name)

    params = {
        'users': users
    }

    return render(request, 'other.html', params)
'''
class LoginSuccessView(generic.TemplateView):
    template_name = "login_success.html"

class U_logout_checkView(generic.TemplateView):
    template_name = 'U_logout_check.html'