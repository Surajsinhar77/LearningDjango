from django.urls import path
from . import views

urlpatterns = [
   path('userSignup', views.userSignup, name='userSignup'),
]

