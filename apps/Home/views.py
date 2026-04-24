from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def Home(request):
    context = {'name': 'John Doe'}
    # Renders the 'my_template.html' template
    return render(request, 'Home/Home.html', context)

def colcom_ai(request):
    return render(request, 'Home/colcomAI.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "auth/login.html")


def register_view(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1']
            )
            return redirect("login")
    return render(request, "auth/register.html")



def logout_view(request):
    logout(request)
    return redirect("login")