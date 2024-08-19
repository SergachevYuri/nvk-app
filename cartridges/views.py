from django.shortcuts import render, get_object_or_404, redirect
from .models import Cartridge
import qrcode
import io
import base64
from .models import RefillRecord, Cartridge, Status
from django.views.generic import ListView
from .forms import CartridgeFilterForm


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


def cartridge_list(request):
    cartridges = Cartridge.objects.order_by("date_added")

    # Генерация QR-кодов для каждого картриджа
    for cartridge in cartridges:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(request.build_absolute_uri(f'/cartridges/{cartridge.id}/'))  # Заменяем на нужный URL
        qr.make(fit=True)

        # Создание изображения QR-кода
        qr_code_image = qr.make_image(fill_color="black", back_color="white")

        # Преобразование изображения в base64
        buffer = io.BytesIO()
        qr_code_image.save(buffer)
        qr_code_image_data = base64.b64encode(buffer.getvalue()).decode()

        # Добавление QR-кода в контекст
        cartridge.qr_code_data = qr_code_image_data

    context = {
        'cartridges': cartridges,
    }
    return render(request, 'cartridge_list.html', context)


def cartridge_detail(request, cartridge_id):
    cartridge = get_object_or_404(Cartridge, pk=cartridge_id)

    # Генерация QR-кода для картриджа
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(request.build_absolute_uri(f'/cartridges/{cartridge.id}/'))
    qr.make(fit=True)

    # Создание изображения QR-кода
    qr_code_image = qr.make_image(fill_color="black", back_color="white")

    # Преобразование изображения в base64
    buffer = io.BytesIO()
    qr_code_image.save(buffer)
    cartridge.qr_code_data = base64.b64encode(buffer.getvalue()).decode()

    last_refill = cartridge.refillrecord_set.order_by('-date_sent').first()
    last_refill_date = last_refill.date_sent if last_refill else None

    context = {
        'cartridge': cartridge,
        'last_refill_date': last_refill_date,
    }
    return render(request, 'cartridge_detail.html', context)



def cartridge_confirm_refill(request, cartridge_id):
    cartridge = get_object_or_404(Cartridge, pk=cartridge_id)

    if request.method == 'POST':
        cartridge.status = Status.REFILLED  # Assuming you have a Status.REFILLED value
        cartridge.save()
        return redirect('cartridge_detail', cartridge_id=cartridge_id)  # Redirect back to the detail page

    return redirect('cartridge_list')  # Or redirect to another page

class CartridgeListView(ListView):
    model = Cartridge
    template_name = "cartridge_list.html"
    context_object_name = "cartridges"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Фильтрация по статусу, если выбран в форме
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        # Сортировка
        order_by = self.request.GET.get('order_by', 'date_added')  # Сортировка по умолчанию - по дате добавления
        queryset = queryset.order_by(order_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = CartridgeFilterForm(self.request.GET)
        return context