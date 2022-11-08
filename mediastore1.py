from pydoc import describe
import pandas as pd
import requests
import json
from datetime import date


#variaveis
Store = 0
Weekly_Sales = 0
linha = 0


df = pd.read_csv("Walmart.csv")

for index, row in df.iterrows():
    Store = row['Store']
    Weekly_Salescsv = row['Weekly_Sales']
    if Store == 1:
        Weekly_Sales = Weekly_Sales + Weekly_Salescsv
        print(Weekly_Sales)
        linha = linha + 1
    else:
        print("Não é store 1")


print (Weekly_Sales/linha)
