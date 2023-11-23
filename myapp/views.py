from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse("<h1>This is my first Django</h1>")

# def second(request):
#     return HttpResponse("<h1>This secon page of My project</h1>")


def index(request):
    return render(request,"1.html")

def second(request):
    return render(request,"2.html")