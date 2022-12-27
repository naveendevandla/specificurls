from django.urls import path
from A.views import *
app_name='Aa'
urlpatterns=[
    path('spe/',spe,name='spe'),
]