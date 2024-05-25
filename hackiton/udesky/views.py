import pandas as pd
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .graph_gen import  fig_cr_line, fig_cr_tree
from .pcr_nalezy import fig_pcr, fig_pcr_tabulka


def index(request):
    return render(request, "index.html",{})

def fotky(request):
    return render(request, "fotky.html",{})

def duchodci_rok(request):
    
    pplot_line = plot(fig_cr_line, output_type='div')
    pplot_tree = plot(fig_cr_tree,output_type="div")
    return render(request, "duchodci_rok.html", {"plot_line":pplot_line,"plot_tree":pplot_tree})
   
def pcr_nalezy(request):
    ptable = plot(fig_pcr_tabulka, output_type='div')
    pplot = p

    return render(request, "pcr_nalezy.html", {"plot": pplot, "table": ptable})

def soudy(request):
    pplot = plot(fig, output_type='div')
    return render(request, "soudy.html",{"plot":pplot})
