from django.shortcuts import render
from .models import News


def index(request):
    return render(request, 'kazkozvuks/index.html')


def news_title(request):
    news_title = News.objects.order_by('date_added')
    context = {'news_title': news_title}
    return render(request, 'kazkozvuks/news_title.html', context)


def news_topic(request, news_topic_id):
    news_topic = News.objects.get(id=news_topic_id)
    news_entries = news_topic.news_entry_set.order_by('-date_added')
    context = {'news_topic': news_topic, 'news_entries': news_entries}
    return render(request, 'kazkozvuks/news_topic.html', context)