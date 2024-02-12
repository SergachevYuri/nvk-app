from django.shortcuts import render, get_object_or_404
from .models import RefillRecord

def refill_detail(request, refill_id):
    refill = get_object_or_404(RefillRecord, pk=refill_id)
    return render(request, 'refill_detail.html', {'refill': refill})


def refills(request):
    refills = RefillRecord.objects.all()
    return render(request, 'refills.html', {'refills': refills})