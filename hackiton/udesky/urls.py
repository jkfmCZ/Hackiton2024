from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("duchodci/", views.duchodci_rok, name="duchodci"),
    path("policie/", views.pcr_nalezy, name="policie"),
    ]