from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import os

img_path = os.getcwd()+'/opal/static/images/slideshow/'
images = ['images/slideshow/'+img_name for img_name in os.listdir(img_path)]

# Create your views here.
def index(request):
    template = loader.get_template('opal/index.html')
    context = RequestContext(request, {
        'img_indexes': range(1, len(images)),
        'img_paths': images,
    })
    return HttpResponse(template.render(context))
