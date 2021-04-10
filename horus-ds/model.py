
from conexion import  colec_vaccdata
import json
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from enum import Enum

cantidad_elementos = colec_vaccdata.count()
colec_dicc = json.loads(colec_vaccdata)
"""resultado = colec_vaccdata.find_one()
print(resultado['dateString'])"""



plt.set_xlabel('Fecha')     
plt.set_ylabel('Vacunados Totales') 



for element in colec_dicc:
    print(element["dateString"])
    for subelement in element:
        print(subelement["data"])
    
"""
def plot(price, ma_20, ma_100, action_price_points):     
    ax = price.plot()     
    
    ma_20.plot(label='Moving Average 20 Days', ax=ax)     
    #ma_100.plot(label='Moving Average 100 Days', ax=ax)     
    
    ax.set_xlabel('Date')     
    ax.set_ylabel('Closing Price')     
    ax.set_title('Caterpillar Inc. Closing Price')     
    ax.legend(loc='upper left')     
    
    for position in action_price_points:         
        plt.scatter(position.date, position.price, s=600, c=position.action.value)     
    
    plt.show()



"""