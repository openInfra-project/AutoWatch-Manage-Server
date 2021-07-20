from django.http import response
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')

def makeroom(request):
    return render(request,'makeroom.html')    
    
def enteroom(request):
    return render(request,'enteroom.html')    