from django.shortcuts import render,redirect
from theater.models import *
from .models import *
from datetime import date
from django.contrib import messages

global today 
today = date.today()

def index(request):
	movies = Movie.objects.all()
	return render(request,'customers/index.html',{'movies':movies})

def movie_details(request, movie_pk):
	movie = Movie.objects.filter(id=movie_pk)
	return render(request,'customers/movie_details.html',{'movie':movie})

def ticket_plan(request, movie_pk):
	print('sawad')
	movie = Movie.objects.filter(id=movie_pk)
	show = Show.objects.filter(date=today,movie__in=movie)
	show2 = Show.objects.filter(movie__in=movie)
	print(show)
	dates = []
	for i in show2:
		date = str(i.date)
		dates.append(date)
	print(dates)
	
	return render(request,'customers/ticket_plan.html',{'shows':show,'movie':movie,'dates':dates})
def load_data(request):
	if request.method == 'POST':
		location = request.POST['location']
		date2 = request.POST['date']
		print(date2)
		movie_pk = request.POST['pk']
		#print(movie_pk)
		movie = Movie.objects.filter(id=movie_pk)
		#print(movie)
		show = Show.objects.filter(date=date2,movie__in=movie)
		show2 = Show.objects.filter(movie__in=movie)
		dates = []
		for i in show2:
			date = str(i.date)
			dates.append(date)
		print(dates)
		return render(request,'customers/load_data.html',{'shows':show,'movie':movie,'dates':dates})
	return redirect(index)

def seat_plan(request, show_pk):
	show = Show.objects.filter(id=show_pk)
	max_seat = 0
	for seat in show:
		max_seat = (seat.screen.seating_capacity)
	my_lst = []
	book_lst = []
	#max_seat2 = int(max_seat/10)
	for i in range(1,max_seat+1):
		my_lst.append(i)
		if Booking.objects.filter(show=show_pk,seat_number=i).exists():
			book_lst.append(i)
	print(book_lst)
	return render(request,'customers/seat_plan.html',{'shows':show,'seat':my_lst,'book':book_lst})

def booking(request):
	if request.method == 'POST':
		seats = request.POST['seats']
		show_id = request.POST['show_id']
		show = Show.objects.get(id=show_id)
		seat = seats.split(",")
		length = len(seat)
		for a in range(length):
			f = seat[a]
			print(f)
			pending  = Booking.objects.create(user=request.user,show=show,seat_number=f,status='Pending')
		return redirect('index') 
	return redirect('index')