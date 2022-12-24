from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dev3(request):
    return HttpResponse('django')
def dev4(request):
    return HttpResponse('sql')