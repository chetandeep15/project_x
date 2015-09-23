from django.shortcuts import render, redirect

# Create your views here.

from logins.forms import Login_Form

from django.contrib.auth import authenticate, login, logout

#import pdb

from django.contrib.auth.models import User

def login_user(request):
	#pdb.set_trace()
	if request.method=="POST":

		form=Login_Form(request.POST)

		if form.is_valid():

			uname=form.cleaned_data['uname']

			upass=form.cleaned_data['upass']

			u=authenticate(username=uname, password=upass)

			if u is not None:

				if u.is_active :

					login(request, u)

					return redirect("/home")

				else :

					return redirect("/")
			else :
				return redirect("/")

	else:

		form=Login_Form()

		return render(request,'login.html',{'form':form})


def logout_user(request):

	logout(request)

	return render(request,'logout.html')