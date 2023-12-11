from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


from TestApp.models import*
from TestApp.models import contact
from TestApp.models import Post
from TestApp.models import BlogComment

from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.
def  hello(request):
	msg="welcome to Django"
	return HttpResponse(msg)
def Hi(retrun):
	msg='<h1>Hello Hi django,</h1>'
	return HttpResponse(msg)
def mygoogle(request):
	return redirect("http:/www.google.com")
def welcome(request,name):
	msg="welcome dear"+name
	return HttpResponse(msg)
def index(request):
	context={'name':'nisha'}
	
	return render(request,'index.html')
def agra(request):
	return render(request,'agra.html')
def datainput(request):
	return render(request,'datainput.html')

@csrf_exempt
def datasave(request):

	a=request.POST.get('sname')
	b=request.POST.get('scity')
	c=request.POST.get('semail')
	obj=Employee(name=a,city=b,email=c)
	obj.save()
	return HttpResponse('datasaved')
def datashow(request):
	obj=Employee.objects.all()
	msg="data is <br>"
	for res in obj:
		msg=msg+res.name+'<br>'
		msg=msg+res.city+'<br>'
		msg=msg+res.email+'<br>'
	return HttpResponse(msg)
def filterdata(request):
	return render(request,'filterdata.html')
@csrf_exempt
def datafind(request):
	a=request.POST.get("sname")
	obj=Employee.objects.filter(name=a)
	msg="data is <br>"
	for res in obj:
		msg=msg+res.name+"<br>"
		msg=msg+res.city+"<br>"
		msg=msg+res.email+"<br>"
	return HttpResponse(msg)
def updatedata(request):
	return render(request,'updatedata.html')
@csrf_exempt
def datamodify(request):
	a=request.POST.get("sname")
	b=request.POST.get("scity")
	c=request.POST.get("semail")


	obj=Employee.objects.get(name=a)
	obj.city=b
	obj.email=c
	obj.save()
	return HttpResponse("data changed")
		
def removedata(request):
	return render(request,'removedata.html')


def quiz(request):
	return render(request,'quiz.html')
@csrf_exempt
def datasign(request):

	a=request.POST.get('username')
	b=request.POST.get('password')
	c=request.POST.get('confirm password')
	obj=signup(username=a,password=b,confirm_password=c)
	obj.save()
	return HttpResponse('datasaved')


#project start of bloging systtem

def bloghome(request):
	allPosts=Post.objects.all()
	context={'allPosts':allPosts}
	return render(request,'bloghome.html', context)
def blogpost(request):
	comments=BlogComment.objects.all()
	context={'comments':comments}
	
	
	return render(request,'blogpost.html',context)

def about(request):
	return render(request,'about.html')

def homepage(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def search(request):
	query=request.GET['query']
	allPosts=Post.objects.filter(title__icontains=query)
	params={'allPosts':allPosts}

	return render(request,'search.html')


def signup(request):

    if request.method == "POST":
        # Get the post parameters
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(username, email, password1)
            messages.success(request, "Account created successfully.")
           # return redirect('login')
        except IntegrityError:

            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
        	login(request, user)
        	messages.success(request,'successfully login')
        	return redirect('home')
            
           
        else:
        	messages.error(request,'invalid')
        	return HttpResponse('error')

    return render(request, 'login.html')
    



def logoutpage(request):
	logout(request)
	messages.success(request,'successfully logged out')
	return redirect("home")
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        comment=BlogComment(comment= comment, user=user)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    return HttpResponse('successfully comment')


def post(request):
	
	if request.method=='POST':
		title=request.POST['title']
		author=request.POST['author']
		timeStamp=request.POST['timeStamp']

		content=request.POST['content']
		my_data=Post(title=title,author=author,timeStamp=timeStamp  ,content=content)
		my_data.save()



	return render(request,'post_form.html')
def Contact(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		content=request.POST['content']
			
		my_data=contact(name=name,email=email,phone=phone,content=content)
		my_data.save()
	return render(request,'contact.html')
	
		


def update(request):
	if request.method=='POST':
		title=request.POST.get('title')
		author=request.POST.get('author')
		timeStamp=request.POST.get('timeStamp')

		content=request.POST.get('content')
		my_data = Post.objects.get(title=title)
		my_data.author=author
		my_data.timeStamp=timeStamp
		my_data.content=content
		my_data.save()
		messages.success(request, "Your post has been update successfully")


	
	return render(request,'postupdate.html')		
	