from django.contrib import admin
from .models import News, News_Entry, Partners, Partners_Entry

# Register your models here.
admin.site.register(News)
admin.site.register(News_Entry)
admin.site.register(Partners)
admin.site.register(Partners_Entry)