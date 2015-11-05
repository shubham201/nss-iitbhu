from django import forms
from django.shortcuts import render
from .models import Volunteer, UserProfile
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from django.contrib.admin import widgets
from django import forms
from django.contrib.auth.models import User

class VolunteerForm(forms.ModelForm):
	name = forms.CharField(max_length=20, help_text="Please enter the Volunteer name")
	address = forms.CharField(widget=forms.Textarea, max_length=100)
	joining_date = forms.DateField(widget=SelectDateWidget())
	contact = forms.IntegerField()
	email = forms.EmailField(widget=forms.EmailInput(), help_text='A valid email address, please.')
	working_hrs = forms.IntegerField()
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
		'''
		contact = cleaned_data.get('contact')
		t = contact
		count = 0
		while t>1:
			t = t/10
			count = count + 1
		if count == 10:
			return cleaned_data
		else:
			raise Exception
		'''

	class Meta:
		model = Volunteer
		fields = ('name', 'address', 'joining_date', 'contact', 'email', 'working_hrs')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website',)
#forms.DateField(initial=datetime.date.today)