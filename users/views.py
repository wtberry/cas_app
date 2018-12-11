from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # now create form to pass to template, let's use pre-made for now
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form}) # render the register
