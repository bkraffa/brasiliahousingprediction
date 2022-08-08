import fastapi
from pydantic import BaseModel
from fastapi import FastAPI
import pickle
import pandas as pd
from src.reccomendationsystem import RecomendaImoveis

class Item(BaseModel):
    text: str

with open("model/rf.pkl", "rb") as file:
    rf = pickle.load(file)

with open("model/ohe.pkl", "rb") as file:
    ohe = pickle.load(file)

app = FastAPI()

x = {'area': 60, 'Quartos':2, 'setor':'CA'}
dct = {k:[v] for k,v in x.items()}

df = pd.DataFrame.from_dict(dct)
dummy = ohe.transform(df.setor.to_numpy().reshape(-1,1))
dummy = pd.DataFrame(dummy.toarray(), columns = ohe.get_feature_names())
df.drop(columns='setor', inplace=True)
df = pd.concat([df,dummy],axis=1)
y_pred = rf.predict(df)
print(y_pred)

top10 = RecomendaImoveis(x['area'],x['Quartos'],x['setor'])
print(top10)
