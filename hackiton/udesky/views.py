import pandas as pd
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .graph_gen import duchodci


def index(request):
    return render(request, "index.html",{})

def fotky(request):
    return render(request, "fotky.html",{})

def duchodci_rok(request):
    fig = px.bar(duchodci, x="rok", y="pocet_duchodcu", title="Počet důchodců")
    pplot = plot(fig, output_type='div')
    return render(request, "duchodci_rok.html", {"plot":pplot})

def pcr_nalezy(request):

    #Bar chart
    df_prc = pd.read_json("udesky/data/pcr_filtered_informace.json")

    df_prc['vyvěšení'] = pd.to_datetime(df_prc['vyvěšení'])
    df_prc['year_month'] = df_prc['vyvěšení'].dt.to_period('M')
    df_count = df_prc.groupby('year_month').size().reset_index(name='count')
    df_count['year_month'] = df_count['year_month'].dt.to_timestamp()

    fig = px.bar(df_count, x='year_month', y='count', title='Počet nálezů střeliva / zbraní v ČR podle měsíců (2022-2024)',
                 labels={'year_month': 'Čas', 'count': 'střelivo / zbraně'},)

    pplot = plot(fig, output_type='div')

    #Tabulka
    df_prc = pd.read_json("udesky/data/pcr_filtered_informace.json")

    df_prc['vyvěšení'].replace('', 'No date', inplace=True)

    fig = go.Figure(data=[go.Table(
        columnwidth = [50,400],
           
    header=dict(values=[['<b>Datum</b>'],
                  ['<b>Oznámení</b>']],
                fill_color='royalblue',
                align='left',
                font=dict(color='white', size=12)),  # Added closing parenthesis here
    cells=dict(values=[df_prc['vyvěšení'], df_prc['název']],
                fill_color=[['#f1f1f1', 'white'] * (len(df_prc) // 2)],
               align='left'))
])
    ptable = plot(fig, output_type='div')


    return render(request, "pcr_nalezy.html", {"plot": pplot, "table": ptable})
