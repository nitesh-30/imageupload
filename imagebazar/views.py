from http.client import HTTPResponse


from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *
def show_about_page(request):
    print("about page request")
    
    return render(request,"about.html",{})
def show_home_page(request):
   cats=categry.objects.all()
   images= image.objects.all()
   data={'images':images,'cats':cats}
   return render(request,"home.html",data)
def show_categry_page(request,cid):
  
   cats=categry.objects.all()
   categry=categry.objects.get(pk=cid)
   images= image.objects.filter(cat=categry)
   data={'images':images,'cats':cats}
   return render(request,"home.html",data)
