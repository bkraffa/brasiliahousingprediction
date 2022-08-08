import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pickle


def preprocessing(df):
    df.price.replace('\.','', regex=True,inplace=True)
    df.drop(df[df.Cidade == 'BRASÍLIA - JARDINS MANGUEIRAL'].index, inplace=True)
    df.price = df.price.astype(int) 
    df.drop(df[df.price > 50000].index, inplace=True)
    df.area = df.area.str.split(',').str[0]
    df.area.replace('\.','', regex=True,inplace=True)
    df.area = df.area.astype(int)
    df.drop(df[df.area > 2000].index, inplace=True)
    df.drop(df[df.area == 0].index, inplace=True)
    df.loc[df['area'] > 1000,'area'] = df['area']/10
    df['setor'] = df.name.str.split(' ').str[0]
    df.loc[df['setor'] == 'SGAN\xa0911','setor'] = 'SGAN'
    df.loc[df['Cidade'] == 'BRASÍLIA - VILA PLANALTO','setor'] = 'Vila Planalto'
    df.loc[df['setor'] == 'Área','setor'] = 'AOS'
    columns = ['Unnamed: 0','valueperm2','Posição do Sol','Posição do Imóvel','Andar do Apartamento','Total de Andar do Empreendimento',
'Nome do Edifício','Área Total','Aceita Financiamento','Área Terreno','Unidades no Andar','Aceita Permuta','IPTU R$']
    df.drop(columns=columns,inplace=True)
    #df['iptuvsarea'] = df['IPTU R$']/df.area
    #df.loc[df['iptuvsarea'] < 0.1,'IPTU R$'] = df['IPTU R$'] * 1000
    df.loc[(df['Condomínio R$'] < 50) & (df['area'] > 120),'Condomínio R$'] = df['Condomínio R$'] * 1000
    #df['iptuvsarea'] = df['IPTU R$']/df.area
    #df.loc[df['iptuvsarea'] < 10,'IPTU R$'] = df['IPTU R$'] * 6
    df.to_csv('../data/dfpreprocessed.csv')
    return df

def encoding(df):
    df['price'] = df['price'] + df['Condomínio R$'] 
    cols = ['Cidade','Suítes','Garagens','link','name','Condomínio R$','setorareaband','areaband']
    df.drop(columns=cols,inplace=True)
    df = df.reset_index(drop=True)
    ohe = OneHotEncoder(handle_unknown='ignore')
    ohe.fit(df['setor'].to_numpy().reshape(-1,1))
    with open('../model/ohe.pkl', 'wb') as f:
        pickle.dump(ohe, f)
    dummies = ohe.transform(df['setor'].to_numpy().reshape(-1,1))
    dummies = pd.DataFrame(dummies.toarray(), columns = ohe.get_feature_names())
    df.drop(columns = 'setor', inplace=True)
    df = pd.concat([df,dummies],axis=1)
    df.to_csv('../data/dffinal.csv')
    return df

def divide_dataset(df):
    x = df.drop(columns = 'price')
    Y = df.price
    X_train, X_test, y_train, y_test = train_test_split(x, Y , test_size= 0.3,random_state=42)
    return X_train, X_test, y_train, y_test