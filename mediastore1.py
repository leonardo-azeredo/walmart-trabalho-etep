from pydoc import describe
import pandas as pd
from datetime import date


#variaveis
Store = 0
Weekly_Sales = 0
linha = 0
Temperature = 0
Fuel_Price = 0
Holiday_Flag = 0
CPI = 0 
Unemployment = 0
loja = int(input('Número da loja: '))


df = pd.read_csv("Walmart.csv")

for index, row in df.iterrows():
    Store = row['Store']
    Weekly_Salescsv = row['Weekly_Sales']
    Temperaturecsv = row['Temperature']
    Fuel_Pricecsv = row ["Fuel_Price"]
    Holiday_Flagcsv = row ['Holiday_Flag']
    CPIcsv = row ['CPI']
    Unemploymentcsv = row ['Unemployment']
    
    if Store == loja:
        Weekly_Sales = Weekly_Sales + Weekly_Salescsv
        Temperature = Temperature + Temperaturecsv
        Fuel_Price = Fuel_Price + Fuel_Pricecsv
        Holiday_Flag = Holiday_Flag + Holiday_Flagcsv
        CPI = CPI + CPIcsv 
        Unemployment = Unemployment + Unemploymentcsv
        linha = linha + 1   

arquivo = open("media.txt" , "w+")

#salva a resposta do script em um arquivo txt

print (f"Media de vendas da loja {loja}" , round(Weekly_Sales/linha , 2) , "Media de temperatura em F " , 
round(Temperature/linha , 2 ), "Media de preco da gasolina" , round(Fuel_Price/linha , 2) ,
 "Numero de feriados" , Holiday_Flag, "Media do CPI" , round(CPI/linha , 2 ) , 
 "Media Unemployment" , round(Unemployment/linha , 2) , file=arquivo)