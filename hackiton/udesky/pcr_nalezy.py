import pandas as pd
import plotly.express as px
import plotly.offline as plot
import plotly.graph_objects as go

df_prc = pd.read_json("udesky/data/pcr_filtered_informace.json")

df_prc['vyvěšení'] = pd.to_datetime(df_prc['vyvěšení'])
df_prc['year_month'] = df_prc['vyvěšení'].dt.to_period('M')
df_count = df_prc.groupby('year_month').size().reset_index(name='count')
df_count['year_month'] = df_count['year_month'].dt.to_timestamp()
df_count['year'] = df_count['year_month'].dt.year

fig_pcr = px.bar(df_count, x='year_month', y='count', title='Počet nálezů střeliva / zbraní v ČR podle měsíců (2022-2024)',
             labels={'year_month': 'Čas', 'count': 'střelivo / zbraně'},)
fig_cr_tree = px.treemap(
    df_count,
    path=["year","yer_month"],  # Hierarchie
    values='count',  # Sloupec s hodnotami
    title='Počet nálezů střeliva / zbraní v ČR podle měsíců (2022-2024) ve stromovem grafu'
)



# Tabulka
df_prc = pd.read_json("udesky/data/pcr_filtered_informace.json")

df_prc['vyvěšení'].replace('', 'No date', inplace=True)

fig_pcr_tabulka = go.Figure(data=[go.Table(
    columnwidth=[50, 400],
    header=dict(values=[['<b>Datum</b>'],
                        ['<b>Oznámení</b>']],
                fill_color='royalblue',
                align='left',
                font=dict(color='white', size=12)),
    cells=dict(values=[df_prc['vyvěšení'], df_prc['název']],
               fill_color=[['#f1f1f1', 'white'] * (len(df_prc) // 2)],
               align='left'))
])

