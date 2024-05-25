import pandas as pd
import json


dfkraje = pd.read_csv("udesky/data/duchodci-v-cr-krajich-okresech.csv") #editoval jsem cestu mozna bude potreba zmenit
dfkraje['rok'] = dfkraje['referencni_obdobi'].apply(lambda x: x.split('-')[0])

duchodci = dfkraje[
        (dfkraje["druh_duchodu"] == "Starobní důchod S") & 
        (dfkraje["pohlavi"] == "Celkem") & 
        (dfkraje["referencni_oblast"] == "Česká republika")]



<<<<<<< Updated upstream
# file = "/udesky/data/soudy_decin.jsondl"
# with open(file, 'r', encoding='utf-8') as file:
#     data = json.load(file)
=======
file = "udesky/data/soudy_decin.jsonld"
with open(file, 'r', encoding='utf-8') as file:
    data = json.load(file)
>>>>>>> Stashed changes


# df = pd.json_normalize(data['informace'])
# # print(df)
# df['vyvěšení.datum_a_čas'] = pd.to_datetime(df['vyvěšení.datum_a_čas'])


# df['rok_vyvěšení'] = df['vyvěšení.datum_a_čas'].dt.year
# df["count"] = 1
# df_count_per_year = df.groupby('rok_vyvěšení').size().reset_index(name='count')


# df_count_per_year.reset_index(drop=True, inplace=True)

# # print(df_count_per_year)
# data = {
#     'název_obce': ["Děčín"],
#     '2023': [df_count_per_year["count"].loc[0]],
#     '2024': [df_count_per_year["count"].loc[1]]}
# df2 = pd.DataFrame(data)

