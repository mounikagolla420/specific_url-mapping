from app2.views import *
from django.urls import path
app_name='lovely'
urlpatterns=[
    path('vijji/',vijji,name='vijji'),
    path('mahi/',mahi,name='mahi'),
]