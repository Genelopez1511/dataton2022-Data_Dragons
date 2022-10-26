# Este un script de python para visualizar y probar scripts
import pandas as pd 


# Importación de los datasets suministrados

data_clientes = pd.read_csv("dataset/clientes.csv")
data_clientes_noticias = pd.read_csv("dataset/clientes_noticias.csv")
data_noticias = pd.read_csv("dataset/noticias.csv")

print(data_clientes.head(10))