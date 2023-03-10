from django.shortcuts import render
from .models import  Team, Place
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
import json

# Create your views here.


def home(request):
    obj = Team.objects.all()
    obj1 = Place.objects.all()
    return render(request, 'index.html', {'result':obj,'results':obj1})

#
# def submit(request):
#     return render(request,"submit.html")
