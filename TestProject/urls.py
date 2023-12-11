"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from TestApp.views import *
from TestApp import views






urlpatterns = [


    path("admin/", admin.site.urls),
    
    path('TestApp/', include('TestApp.urls')),


    




    path('hello/',hello),
    path('Hi/',Hi),
    path('mygoogle/',mygoogle),
    path('welcome/<str:name>',welcome),
    path('index/',index),
    path('agra/',agra),
    path('datainput/',datainput),
    path('datasave/',datasave),
    path('datashow/',datashow),
    path('filterdata/',filterdata),
    path('datafind/',datafind),
    path('updatedata/',updatedata),
    path('datamodify/',datamodify),
    path('removedata/',removedata),
    
    path('datasign/',datasign),
    path('login/',views.loginpage,name='login'),
    
   # project start of blog 
    path('bloghome/',bloghome),
    

    path('blogpost/',blogpost),
       # path('/<str:slug>', views.blogpost, name='blogpost'),
    path('signup/',signup),

    path('home/',views.homepage,name='home'),
    path('about/',about),
    path('contact/',views.Contact,name='contact'),
    path('search/',search),
    path('logout/',views.logoutpage,name='logout'),
    path('post_form/',views.post,name='post_form'),
    path('postupdate/',views.update,name='postupdate'),
    path('postComment', views.postComment, name="postComment")




       

       








   
   


    
]

