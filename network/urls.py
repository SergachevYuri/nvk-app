from django.urls import path
from . import views

urlpatterns = [
    path('', views.network_home, name='network_home'),
    path('switches/', views.switches, name='switches'),
    path('switches/<int:switch_id>/ports/', views.switch_ports, name='switch_ports'),
    path('ip-addresses/', views.ip_addresses, name='ip_addresses'),
]