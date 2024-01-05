from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hello there friend!')
    return render(request, 'generator/home.html', {'password':'abacbvad'})

def password(request):
    return render(request, 'generator/password.html')