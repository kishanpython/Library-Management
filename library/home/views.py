from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_views(request):
	return render(request,'home/home.html',{'nbar': 'stu'})