from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        gender=str(request.POST['gender'])
        
        check_user=UserDB.objects.filter(email=email)
        if check_user:
            return render(request,'home.html',{'error':'Email id already register'})
        users=UserDB(name=name,email=email,gender=gender)
        users.save()
        if gender=='male':
            return redirect('form-m')
        if gender=='female':
            return redirect('form-f')
            
            

    return render(request,'home.html')

def mform(request):
    return render(request,'formTwo.html')
def fform(request):
    return render(request,'formThree.html')