from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

## creating some data to pass to the pages with templates
posts = [
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
            'posts':posts
            }
    return render(request, 'cas/home.html', context) # returning templates in templates/cas

def about(request):
    return render(request, 'cas/about.html', {'title': "Abouty-using template for title"})
