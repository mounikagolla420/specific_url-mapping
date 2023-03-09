from app3.views import *
from django.urls import path
app_name='lovely'
urlpatterns=[
    path('kalpana/',kalpana,name='kalpana'),
    path('supri/',supri,name='supri'),
]