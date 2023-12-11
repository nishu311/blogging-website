from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.urls import reverse



# Create your models here.
class Employee(models.Model):
	name=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	class Meta:
		db_table='Employee'






# blog project start
class contact(models.Model):
	sno=models.CharField(max_length=30)
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phone=models.CharField(max_length=12)
	content=models.TextField(max_length=100)
	timeStamp=models.DateTimeField(auto_now_add=True,blank=True)


	#blog post
class Post(models.Model):
	sno=models.CharField(max_length=30)
	title=models.CharField(max_length=255)
	content=models.TextField()
	author=models.CharField(max_length=12)
	
	timeStamp=models.DateTimeField(blank=True)
	def __str__(self):
		return 'message from'+self.title +'by' + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
   
    timestamp= models.DateTimeField(default=now)














 
    
