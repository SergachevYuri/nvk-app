from django.urls import path
from . import views

urlpatterns = [
    path('refills/', views.refills, name='refills'),
    path('refills/<int:refill_id>/', views.refill_detail, name='refill_detail'),
]
