from django.shortcuts import render, redirect
from .models import Links
from .forms import LinksForm
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

def jq(request, id):
  links = Links.objects.get(id=id)
  template = loader.get_template('teams/jq.html')
  context = {
    'links': links,
  }
  return HttpResponse(template.render(context, request))

def lh(request, id):
  links = Links.objects.get(id=id)
  template = loader.get_template('teams/lh.html')
  context = {
    'links': links,
  }
  return HttpResponse(template.render(context, request))

def add_link(request):
    links = Links.objects.all()
    form = LinksForm()
  
    if request.method == 'POST':
      form = LinksForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/add_link')
      
    context = {'links': links, 'form': form}
    return render(request, 'teams/add_link.html', context)

def index2(request):
    links = Links.objects.all().values()
    template = loader.get_template('teams/base2.html')
    context = {
        'links':links
    }
    return HttpResponse(template.render(context, request))

def index3(request):
    links = Links.objects.all().values()
    template = loader.get_template('teams/base3.html')
    context = {
        'links':links
    }
    return HttpResponse(template.render(context, request))




#fra: https://www.w3schools.com/django/django_add_link_details.php