from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def display(request):
    msg='<h1>Hello..Welcome to Django project1 Deployment.</h1>'
    return HttpResponse(msg)

