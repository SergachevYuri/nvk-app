from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def index(request):
    phonebook = Phonebook.objects.all()
    return render(request, 'phonebook.html', {'phonebook': phonebook})