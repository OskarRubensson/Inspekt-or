from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    data = ""
    return render(request, 'home.html', {'user': request.user.get_short_name(), 'data': data})