from django import forms

from django.contrib.auth.models import User

class Login_Form(forms.Form):

	uname=forms.CharField(label="Enter your username ")

	upass=forms.CharField(widget=forms.PasswordInput(),label="Enter your password ")
