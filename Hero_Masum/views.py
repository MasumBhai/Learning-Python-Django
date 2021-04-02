from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Masum Bhai is Hero</h1>")
def anything(response):
    return HttpResponse("<h1>Love You Masum 😍</h1>")
