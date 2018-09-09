from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Admin_prof
from django.core.urlresolvers import reverse
from .models import student
from django.core.mail import send_mail  
#from events.models import Participant
from django.contrib.auth.decorators import login_required
from books.views import allocate_book
from books.models import Book
from django.contrib.auth import ( 
   authenticate,
   login,
   logout,
	
	)
# Create your views here.

@login_required
def register_views(request):

	if request.method=="POST":

		firstname=request.POST['fname']
		lastname=request.POST['lname']
		username=request.POST['username']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		mobno=request.POST['mobno']
		email=request.POST['email']

########...... 	validations   .....########
		
		t=User.objects.filter(username=username)
		if len(t):
			return render(request,'account/register.html',{'msg':'Username already register'})

		e=User.objects.filter(email=email)
		if len(e):
			return render(request,'account/register.html',{'msg':'Email already register'})

		if len(mobno)!=10:
			return render(request,'account/register.html',{'msg':'Enter correct mobile number'})	

		m=Admin_prof.objects.filter(mobno=mobno)
		if len(m):
			return render(request,'account/register.html',{'msg':'Mobile number already register'})

		
		if password!=cpassword:
			return render(request,'account/register.html',{'msg':'Password and Confirm Password must be same'})


#######....... CREATING USER OBJECT ......#############
		user,create = User.objects.get_or_create(

				first_name=firstname,
				last_name=lastname,
				username=username,
				email=email,


		)

		user.set_password(password)
		user.save()

		pro=Admin_prof(user=user, mobno=mobno)
		pro.save()

		return HttpResponseRedirect(reverse('home:home'))

	else:
		return render(request,'account/register.html')


def student_views(request):

	if request.method=="POST":

		firstname=request.POST['fname']
		lastname=request.POST['lname']
		mobno=request.POST['mobno']
		email=request.POST['email']
		rollno=request.POST['rollno']
		studentid=request.POST['id']

########...... 	validations   .....########
		

		if len(mobno)!=10:
			return render(request,'account/studentreg.html',{'msg':'Enter correct mobile number'})	
		s=student.objects.filter(email=email)
		if len(s):
			return render(request,'account/studentreg.html',{'msg':'Email already register'})
		r=student.objects.filter(rollno=rollno)
		if len(r):
			return render(request,'account/studentreg.html',{'msg':'Roll number already register'})


#######....... CREATING USER OBJECT ......#############

		pro=student(firstname=firstname,lastname=lastname,mobno=mobno,email=email,rollno=rollno,studentid=studentid)
		pro.save()

#########....... EMAIL SENDING  .........#############

		subject = "𝓚𝓚𝓛𝓘𝓑𝓡𝓐𝓡𝓨"  
		msg     = "YOUR STUDENT ID FOR LIBRARY IS " + studentid 
		to      = [email] 
		res     = send_mail(subject, msg, settings.EMAIL_HOST_USER,to,fail_silently=True)  
		if res==1:
			return HttpResponseRedirect(reverse('home:home'))
		else:
			return render(request,'account/studentreg.html',{'msg':'Message not send'})			
	else:
		return render(request,'account/studentreg.html')		


def login_view(request):
	if request.method=="POST":

		username=request.POST['username']
		password=request.POST['password']

		try:
			user=authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				return HttpResponseRedirect(reverse('home:home'))

			else:
				return render(request,'account/login.html',{'msg':'Wrong username or password'})
		except:
			return render(request,'account/login.html',{'msg':'Error in login'})

	else:
		return render(request,'account/login.html')

	
@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('accounts:login'))


				
				
