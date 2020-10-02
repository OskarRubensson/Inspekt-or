from django.shortcuts import render, redirect

# Create your views here.
def home(request, id=1):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    return render(request, 'home.html', {'user': request.user.get_username()})