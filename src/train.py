from lightgbm import train
import pandas as pd
import numpy as np
import pickle
from preprocessing import preprocessing, preprocessing2, divide_dataset
from filler import filler
from sklearn.ensemble import RandomForestRegressor

if __name__ == "__main__":
    df = pd.read_csv('..\data\data.csv', encoding='utf-8')
    df = preprocessing(df)
    df = filler(df)
    df = preprocessing2(df)
    X_train, X_test, y_train, y_test = divide_dataset(df)
    regressor = RandomForestRegressor(n_estimators=5, random_state=42,max_features=np.sqrt(0.1), min_samples_leaf=1)
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    erro = abs(y_pred - y_test)
    print(f'Erro médio da regressão random forest é (Em reais): {round(np.mean(erro),2)}')
    with open("../model/rf.pkl", "wb") as file:
        pickle.dump(obj=regressor, file=file)    