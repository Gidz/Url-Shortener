from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TinyUrl
from .utils import codegen

def index(request):
    return render(request,"shortener/index.html",{})

def short_url_redirect(request,slug):
    obj = TinyUrl.objects.get(shorturl=slug)
    return redirect(obj.url)

def shorten_url(request):
    if(request.method=='POST'):
        raw_url = request.POST['raw_url']
        TinyUrl.objects.create(
        url = raw_url,
        shorturl = codegen()
        )
        print("Tried to save it")
    return HttpResponse("URL saved")
