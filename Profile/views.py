from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def Register(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('Profile:Login')
        
    context = {
        'form':form
    }
    
    return render(request, 'Profile/Register.html', context)

