from app1.views import *
from django.urls import path
app_name='bujji'
urlpatterns=[
    path('mouni/',mouni,name='mouni'),
    path('sari/',sari,name='sari'),
]