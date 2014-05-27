from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('opal/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def about(request):
    return HttpResponse("You are in the about page")

def people(request):
    return HttpResponse("You are in the people's page")
