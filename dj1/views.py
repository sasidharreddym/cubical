from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def lucifer(request):
    return HttpResponse('<marquee><h1>lucifer is an angel who became a devil</h1><marquee>')

def hellboy(request):
    return HttpResponse('<marquee><h1>it was a good movie and it has 2 parts</h1><marquee>')

def jspiders(request):
    return HttpResponse("<marquee><h1>python was teaching by Santosh sir,Harshad sir,Rakesh sir</h1><marquee>'")