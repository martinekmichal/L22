from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member



def members_old(request):
    return HttpResponse("Hello world!")

def members_old2(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def members(request):
  template = loader.get_template('index.html')
  return render(request, "index.html")

def all_members(request):
  mymembers = Member.objects.all().values()
  context = {
    'mymem': mymembers,
  }
  return render(request, "all_members.html", context)

def details(request, id):
  mymember = Member.objects.get(id=id)
  return render(request, "detail.html", {"mymember":mymember})