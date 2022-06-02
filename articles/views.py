from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dinner(request):
    return render(request, 'dinner.html')