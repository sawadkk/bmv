from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
               path('dashboard',views.dashboard,name="dashboard"),
               path('update_profile',views.update_profile,name = 'update_profile'),
               path('add_screen',views.add_screen,name = 'add_screen'),
               path('add_movie',views.add_movie,name = 'add_movie'),
               url(r'^add_show(?P<screen_pk>\d+)',views.add_show,name='add_show'),
               path('test',views.test,name = 'test'),
               path('send_mail_to_all',views.send_mail_to_all,name = 'send_mail_to_all'),

               ]

