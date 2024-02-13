from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def index(request):
    phonebook = Phonebook.objects.all()
    return render(request, 'index.html', {'phonebook': phonebook})