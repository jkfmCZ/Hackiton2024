import pandas as pd
import geopandas as gpd
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .graph_gen import  fig_cr_line, fig_cr_tree, df_kraje
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

    fig_bar = plot(fig_pcr, output_type='div')
    ptable = plot(fig_pcr_tabulka, output_type='div')

    return render(request, "pcr_nalezy.html", {"plot": fig_bar, "table": ptable})

def soudy(request):
    pplot = plot(fig_cr_tree, output_type='div')
    return render(request, "soudy.html",{"plot":pplot})
def testt(request):
    # Load GeoJSON file


    geojson_path = "udesky/data/mapy/czech-regions-low-res.json"
    geodf = gpd.read_file(geojson_path)
    # rokymax = df["rok"].max()
    df_krajky = df_kraje

    df = pd.DataFrame({
        'name': geodf['name'],
        'prumerna_vyse_duchodu': df_kraje.set_index('name').reindex(geodf['name'])['prumerna_vyse_duchodu'].values
    })

    # Create the choropleth map
    fig = px.choropleth_mapbox(
        df, 
        geojson=geodf.__geo_interface__,  # Use the __geo_interface__ to pass the GeoDataFrame as geojson
        locations='name', 
        color='prumerna_vyse_duchodu',
        hover_name='name', 
        hover_data={'prumerna_vyse_duchodu': True},
        featureidkey="properties.name",  # Adjust this based on your geojson properties
        mapbox_style="carto-positron",
        center={"lat": 49.8, "lon": 15.5},
        zoom=6,
        title="Average Pension Amount by Region in the Czech Republic"
    )

    mapa = plot(fig, output_type='div')

    return render(request, "test.html", {"mapa": mapa})

def test(request):
    geojson_path = "udesky/data/mapy/czech-regions-low-res.json"
    geodf = gpd.read_file(geojson_path)
    df = pd.DataFrame({
        'name': geodf['name'],
        'population': geodf['population']
    })
    
    df_kraje.to_json("udesky/data/mapy/kraje_test.json")
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
