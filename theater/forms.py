from django import forms
from accounts.models import *
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('owner_name', 'theater_name', 'address' , 'phone_number')