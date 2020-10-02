from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return redirect('/')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def log_out(request):
    logout(request)
    return redirect('/accounts/login')