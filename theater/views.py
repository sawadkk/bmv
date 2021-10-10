from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.views import index
from .forms import *
from django.db import transaction
from accounts.models import *
from django.db import models
from .tasks import send_mail_func,test_func
from django.urls import reverse_lazy
from django.views import generic
from .models import *

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

@login_required(login_url='signin_form')
def dashboard(request):
    user=request.user
    if user.groups.filter(name='theater').exists():
        screen = Screen.objects.filter(theater=request.user)
        return render(request,'theater/dashboard.html',{'screen':screen})
    else:
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


def add_screen(request):
    form = ScreenForm()
    if request.method == 'POST':
        print(1)
        form = ScreenForm(request.POST)
        if form.is_valid():
            screen = Screen()
            screen.screen_name = form.cleaned_data['screen_name']
            screen.theater = request.user
            screen.seating_capacity = form.cleaned_data['seating_capacity']
            screen.entry_fee = form.cleaned_data['entry_fee']
            print(screen.entry_fee)
            screen.save()
            messages.success(request,('screen added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_screen.html',{'screen_form':form})
    return render(request,'theater/add_screen.html',{'screen_form':form})

def add_movie(request):
    form = MovieForm()
    if request.method == 'POST':
        print(1)
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = Movie()
            movie.screen = form.cleaned_data['screen']
            movie.movie_name = form.cleaned_data['movie_name']
            movie.poster_image = form.cleaned_data['poster_image']
            movie.summery = form.cleaned_data['summery']
            movie.save()
            messages.success(request,('movie added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_movie.html',{'movie_form':form})
    return render(request,'theater/add_movie.html',{'movie_form':form})

def add_show(request, screen_pk):
    form = ShowForm()
    if request.method == 'POST':
        print(1)
        form = ShowForm(request.POST)
        if form.is_valid():
            show = Show()
            show.screen = Screen.objects.get(pk=screen_pk)
            show.theater = request.user
            show.movie = form.cleaned_data['movie']
            show.date = form.cleaned_data['date']
            show.time = form.cleaned_data['time']
            show.save()
            messages.success(request,('show added'))
            return redirect('dashboard')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render(request,'theater/add_show.html',{'show_form':form})
    screen = Screen.objects.filter(pk=screen_pk)
    sawad = screen_pk
    return render(request,'theater/add_show.html',{'show_form':form,'screen':screen})