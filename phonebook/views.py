from django.shortcuts import render
from .models import Phonebook
from organization.models import Directorate, Department

def index(request):
    departments = Department.objects.all()
    phonebook = Phonebook.objects.all()
    context = {
        'departments': departments,
        'phonebook': phonebook,
    }
    return render(request, 'phonebook.html', context)
