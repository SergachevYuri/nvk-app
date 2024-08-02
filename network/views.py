from django.shortcuts import render, get_object_or_404
from .models import Switch, Ports, IPAM

def network_home(request):
    return render(request, 'base.html')

def switches(request):
    switches = Switch.objects.all()
    return render(request, 'switches.html', {'switches': switches})

def switch_ports(request, switch_id):
    switch = get_object_or_404(Switch, id=switch_id)
    ports = Ports.objects.filter(switch=switch)
    return render(request, 'switch_ports.html', {'switch': switch, 'ports': ports})

def ip_addresses(request):
    ip_addresses = IPAM.objects.all()
    return render(request, 'ip_addresses.html', {'ip_addresses': ip_addresses})
