from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kusoma(request):
    return HttpResponse('Acha tusome')

def mtihani(request):
    return HttpResponse('Ni rahisi sanaa')
