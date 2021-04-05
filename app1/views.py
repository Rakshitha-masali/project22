from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is direct html code</h1>")

def hello(request):
    return render(request,"sample1.html")

def sample_app1(request):
    return render(request,"sample_app1.html")
