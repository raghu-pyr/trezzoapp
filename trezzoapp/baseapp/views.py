from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def ml(request):
    return render(request, "mlpage.html") 