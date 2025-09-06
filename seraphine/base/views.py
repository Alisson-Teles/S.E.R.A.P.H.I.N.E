from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def chat(request):
    return render(request, 'chat.html')