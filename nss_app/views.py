from django.shortcuts import render, redirect

# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import sqlite3
from .models import Volunteer
from .forms import  VolunteerForm

def index(request):
	volunteer_list = Volunteer.objects.order_by('name')[:5]
	context_dict = {
		'volunteers' : volunteer_list,
	}
	return render(request, 'nss_app/index.html', context_dict)

def add_volunteer(request):
	if request.method == 'POST':
		form = VolunteerForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			form.errors

	else:
		form = VolunteerForm()
		return render(request,'nss_app/add_volunteer.html',{'form':form})


def about(request):
	return render(request, 'nss_app/about.html')


def result(request):
	title = 'Welcome to National Service Scheme'
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		else:
			objs = Volunteer.objects.filter(name__icontains=q)
			content = {
				'title':title,
				'objs':objs,
				'query':q
			}
			return render(request, 'nss_app/show.html',content)
	content = {
		'title':title, 'error':errors
	}
	return render(request, 'nss_app/result.html',)


def thank(request):
	return render(request, 'nss_app/input.html')


def volunteer(request, volunteer_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
	    # If we can't, the .get() method raises a DoesNotExist exception.
	    # So the .get() method returns one model instance or raises an exception.
		volunteer = Volunteer.objects.get(slug=volunteer_name_slug)
		context_dict['volunteer_name'] = volunteer.name
		context_dict['volunteer'] = volunteer
	except Volunteer.DoesNotExist:
		# We get here if we didn't find the specified category.
		#  Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'nss_app/volunteer.html', context_dict)


def village(request, village_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
	    # If we can't, the .get() method raises a DoesNotExist exception.
	    # So the .get() method returns one model instance or raises an exception.
		village = Village.objects.get(slug=village_name_slug)
		context_dict['village_name'] = village.name
		context_dict['village'] = village
	except Village.DoesNotExist:
		# We get here if we didn't find the specified category.
		#  Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'nss_app/village.html', context_dict)

def camp(request, camp_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
	    # If we can't, the .get() method raises a DoesNotExist exception.
	    # So the .get() method returns one model instance or raises an exception.
		camp = Camp.objects.get(slug=camp_name_slug)
		context_dict['camp_name'] = camp.name
		context_dict['camp'] = camp
	except Camp.DoesNotExist:
		# We get here if we didn't find the specified category.
		#  Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'nss_app/camp.html', context_dict)

def family(request, family_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
	    # If we can't, the .get() method raises a DoesNotExist exception.
	    # So the .get() method returns one model instance or raises an exception.
		family = Famliy.objects.get(slug=family_name_slug)
		context_dict['family_name'] = family.name
		context_dict['family'] = family
	except Family.DoesNotExist:
		# We get here if we didn't find the specified category.
		#  Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'nss_app/family.html', context_dict)

def fund(request, fund_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
	    # If we can't, the .get() method raises a DoesNotExist exception.
	    # So the .get() method returns one model instance or raises an exception.
		fund = Fund.objects.get(slug=fund_name_slug)
		context_dict['fund_name'] = fund.name
		context_dict['fund'] = fund
	except Fund.DoesNotExist:
		# We get here if we didn't find the specified category.
		#  Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'nss_app/fund.html', context_dict)

