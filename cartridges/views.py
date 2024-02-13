from django.shortcuts import render, get_object_or_404
from .models import RefillRecord, Cartridge

def refill_detail(request, refill_id):
    refill = get_object_or_404(RefillRecord, pk=refill_id)
    return render(request, 'refill_detail.html', {'refill': refill})


def refills(request):
    refills = RefillRecord.objects.all()
    return render(request, 'refills.html', {'refills': refills})


def cartridges(request):
    cartridges = Cartridge.objects.all()
    return render(request, 'cartridge.html', {'cartridge': cartridges})


def inrefills(request):
    cartridges = Cartridge.objects.filter(status="RF")
    return render(request, 'inrefills.html', {'cartridge': cartridges})