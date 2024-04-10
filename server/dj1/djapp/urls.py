from django.urls import path
from . import views

urlpatterns = [
   path('sign_up', views.sign_up, name='sign_up'),
   path('login', views.login, name='login'),
   path('get_user', views.get_user, name='get_user'),
   path('create_post', views.create_post, name='create_post'),
]

