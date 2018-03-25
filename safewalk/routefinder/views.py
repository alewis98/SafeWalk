from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are at the RouteFinder Homepage.")

def crime(request, crime_id):
    return HttpResponse("Crime committed at ")