from django.shortcuts import render
from django.http import HttpResponseRedirect
from .froms import RegisterForm, LoginForm

# Create your views here.
def Home(request):
    return render(request, "LR_form/home.html")

def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/welcome")
    else:
        form = LoginForm()
    return render(request, "LR_form/log_in.html", {"form": form})

def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            
    else: 
        form = RegisterForm()
    return render(request, "LR_form/registration.html", {"form": form})

def welcome(request):
    return render(request, "LR_form/welcome.html")