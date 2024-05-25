import pandas as pd
import plotly.express as px
import plotly.offline as plot
import json




df = pd.read_csv("udesky/data/duchodci-v-cr-krajich-okresech.csv")
df['referencni_obdobi'] = pd.to_datetime(df['referencni_obdobi'])
df['rok'] = df['referencni_obdobi'].dt.year
df["real_pocet"] = df["pocet_duchodcu"] *1000
df = df[df["druh_duchodu"]=="Starobní důchod SD"]


df = df[df["pohlavi"] =="Celkem"]
df_kraje = df[df['referencni_oblast'].str.contains("Kraj|kraj", na=False)]
df_cr = df[df["referencni_oblast"]=="Česká republika"]
df_cr
fig_cr_line = px.line(df_cr, x="rok", y="real_pocet", title='Důchodci jsou také  kriminálníci')

fig_cr_tree = px.treemap(
    df_cr,
    path=["referencni_oblast","rok"],  # Hierarchie
    values='prumerna_vyse_duchodu',  # Sloupec s hodnotami
    title='Stromový graf důchodů podle druhu, pohlaví a oblasti'
)



dta = {
    "nazev_okresu":[""],
    2018:[""],
    2019:[""],
    2020:[""],
    2021:[""],
    2022:[""],
    2023:[""],
    2024:[""]
}
df_d = pd.DataFrame(dta)
chomutov = "udesky/data/chomutov_soudy.jsonld"
most= "udesky/data/most_soud.jsonld"
decin = "udesky/data/soudy_decin.jsonld"
usti = "udesky/data/usti_soud.jsonld"
b=0
jmena = ["Chomutov","Most","Děčin","Ústi","Louny","Litomeřice"]
listerpister = [chomutov,most,decin,usti,]
for x in listerpister:
    print(x)
    with open(x, 'r', encoding='utf-8') as file:
        data = json.load(file)

    df = pd.json_normalize(data['informace'])
    df['vyvěšení.datum_a_čas'] = pd.to_datetime(df['vyvěšení.datum_a_čas'])


    df['rok_vyvěšení'] = df['vyvěšení.datum_a_čas'].dt.year
    df["count"] = 1
    df_count_per_year = df.groupby('rok_vyvěšení').size().reset_index(name='count')

    df_count_per_year.reset_index(drop=True, inplace=True)

    df_count_per_year.sort_values(by=["rok_vyvěšení"], ascending=False)
    df_d.at[b, "nazev_okresu"] = jmena[b]
    pocet = df_count_per_year.shape[0]
    for i in range(pocet):
        if df_count_per_year["rok_vyvěšení"].loc[i] < 2018:
            print("no ben")
            # print(df_count_per_year["rok_vyvěšení"].loc[i])
        else:
            df_d.at[b,df_count_per_year["rok_vyvěšení"].loc[i]] = df_count_per_year["count"].loc[i]
            # print(i)
    # print(df_d)
    b += 1
for i in range(0,2):
      df_d.at[b, "nazev_okresu"] = jmena[b]
      b+=1

# Append the dictionary to the DataFrame
# df_d = pd.concat([df_d, pd.DataFrame([new_row])], ignore_index=True)
# print(df_d)
# x = 0
# for i in df_count_per_year["rok_vyvěšení"]:
#     try:
#         df_d[i].loc[0] = df_count_per_year["count"].loc[x]
#     except:
#         print("gg")

print(df_d.to_string)

fig = px.bar(df_d, x="nazev_okresu", y=2023, title="Počet soudů v rokach")




