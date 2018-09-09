from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin_prof(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	mobno=models.CharField(max_length=10)


	def __str__(self):
		return self.mobno

class student(models.Model):
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	mobno=models.CharField(max_length=15)
	email=models.EmailField()
	rollno=models.CharField(max_length=10)
	studentid=models.CharField(max_length=10)
	

	def __str__(self):
		return self.firstname


		