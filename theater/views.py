from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin_form')
def dashboard(request):
	#check if your in the theater group
	user = request.user
	if user.groups.filter(name='theater').exists():
		return render(request,'theater/dashboard.html')
	
	messages.info(request,"permission denied")	
	return redirect('index')

