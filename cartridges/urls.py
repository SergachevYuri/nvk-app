from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartridges, name='cartridges'),
    path('<int:cartridge_id>/', views.cartridge_detail, name='cartridge_detail'),
    path('refills/', views.refills, name='refills'),
    path('inrefills/', views.inrefills, name='inrefills'),  # Исправил name на 'inrefills' для уникальности
    path('refills/<int:refill_id>/', views.refill_detail, name='refill_detail'),
    path('list/', views.cartridge_list, name='cartridge_list'),
    path('<int:cartridge_id>/confirm_refill/', views.cartridge_confirm_refill, name='cartridge_confirm_refill'),
]
