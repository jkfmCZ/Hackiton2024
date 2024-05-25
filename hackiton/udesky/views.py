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

def duchody_kraje(request):
    pension_data = {
        "Kraj Vysočina": 15139.0,
        "Jihomoravský kraj": 14070.0,
        "Olomoucký kraj": 13427.0,
        "Moravskoslezský kraj": 15783.0,
        "Zlínský kraj": 13988.0,
        "Středočeský kraj": 14126.0,
        "Jihočeský kraj": 15118.0,
        "Plzeňský kraj": 13978.0,
        "Karlovarský kraj": 13736.0,
        "Ústecký kraj": 14516.0,
        "Liberecký kraj": 13634.0,
        "Královéhradecký kraj": 14380.0,
        "Pardubický kraj": 14160.0,
        "Hlavní město Praha": 13427.0,
    }
      # Convert the dictionary to a DataFrame
    df_kraje = pd.DataFrame(list(pension_data.items()), columns=['name', 'prumerna_vyse_duchodu'])

    # Load the GeoJSON file
    geojson_path = "udesky/data/mapy/czech-regions-low-res.json"
    geodf = gpd.read_file(geojson_path)
    
    # Clean the name columns by stripping any extra spaces
    geodf['name'] = geodf['name'].str.strip()
    df_kraje['name'] = df_kraje['name'].str.strip()

    # Merge the GeoDataFrame with the pension DataFrame on the 'name' column
    merged_df = geodf.merge(df_kraje, on='name', how='left')
    
    # Create the choropleth map
    fig = px.choropleth_mapbox(
        merged_df, 
        geojson=merged_df.__geo_interface__,  # Use the __geo_interface__ to pass the GeoDataFrame as geojson
        locations='name', 
        color='prumerna_vyse_duchodu',
        hover_name='name', 
        hover_data={'prumerna_vyse_duchodu': True},
        featureidkey="properties.name",  # Adjust this based on your geojson properties
        mapbox_style="carto-positron",
        center={"lat": 49.8, "lon": 15.5},
        zoom=6,
        title="průměrná výše důchodu v jednotlivých krajích 2022"
    )

    mapa = plot(fig, output_type='div')

    return render(request, "test.html", {"mapa": mapa})