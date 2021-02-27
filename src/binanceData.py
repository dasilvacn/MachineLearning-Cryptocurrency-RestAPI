import numpy as np
import pandas as pd
from binance.client import Client
from sklearn.ensemble import  GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from  sklearn.metrics import mean_squared_error
import pickle



client = Client()

df = pd.DataFrame()
coinList = [
    "BTCUSDT","ETHUSDT","BNBUSDT",
    "LTCUSDT","NEOUSDT","XRPUSDT",
    "ADAUSDT","BELUSDT","XLMUSDT",
    "BATUSDT","LINKUSDT","BANDUSDT",
    "ONTUSDT","IOTAUSDT"
    ]

matris = []
for i in coinList:
    liste = []
    candles = client.get_historical_klines(i, Client.KLINE_INTERVAL_1HOUR, "01 OCT, 2020", "26 Feb, 2021")
    for j in candles:
        liste.append(j[4])
    df[i]=liste

df.to_csv('file_name.csv')

coinList = [
    "BTCUSDT","ETHUSDT","BNBUSDT",
    "LTCUSDT","NEOUSDT","XRPUSDT",
    "ADAUSDT","BELUSDT","XLMUSDT",
    "BATUSDT","LINKUSDT","BANDUSDT",
    "ONTUSDT","IOTAUSDT"
]
df = pd.read_csv("file_name.csv")
for i in coinList:
    df = df[coinList]
    #print(df.head())
    x = df.drop([i], inplace =False, axis=1)
    y = df[[i]].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state=42)
    GRAD = GradientBoostingRegressor()
    GRAD.fit(x_train, y_train.ravel())
    preds = GRAD.predict(x_test)
    mse = mean_squared_error(y_test, preds)
    print("GRADIENT: ", np.sqrt(mse))
    pickle.dump(GRAD, open(i, 'wb'))