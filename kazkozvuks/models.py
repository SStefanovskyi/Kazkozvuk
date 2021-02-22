from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class News(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class News_Entry(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    video = EmbedVideoField(blank=True, verbose_name='Відео')

    class Meta:
        verbose_name_plural = 'news_entries'

    def __str__(self):
        return f"{self.text[:50]}..."


class Partners(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Partners_Entry(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'partners_entry'

    def __str__(self):
        return f"{self.text[:50]}..."