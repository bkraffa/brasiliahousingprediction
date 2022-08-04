import pandas as pd
from sklearn.model_selection import train_test_split

def preprocessing(df):
    df.price.replace('\.','', regex=True,inplace=True)
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
'Nome do Edifício','Área Total','Aceita Financiamento','Área Terreno','Unidades no Andar','Aceita Permuta']
    df.drop(columns=columns,inplace=True)
    df['iptuvsarea'] = df['IPTU R$']/df.area
    df.loc[df['iptuvsarea'] < 0.1,'IPTU R$'] = df['IPTU R$'] * 1000
    df.loc[(df['Condomínio R$'] < 50) & (df['area'] > 120),'Condomínio R$'] = df['Condomínio R$'] * 1000
    df['iptuvsarea'] = df['IPTU R$']/df.area
    df.loc[df['iptuvsarea'] < 10,'IPTU R$'] = df['IPTU R$'] * 6
    return df

def preprocessing2(df):
    df = pd.get_dummies(df, columns=['setor'])
    df['price'] = df['price'] + df['Condomínio R$'] + df['IPTU R$']/12
    cols = ['Cidade','Suítes','Garagens','link','iptuvsarea','areaband','setorareaband','name','Condomínio R$','IPTU R$']
    df.drop(columns=cols,inplace=True)
    return df

def divide_dataset(df):
    x = df.drop(columns = 'price')
    Y = df.price
    X_train, X_test, y_train, y_test = train_test_split(x, Y , test_size= 0.3,random_state=42)
    return X_train, X_test, y_train, y_test