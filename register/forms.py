from django import forms

from django.contrib.auth.models import User

class Registration_Form(forms.ModelForm):

	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	class Meta:

		model=User

		fields=['first_name', 'last_name', 'username', 'email', 'password']
		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'text','placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'text','placeholder': 'LastName'}),
            'username' :forms.TextInput(attrs={'class': 'text','placeholder': 'Username'}),
            'email':forms.TextInput(attrs={'class':'text','placeholder': 'Email'}),
        }

	def clean_username(self):

		value=self.cleaned_data['username']

		if User.objects.filter(username=value[0]):

			raise ValidationError(u'The username %s is already taken' %value)

		return value