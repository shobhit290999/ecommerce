from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from django.views import View


def index(request):
    return render(request,"shop.html")
# Create your views here.
