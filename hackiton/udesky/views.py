import pandas as pd
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .graph_gen import duchodci, fig
from .pcr_nalezy import fig_pcr, fig_pcr_tabulka


def index(request):
    return render(request, "index.html",{})

def fotky(request):
    return render(request, "fotky.html",{})

def duchodci_rok(request):
    fig = px.bar(duchodci, x="rok", y="pocet_duchodcu", title="Počet důchodců")
    pplot = plot(fig, output_type='div')
    return render(request, "duchodci_rok.html", {"plot":pplot})

def pcr_nalezy(request):


    pplot = plot(fig_pcr, output_type='div')


    ptable = plot(fig_pcr_tabulka, output_type='div')


    return render(request, "pcr_nalezy.html", {"plot": pplot, "table": ptable})

def soudy(request):
    pplot = plot(fig, output_type='div')
    return render(request, "soudy.html",{"plot":pplot})
