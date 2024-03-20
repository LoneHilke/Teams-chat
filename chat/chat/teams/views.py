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



#fra: https://www.w3schools.com/django/django_add_link_details.php