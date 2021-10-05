from django.db import models
from django.contrib.auth.models import User
from theater.models import *

class Pending(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	seat_number = models.CharField(max_length=50) 

class Booked(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	seat_number = models.CharField(max_length=50)

