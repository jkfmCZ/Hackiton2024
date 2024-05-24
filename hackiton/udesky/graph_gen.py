import pandas as pd


dfkraje = pd.read_csv("duchodci-v-cr-krajich-okresech.csv")
dfkraje['rok'] = dfkraje['referencni_obdobi'].apply(lambda x: x.split('-')[0])

duchodci = dfkraje[
        (dfkraje["druh_duchodu"] == "Starobní důchod S") & 
        (dfkraje["pohlavi"] == "Celkem") & 
        (dfkraje["referencni_oblast"] == "Česká republika")]

