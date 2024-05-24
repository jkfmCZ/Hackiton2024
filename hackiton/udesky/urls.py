from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("duchdci", views.duchodci_rok, name="duchodci"),
    
    ]