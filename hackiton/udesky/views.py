import pandas as pd
import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot



from .graph_gen import duchodci


def index(request):
    return render(request, "index.html",{})

def duchodci_rok(request):
    fig = px.bar(duchodci, x="rok", y="pocet_duchodcu", title="Počet důchodců")
    pplot = plot(fig, output_type='div')
    return render(request, "duchodci_rok.html", {"plot":pplot})



def pcr_nalezy(request):
    # Load the data
    df_prc = pd.read_json("udesky/data/pcr_filtered_informace.json")

    # Convert 'vyvěšení' column to datetime
    df_prc['vyvěšení'] = pd.to_datetime(df_prc['vyvěšení'])

    # Extract year and month from 'vyvěšení' column
    df_prc['year_month'] = df_prc['vyvěšení'].dt.to_period('M')

    # Group by year and month
    df_count = df_prc.groupby('year_month').size().reset_index(name='count')

    # Convert 'year_month' back to datetime for plotting
    df_count['year_month'] = df_count['year_month'].dt.to_timestamp()

    # Create bar plot
    fig = px.bar(df_count, x='year_month', y='count', title='Počet nálezů střeliva/zbraní v ČR podle měsíců (2010-2020)',
                 labels={'year_month': 'Date', 'count': 'Počet nálezů střeliva/zbraní'})

    # Generate the plot
    pplot = plot(fig, output_type='div')

    # Render the template with the plot
    return render(request, "pcr_nalezy.html", {"plot": pplot})
