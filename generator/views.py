from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length')) # obtenemos el valor de length desde la url, debemos pasar de string a int

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@#$%&/?¿-_*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})

