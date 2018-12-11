from django.urls import path
from . import views # importing views.py

urlpatterns = [
    path('', views.home, name='cas-home'), # views.home (function from views.py, returns http response)
    path('about/', views.about, name='cas-about'), # views.home (function from views.py, returns http response)
    path('data/', views.display_data, name='cas-data'), # views.home (function from views.py, returns http response)
]

