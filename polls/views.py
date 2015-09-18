from django.shortcuts import render, redirect

# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import sqlite3
from .models import Volunteer, VolunteerForm


def index(request):
	if request.method == 'POST':
		form = VolunteerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = VolunteerForm()
		title = 'Welcome to National Service Scheme'
		return render(request,'polls/index.html',{'title':title, 'form':form})

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
			return render(request, 'polls/show.html',content)
	content = {
		'title':title, 'error':errors
	}
	return render(request, 'polls/result.html',)

def thank(request):
	return render(request, 'polls/input.html')