from django.urls import path
from app2.views import *

app_name='satya'

urlpatterns=[
    path('lucky/',lucky,name='lucky'),
]