from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm



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

def info(request):
  mymember = Member.objects.all().values()
  return render(request, "info.html", {"mymember":mymember})

def add_member(request):
  if request.method == "POST":
    form = MemberForm(request.POST)
    if form.is_valid():
      #firstname = form.cleaned_data["firstname"]
      #lastname = form.cleaned_data["lastname"]
      #print(f"HI, {firstname} {lastname}!")
      form.save()
      return redirect("all_members")
  return render(request, "add_member.html",{"form":MemberForm()})
