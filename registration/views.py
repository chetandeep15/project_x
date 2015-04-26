from django.shortcuts import render

from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.models import User

from registration.forms import Registration_Form

def register(request):

	if request.method=="POST":

		form=Registration_Form(request.POST)

		if form.is_valid():

			unm=form.cleaned_data['username']

			pss=form.cleaned_data['password']

			fnm=form.cleaned_data['first_name']

			lnm=form.cleaned_data['last_name']

			eml=form.cleaned_data['email']

			u=User.objects.create_user(username=unm, password=pss, email=eml, first_name=fnm, last_name=lnm)

			u.save()

			return render(request,'success_register.html',{'u':u})

	else:

		form=Registration_Form()

	return render(request,'register_user.html',{'form':form})