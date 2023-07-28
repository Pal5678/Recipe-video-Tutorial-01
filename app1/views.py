from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def htmlexample(request):
    template=loader.get_template('file1.html')
    return HttpResponse(template.render())
def s3(request) :
    template = loader.get_template('s3.html')
    return HttpResponse(template.render())