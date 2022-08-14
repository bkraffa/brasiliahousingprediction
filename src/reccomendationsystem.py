import numpy as np 
import pandas as pd
import seaborn as sns
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn import neighbors

def RecomendaImoveis(area,quartos,setor):
    df_original = pd.read_csv('data/dfpreprocessed.csv',error_bad_lines = False)
    df_original.drop(columns = 'Unnamed: 0', inplace=True)
    df_original['valor_total'] = df_original['price'] + df_original['Condomínio R$']
    df = pd.read_csv('data\dffinal.csv',error_bad_lines = False)
    df.drop(columns = 'Unnamed: 0', inplace=True)

    userInput = [{'area':area,'Quartos':quartos,'setor':setor}]
    userInput = pd.DataFrame(userInput)

    with open("model/ohe.pkl", "rb") as file:
        ohe = pickle.load(file)
    
    dummy = ohe.transform(userInput.setor.to_numpy().reshape(-1,1))
    dummy = pd.DataFrame(dummy.toarray(), columns = ohe.get_feature_names())

    userInput.drop(columns='setor', inplace=True)
    userInput = pd.concat([userInput,dummy],axis=1)

    df = pd.concat([userInput,df],axis=0).reset_index(drop=True)

    features = df.drop(columns=['price'])

    model = neighbors.NearestNeighbors(n_neighbors=11, algorithm='ball_tree')
    model.fit(features)
    dist, idlist = model.kneighbors(features)

    df_original = df_original[['name','valor_total','price','Condomínio R$','area','Quartos','Cidade','link']]

    mais_proximos = []
    for x in idlist[0]:
        if x != 0:
            mais_proximos.append(x-1)

    top10 = df_original.loc[mais_proximos].reset_index(drop=True)
    top10.fillna(0,inplace=True)
    top10['Condomínio R$'] = top10['Condomínio R$'].astype(int)
    top10['Quartos'] = top10['Quartos'].astype(int)
    top10['price'] = top10['price'].astype(int)
    top10['valor_total'] = top10['price'] + top10['Condomínio R$']
    top10['valor_total'] = top10['valor_total'].astype(int)
    #top10 = top10.replace({0:'Não disponível'})
    top10.Cidade = top10.Cidade.str.split('-').str[1].str.strip()

    return top10