from django.db import models
from django.contrib.auth.models import User
from theater.models import *

class Pending(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	seat_number = models.IntegerField() 

class Booked(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	seat_number = models.IntegerField()

class Show(models.Model):
	screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
	theater = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	#start_date = models.DateField()
	#end_date = models.DateField()
	date = models.DateField()
	time = models.TimeField()

	def __str__(self):
		return  self.screen.screen_name +" | "+ self.movie.movie_name +" | ", self.time