from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # import whatever object / table you want to display
# Create your views here.

## creating some data to pass to the pages with templates
stuff = [
        {
            'name': 'Lisa',
            'position': 'Director',
            'from': 'U.S.'
            },
        {
            'name': 'Francis',
            'position': 'Tutor Supervisor',
            'from': 'Taiwan'
            },
        {
            'name': 'Noele',
            'position': 'SIA boss',
            'from': 'Japan??'
            }
        ]

def home(request):
    context = {
            'posts':Post.objects.all()
            }
    return render(request, 'cas/home.html', context) # returning templates in templates/cas

def about(request):
    context = {'stuff':stuff}
    return render(request, 'cas/about.html', context)
