from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TinyUrl

def index(request):
    return render(request,"shortener/index.html",{})

def short_url_redirect(request,slug):
    obj = TinyUrl.objects.get(shorturl=slug)
    return redirect(obj.url)
