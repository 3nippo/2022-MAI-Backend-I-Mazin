from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Here will be logged/unlogged page")
# Create your views here.
