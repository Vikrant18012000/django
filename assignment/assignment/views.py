from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def create(request):
    if request.method =='POST':
        name: request.POST['name']
        email: request.POST['email']
        bio: request.POST['bio']
        new_profile = Profile(name=name,email=email,bio=bio)
        new_profile.save()
        success ='User'+name+'created successfully'
        return HttpResponse(success)