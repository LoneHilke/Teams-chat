from django.shortcuts import render
from .models import Links
from django.http import HttpResponse
from django.template import loader

def index(request):
    links = Links.objects.all().values()
    template = loader.get_template('teams/base.html')
    context = {
        'links':links
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  links = Links.objects.get(id=id)
  template = loader.get_template('teams/details.html')
  context = {
    'links': links,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  
  template = loader.get_template('teams/main.html')
  
  return HttpResponse(template.render())

def fun(request):
    template = loader.get_template('teams/fun.html')
    
    return HttpResponse(template.render())

def jq(request):
  #links = Links.objects.get(id=id)
  template = loader.get_template('teams/jq.html')
  #context = {
    #'links': links,
  #}
  return HttpResponse(template.render())

def lh(request, id):
  links = Links.objects.get(id=id)
  template = loader.get_template('teams/lh.html')
  context = {
    'links': links,
  }
  return HttpResponse(template.render(context, request))



#fra: https://www.w3schools.com/django/django_add_link_details.php