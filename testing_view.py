from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Member
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# tesing view added below - this is to test your code, and the view is avaible in the template.html file
from django.http import HttpResponse, HttpResponseRedirect
def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
      'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))
https://github.com/samson-olofinsae/Dj-pro.git
