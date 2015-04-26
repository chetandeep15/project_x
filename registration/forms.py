from django import forms

from django.contrib.auth.models import User

class Registration_Form(forms.ModelForm):

	password=forms.CharField(widget=forms.PasswordInput())

	class Meta:

		model=User

		fields=['first_name', 'last_name', 'username', 'email', 'password']

	def clean_username(self):

		value=self.cleaned_data['username']

		if User.objects.filter(username=value[0]):

			raise ValidationError(u'The username %s is already taken' %value)

		return value