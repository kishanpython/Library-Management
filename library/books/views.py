from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse

# Create your views here.

from .forms import BookForm
from .models import Book,Allocate
from accounts.models import student 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from collections import defaultdict



def book(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect(reverse('book:show'))
			except:
				pass
		else:
			return render(request,"books/index.html",{'msg':'Books id already register'})
	else:
		return render(request,'books/index.html')

def show(request):
	book = Book.objects.all()
	if len(book)==0:
		return HttpResponse("<center><h1>NO DATA TO SHOW</h1></center>")
	else:
		if request.user.is_active:
			return render(request,'books/show.html',{'book':book})
		else:
			return render(request,'books/show1.html',{'book':book})

def edit(request,id=None):
	book = Book.objects.get(id=id)
	return render(request,'books/edit.html',{'book':book})

def update(request,id=None):
	book = Book.objects.get(id=id)
	form = BookForm(request.POST,instance=book)
	if form.is_valid():
		form.save()
		return redirect("/bk/show/")
	return render(request,'book/edit.html',{'book':book})

def delete(request,id=None):
	book = Book.objects.get(id=id)
	book.delete()
	return redirect('/bk/show/')


def search_book(request):
	if request.method=="POST":
		bid = request.POST['bookid']		
		if len(Book.objects.filter(bid=bid)):
			context={
				'bk':Book.objects.get(bid=bid),
			}
			return render(request,'books/bookdet.html',context)
		else:
			return render(request,'books/bksrh.html',{'msg':'WRONG BOOK ID'})
	else:
		return render(request,'books/bksrh.html')



def allocate_book(request):
	if request.method == "POST":
		sid =  request.POST['studentid']
		bkid = request.POST['bkid']

		check_id = Book.objects.filter(bid=bkid)
		if len(check_id)==0:
			return render(request,'books/allocate.html',{'msg':'Book ID is incorrect'})
		s = student.objects.filter(studentid=sid)
		if  len(s)==0:
			return render(request,'books/allocate.html',{'msg':'Student ID is incorrect'})
		l=[]
		for i in Allocate.objects.all():
			a=i.sid	
			if a==int(sid):
				if i.aid==bkid:
					return render(request,'books/allocate.html',{'msg':'Book Already Allocated'})
				else:
					pass				
			else:
				pass
		allo = Allocate(
			aid=bkid,
			sid=sid,
			)
		allo.save()
		return render(request,'books/allocate.html',{'msg':'Book is Succesfully Allocated'})
	else:
		return render(request,'books/allocate.html')



def search(request):
	if request.method == "POST":
		stu = request.POST['sid']
		request.session['sid'] = stu
		if not student.objects.filter(studentid=stu):
			return render(request,'account/studentlogin.html',{'msg':'Wrong Student ID'})	
		else:
			return redirect (reverse('book:details'))
	else:
		return render(request,'account/studentlogin.html')			

def stu_search(request):
	if request.method == "POST":
		stu = request.POST['sid']
		request.session['sid'] = stu
		if not student.objects.filter(studentid=stu):
			return render(request,'account/stlogin.html',{'msg':'Wrong Student ID'})	
		else:
			return redirect (reverse('book:details'))
	else:
		return render(request,'account/stlogin.html')



def details(request):
		stu=request.session.get('sid')
		l=[]
		t=[]
		x=Allocate.objects.all()
		stu=int(stu)
		for i in x:
			a=i.sid
			if int(a)==stu:
				l.append(i.aid)
				t.append(i.allodate)
			else:
				pass
		a=[]
		for i in l:
			x=Book.objects.get(bid=i)
			a.append(x)
		dit={}
		dit = dict(zip(a,t))				
		context={
			'stu':student.objects.get(studentid=stu),
			'dit':dit,
			'length':len(l),
		}
		if request.user.is_active:
			return render(request,'account/studentdetails.html',context)
		else:	
			return render(request,'books/student.html',context)




def deallocate_views(request,id=None,proid=None):
		x=Allocate.objects.filter(sid=proid)
		try:
			t=x.filter(aid=id)
			t.delete()
		except:
			pass
		finally:
			request.session['sid'] = proid
			return redirect(reverse('book:details'))

			