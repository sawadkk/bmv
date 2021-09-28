from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
               path('',views.index,name="index"),
               url(r'^movie_details(?P<movie_pk>\d+)',views.movie_details,name='movie_details'),
               url(r'^ticket_plan(?P<show_pk>\d+)',views.ticket_plan,name='ticket_plan'),
               path('load_data',views.load_data,name="load_data"),
               ]

