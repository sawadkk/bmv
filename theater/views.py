from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.views import index
from .forms import *
from django.db import transaction
from accounts.models import *
from django.db import models

@login_required(login_url='signin_form')
def dashboard(request):
	#check if your in the theater group
	user = request.user
	if user.groups.filter(name='theater').exists():
		return render(request,'theater/dashboard.html',{user:'users'})
	
	messages.info(request,"permission denied")	
	return redirect('index')
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'theater/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })