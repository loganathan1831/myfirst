from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dev1(request):
    return HttpResponse('<h1>LOGANATHAN IS A FULLSTACK DEVELOPER</h1>')
def dev2(request):
    return HttpResponse('python')