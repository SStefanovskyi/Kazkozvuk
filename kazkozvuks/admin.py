from django.contrib import admin
from .models import News, News_Entry

# Register your models here.
admin.site.register(News)
admin.site.register(News_Entry)