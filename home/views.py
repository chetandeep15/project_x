from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.

def index(request):
	
	return render(request,'index.html')



@login_required(login_url='/login')

def homepage(request):
	user=request.user
	return render(request,'homepage.html',{'user':user})


@login_required(login_url='/login')

def company(request,comp_name):
	page=comp_name+'.html'
	return render (request,page)