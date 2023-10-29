from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')



def main(request):
    return render(request, 'master.html')