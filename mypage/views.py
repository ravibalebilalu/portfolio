from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def my_view(request):
    template = loader.get_template("my_view.html")
    return HttpResponse(template.render())
 
