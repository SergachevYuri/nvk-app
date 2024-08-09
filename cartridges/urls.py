from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartridges, name='cartridges'),
    path('refills/', views.refills, name='refills'),
    path('inrefills/', views.inrefills, name='refills'),
    path('refills/<int:refill_id>/', views.refill_detail, name='refill_detail'),
    path('list/', views.cartridge_list, name='cartridge_list'),
]
