
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'dj-base.html')

def dashboard(request):
    return render(request, 'dashboard.html')
