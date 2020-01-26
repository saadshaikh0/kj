from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from kjpage.models import Student
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        name=request.POST["Name"]
        print(username,email,password,name)
        user=User.objects.create_user(username,email,password=password,first_name=name)
        user.save()
        s=Student(user=user)
        s.save()
        return redirect("/mcq")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("mcq")
        else:
            messages.info(request,"incorrect credintials")
            return redirect("/")
    else:
        return redirect("home")

def logout(request):
    auth.logout(request)
    return redirect("/")