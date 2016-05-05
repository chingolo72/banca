from django.shortcuts import render
from django.http import HttpResponse

def mainhome(request):
	return render(request,"mainhome.html",{})
	
