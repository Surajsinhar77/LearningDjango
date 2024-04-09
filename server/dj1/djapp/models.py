from django.db import models

# Create your models here.
#creating a model for user which have email, password ,name , postRefrence

class Users(models.Model):
    email = models.EmailField(max_length=100)  
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name='user_posts')
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts') 
    # this is for user post refrence related_name is used to get the post of user
