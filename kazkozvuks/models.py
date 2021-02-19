from django.db import models


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

    class Meta:
        verbose_name_plural = 'news_entries'

    def __str__(self):
        return f"{self.text[:50]}..."