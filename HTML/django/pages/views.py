from django.shortcuts import render
from django.http import HttpResponse
def homepageview(request):
	return HttpResponse("Welcome to my first webpage ")
# Create your views here.
