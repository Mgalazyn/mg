from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def project(request):
    context = {}
    return render(request, 'main.html', context)