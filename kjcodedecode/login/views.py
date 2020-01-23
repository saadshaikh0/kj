from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from kjpage.models import Student
from django.contrib import messages

# Create your views here.
# def register(request):
#     if request.method="POST":
