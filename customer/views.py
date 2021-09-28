from django.shortcuts import render,redirect
from theater.models import *
from .models import *

def index(request):
	movies = Movie.objects.all()
	return render(request,'customers/index.html',{'movies':movies})

def movie_details(request, movie_pk):
	movie = Movie.objects.filter(id=movie_pk)
	show = Show.objects.filter(movie_id=movie_pk) 
	return render(request,'customers/movie_details.html',{'movie':movie,'shows':show})

def ticket_plan(request, show_pk):
	show = Show.objects.filter(id=show_pk) 
	return render(request,'customers/ticket_plan.html',{'shows':show})

def load_data(request):
	if request.method == 'POST':
		location = request.POST.get('location')
		print(location)
		date = request.POST.get('date')
		print(date)
		show_pk = request.POST.get('show_pk')
		print(show_pk)
		show = Show.objects.filter(id=show_pk,date=date)
		for i in show:
			print(i.time)
		return render(request,'customers/ticket_plan.html',{'shows':show})
	return redirect('index')