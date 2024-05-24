from django.shortcuts import render
from .graph_gen import duchodci
import plotly.express as px
from plotly.offline import plot
# Create your views here.

def index(request):
    return render(request, "index.html",{})

def duchodci_rok(request):
    fig = px.bar(duchodci, x="rok", y="pocet_duchodcu", title="Počet důchodců")
    pplot = plot(fig, output_type='div')
    return render(request, "duchodci_rok.html", {"plot":pplot})
