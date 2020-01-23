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
        return redirect("/")