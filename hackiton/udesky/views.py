import pandas as pd
import geopandas as gpd
import json
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .graph_gen import duchodci, fig_soudy
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
    pplot = plot(fig_soudy, output_type='div')
    return render(request, "soudy.html",{"plot":pplot})

def test(request):
    # Load GeoJSON file
    geojson_path = "udesky/data/mapy/czech-regions-low-res.json"
    geodf = gpd.read_file(geojson_path)
    
    df = pd.DataFrame({
        'name': geodf['name'],
        'population': geodf['population']
    })
    
    # Create the choropleth map
    fig = px.choropleth_mapbox(
        df, 
        geojson=geodf.__geo_interface__,  # Use the __geo_interface__ to pass the GeoDataFrame as geojson
        locations='name', 
        color='population',
        hover_name='name', 
        hover_data={'population': True},
        featureidkey="properties.name",  # Adjust this based on your geojson properties
        mapbox_style="carto-positron",
        center={"lat": 49.8, "lon": 15.5},
        zoom=6,
        title="Population by Region in Czech Republic"
    )

    mapa = plot(fig, output_type='div')

    return render(request, "test.html", {"mapa":mapa})