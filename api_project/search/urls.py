from unicodedata import name
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    url('post',views.post,name="post"),
    
]