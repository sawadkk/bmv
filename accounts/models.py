from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theater_name = models.CharField(max_length = 50)
    address = models.TextField(max_length=500, blank=True) 
    owner_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = "%y/%m/%d/images")
    location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
