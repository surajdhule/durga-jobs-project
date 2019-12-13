from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s = "<h1>Hello suraj finally started Django . keep going suraj don't stop now </h1>"
    return HttpResponse(s)