from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members_old(request):
    return HttpResponse("Hello world!")

def members_old2(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def members(request):
  template = loader.get_template('index.html')
  return render(request, "index.html")