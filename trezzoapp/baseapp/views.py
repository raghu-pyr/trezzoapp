from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def ml(request):
    return render(request, "mlpage.html") 