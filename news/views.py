from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.all().order_by('-date_added')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

# Create your views here.
