from django.urls import path

from . import views

app_name = 'kazkozvuks'
urlpatterns = [
    # start page
    path('', views.index, name='index'),
    # news page
    path('news/', views.newss, name='news'),
]