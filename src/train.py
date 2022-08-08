from lightgbm import train
import pandas as pd
import numpy as np
import pickle
from preprocessing import preprocessing, encoding, divide_dataset
from filler import filler
from sklearn.ensemble import RandomForestRegressor
from webscraping import ScrapeImoveis 
from datetime import datetime


def RetornaData():
    data = datetime.today().strftime('%d-%m-%Y')
    return data

if __name__ == "__main__":
    ScrapeImoveis()
    df = pd.read_csv('..\data\data.csv', encoding='utf-8')
    df = preprocessing(df)
    df = filler(df)
    df = encoding(df)
    X_train, X_test, y_train, y_test = divide_dataset(df)
    regressor = RandomForestRegressor(n_estimators=50, max_depth=15,min_samples_split=3, random_state=42)
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    erro = abs(y_pred - y_test)
    print(f'Erro médio da regressão random forest é (Em reais): {round(np.mean(erro),2)}')
    data = RetornaData()
    print(f'Data do treinamento do modelo:{data}')
    with open("../model/rf.pkl", "wb") as file:
        pickle.dump(obj=regressor, file=file)