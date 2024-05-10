from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    context={}
    return render(request, "myApp/home.html", context)
def Login(request):
    context={}
    return render(request, "myApp/Login.html", context)
def Admin(request):
    context={}
    return render(request, "myApp/Admin.html", context)
def Menu(request):
    context={}
    return render(request, "myApp/Menu.html", context)
def Order(request):
    context={}
    return render(request, "myApp/Order.html", context)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post:list")
    form = UserCreationForm()
    return render(request, "myApp/Register.html", {"form": form })



