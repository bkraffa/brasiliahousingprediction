import numpy as np

def filler(df):
    cols = ["IPTU R$",'Condomínio R$']
    df[cols] = df[cols].replace({'0':np.nan, 0:np.nan})
    bins = [ 0,40,70,100,150,200]
    df['areaband'] = np.searchsorted(bins, df['area'].values)
    df['setorareaband'] = df['setor'].astype(str) + '-' + df['areaband'].astype(str)
    df['Condomínio R$'] = df['Condomínio R$'].fillna(df.groupby('setorareaband')['Condomínio R$'].transform('mean'))
    df['Condomínio R$'] = df['Condomínio R$'].fillna(df.groupby('areaband')['Condomínio R$'].transform('mean'))
    df['IPTU R$'] = df['IPTU R$'].fillna(df.groupby('setorareaband')['IPTU R$'].transform('mean'))
    df['IPTU R$'] = df['IPTU R$'].fillna(df.groupby('areaband')['IPTU R$'].transform('mean')) 
    df['Quartos'] = df['Quartos'].fillna(df.groupby('setorareaband')['Quartos'].transform('median'))
    return df