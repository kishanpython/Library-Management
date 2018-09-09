from django.db import models
from accounts.models import student
import datetime as dt

# Create your models here.

mdate=dt.date.today()


class Book(models.Model):
	bid = models.CharField(max_length=4,unique=True)
	bname = models.CharField(max_length=50)
	author = models.CharField(max_length=30)
	publisher = models.CharField(max_length=30)
	cost = models.IntegerField()
	desc = models.CharField(max_length=200,null=True)

class Allocate(models.Model):
	aid = models.CharField(max_length=4)
	sid = models.IntegerField()
	allodate = models.DateField(default=mdate)


	def __str__(self):
		return self.aid









