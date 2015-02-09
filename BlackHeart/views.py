__author__ = 'harshit'
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def home(request):
    if request.path == '/' or request.path == '/home/':
        return render(request, 'home.html')
def features(request):
    if request.path == '/Features/':
        return render(request, 'features.html')
