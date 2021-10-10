from django.db import models
from django.contrib.auth.models import User


class Screen(models.Model):
	screen_name = models.TextField(max_length=50)
	theater = models.ForeignKey(User, on_delete=models.CASCADE)
	seating_capacity = models.IntegerField()
	entry_fee = models.IntegerField()
	#show_time = MultiSelectField(choices=TIME_CHOICES)
	def __str__(self):
		return self.screen_name

class Movie(models.Model):
	screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
	movie_name = models.TextField()
	poster_image = models.ImageField(upload_to='thumbnails/',blank=True,null=True)
	summery = models.TextField()

	def __str__(self):
		return self.movie_name

class Show(models.Model):
	screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
	theater = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	#start_date = models.DateField()
	#end_date = models.DateField()
	date = models.DateField()
	time = models.TimeField()

	


