from turtle import home
from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def index(request):
    return render(request,'index.html')

def post(request):  
    if request.method == 'POST':
        movie=request.POST['movie']
        url = "https://mdblist.p.rapidapi.com/"
        querystring = {"s":movie}
        headers = {
            'x-rapidapi-host': "mdblist.p.rapidapi.com",
            'x-rapidapi-key': "58953ca82amshff54863aa2d9305p193405jsnc6a5c76a2a03"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer=response.text
        #call_api=requests.post('',params=movie)
        #print(movie)
        return render(request,'home.html',{'movie':answer})
        #return render(request,'home.html')











