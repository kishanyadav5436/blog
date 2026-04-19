from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    "name":"Kishan_kuamr",
    "title":"first_blog",
    "content":"myfirst blog",
    "date_posted":"20th may"    
     
},
      {
    "name":"Kirsana_kuamr",
    "title":"first_blog",
    "content":"myfirst blog",
    "date_posted":"29th may"    
     
}]


# Create your views here.
def Home(request):
  context={
    'posts':posts
  }
  return render(request, 'myapp/home.html',context)
def about(request):
  return render (request, "about.html")
def M(request):
  return render(request,"M.html")

def register(request):
  return HttpResponse("Register page")