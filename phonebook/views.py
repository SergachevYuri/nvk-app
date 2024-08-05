from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def index(request):
    phonebook = Phonebook.objects.all().order_by('name')
    return render(request, 'phonebook.html', {'phonebook': phonebook})