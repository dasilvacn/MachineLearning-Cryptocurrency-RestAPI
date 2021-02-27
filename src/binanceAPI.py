from flask_restful import Api, Resource, reqparse
import json
import numpy as np
import pandas as pd
from binance.client import Client
import pickle


class Route(Resource):
    def get(self):
        return {
            "ETHEREUM" : "http://127.0.0.1:5000/ETHUSDT", "BINANCE COIN" : "http://127.0.0.1:5000/BNBUSDT",
            "LITECOIN" : "http://127.0.0.1:5000/LTCUSDT", "RIPPLE" : "http://127.0.0.1:5000/XRPUSDT",
            "CARDANO (ADA)" : "http://127.0.0.1:5000/ADAUSDT", "NEO" : "http://127.0.0.1:5000/NEOUSDT",
            "STELLAR (XLM)" : "http://127.0.0.1:5000/XLMUSDT", "ONTOLOGY" : "http://127.0.0.1:5000/ONTUSDT",
            "CHAINLINK" : "http://127.0.0.1:5000/LINKUSDT", "IOTA" : "http://127.0.0.1:5000/IOTAUSDT", 
            "BASIC ATTENTION COIN" : "http://127.0.0.1:5000/BATUSDT", "BAND PROTOCOL" : "http://127.0.0.1:5000/BANDUSDT", 
            "BELLA PROTOCOL" : "http://127.0.0.1:5000/BELUSDT",
            }

    
class Crypto(Resource):
    def get(self, name):
        coinList = [
            "BTCUSDT","ETHUSDT","BNBUSDT",
            "LTCUSDT","NEOUSDT","XRPUSDT",
            "ADAUSDT","BELUSDT","XLMUSDT",
            "BATUSDT","LINKUSDT","BANDUSDT",
            "ONTUSDT","IOTAUSDT"
            ]
        client = Client()
        dict_result = {}
        
        if name in coinList and name != "BTCUSDT":
            df_predict = pd.DataFrame()
            for i in coinList:
                list_pred = []
                if i == name:
                    continue
                candles = client.get_klines(symbol=i, interval="1h", limit=2)
                list_pred.append(candles[0][4])
                df_predict[i] = list_pred
            model = pickle.load(open("MLBinanceAPI/"+ name, 'rb'))
            result = model.predict(df_predict)[0]
            name_last_value = client.get_klines(symbol=name, interval="1h", limit=2)
            dict_result.update({
                name + " 1 SAATLIK MUM ACILISI" : round(float(name_last_value[1][1]), 3),
                name + " ANLIK DEGER" : round(float(name_last_value[1][4]), 3),
               # "Interval": "1 hour",
                name + " 1 SAATLIK MUM KAPANIS TAHMINI" : round(result, 3)
            })
            return dict_result
        else:
            return {name : "NULL"}

