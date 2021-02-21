from django.shortcuts import render
from .models import News


def index(request):
    return render(request, 'kazkozvuks/index.html')


def newss(request):
    newss = News.objects.order_by('date_added')
    context = {'newss': newss}
    return render(request, 'kazkozvuks/news.html', context)