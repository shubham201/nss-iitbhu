from django import forms
from django.shortcuts import render
from .models import Volunteer, Village, Camp, Family, Fund, UserProfile
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from static.py.widgets import SelectTimeWidget

class VolunteerForm(forms.ModelForm):
	name = forms.CharField(max_length=20, help_text="Enter Name")
	address = forms.CharField(widget=forms.Textarea, max_length=100, help_text="Enter Address")
	joining_date = forms.DateField(widget=SelectDateWidget(), help_text="Enter Date")
	contact = forms.IntegerField(help_text="Enter Contact")
	email = forms.EmailField(widget=forms.EmailInput(), help_text='Enter Email')
	#working_hrs = forms.IntegerField(help_text='Enter Working Hrs')
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		"""
		contact = self.cleaned_data.get('contact')
		if (int(contact) < 1) or (not len(str(contact)) == 10):
			raise forms.ValidationError("Enter Valid 10 digit Contact No.")
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		#domain, extension1, extension2  = provider.split('.')
		#if not (extension1 == "ac" and extension2 == "in"):
		if not (provider == "gmail.com" or provider == "iitbhu.ac.in" or provider =="itbhu.ac.in"):
			raise forms.ValidationError("Enter a Valid email address")
		"""
		return cleaned_data

	class Meta:
		model = Volunteer
		fields = ('name', 'address', 'joining_date', 'contact', 'email')

class VillageForm(forms.ModelForm):
	name = forms.CharField(max_length=20, help_text="Enter Name")
	adoption_date = forms.DateField(widget=SelectDateWidget(), help_text="Enter Date")
	family_count = forms.IntegerField(help_text="Enter Family Count")
	block = forms.CharField(max_length=30, help_text='Enter Email')
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data

	class Meta:
		model = Village
		fields = ('name', 'adoption_date', 'family_count', 'block')

class CampForm(forms.ModelForm):
	#village = forms.ForeignKey(Village)
	camp_type = forms.CharField(max_length=20, help_text="Camp Type Name") #required
	date = forms.DateField(widget=SelectDateWidget(), help_text="Enter Date") #required
	strt_time = forms.TimeField(widget=SelectTimeWidget(), help_text="Enter Start Time")
	end_time = forms.TimeField(widget=SelectTimeWidget(), help_text="Enter End Time")
	organising_cost = forms.IntegerField(help_text="Enter Cost to Camp")
	#details = forms.TextField(widget=forms.Textarea, max_length=200, help_text="Details")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		village = self.cleaned_data.get("village")
		return cleaned_data

	class Meta:
		model = Camp
		fields = ('village', 'camp_type', 'date', 'strt_time', 'end_time', 'organising_cost', 'details')

class FamilyForm(forms.ModelForm):
	head_name = forms.CharField(max_length=20, help_text="Head Name")
	#father_name = forms.CharField(max_length=20, help_text="Father Name")
	address = forms.CharField(widget=forms.Textarea, max_length=100, help_text="Address")
	income = forms.IntegerField(help_text="Income")
	members_count = forms.IntegerField(help_text="Members Count")
	#prob_list = forms.TextField(widget=forms.Textarea, max_length=200, help_text="Problems Faces")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		#prob_list = self.cleaned_data.get("prob_list")
		return cleaned_data
		
	class Meta:
		model = Family
		fields = ('head_name', 'address', 'income', 'members_count', 'prob_list')

class FundForm(forms.ModelForm):
	source = forms.CharField(max_length=30,help_text="Source Name")
	receiving_date = forms.DateField(widget=SelectDateWidget(), help_text="Receiving Date")
	amount = forms.IntegerField(help_text="Amount Recieved")
	#net_bal = forms.IntegerField(help_text="Net Balance")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
		
	class Meta:
		model = Fund
		fields = ('source', 'receiving_date', 'amount')



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