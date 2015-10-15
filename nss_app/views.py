from django.shortcuts import render, redirect

# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import sqlite3
from .models import Volunteer
from .forms import  VolunteerForm, UserProfileForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

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

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'nss_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/nss/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your NSS account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'nss_app/login.html', {})

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this restricted text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/nss/')