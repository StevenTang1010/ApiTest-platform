from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, 'base_page.html')