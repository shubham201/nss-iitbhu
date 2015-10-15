from django import forms
import sqlite3
from .models import Volunteer
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from django.contrib.admin import widgets

class VolunteerForm(forms.ModelForm):
	name = forms.CharField(max_length=20, help_text="Please enter the Volunteer name")
	address = forms.CharField(widget=forms.Textarea, max_length=100)
	joining_date = forms.DateField(widget=SelectDateWidget())
	contact = forms.IntegerField()
	email = forms.EmailField(widget=forms.EmailInput(), help_text='A valid email address, please.')
	working_hrs = forms.IntegerField()
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Volunteer
		fields = ('name', 'address', 'joining_date', 'contact', 'email', 'working_hrs')

