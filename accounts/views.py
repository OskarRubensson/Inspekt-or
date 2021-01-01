from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return redirect('/')
def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'registration/sign_up.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('/login')