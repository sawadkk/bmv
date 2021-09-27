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