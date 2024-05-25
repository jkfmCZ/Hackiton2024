from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("duchodci/", views.duchodci_rok, name="duchodci"),
    path("policie/", views.pcr_nalezy, name="policie"),
    path("fotky/", views.fotky, name="fotky"),
    path("soudy/", views.soudy, name="soudy")
    ]