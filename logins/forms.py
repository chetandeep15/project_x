from django import forms

from django.contrib.auth.models import User

class Login_Form(forms.Form):

	uname=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'text','class':' user','placeholder': 'Username'}))

	upass=forms.CharField(widget=forms.PasswordInput(attrs={'class':'lock','placeholder': 'Password'}),label="Password ",)
