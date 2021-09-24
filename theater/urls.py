from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
               path('dashboard',views.dashboard,name="dashboard"),
               path('update_profile',views.update_profile,name = 'update_profile'),

               ]

