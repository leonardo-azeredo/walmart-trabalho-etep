from pydoc import describe
import pandas as pd
from datetime import date


#variaveis
Store = 0
Weekly_Sales = 0
linha = 0
loja = int(input('Número da loja: '))

df = pd.read_csv("Walmart.csv")

for index, row in df.iterrows():
    Store = row['Store']
    Weekly_Salescsv = row['Weekly_Sales']
    if Store == loja:
        Weekly_Sales = Weekly_Sales + Weekly_Salescsv
        print(Weekly_Sales)
        linha = linha + 1   

arquivo = open("media.txt" , "w+")

print ("Media da loja" , Weekly_Sales/linha , file=arquivo)