# Importe as bibliotecas necessárias para este projeto
import numpy as np
import pandas as pd
from IPython.display import display # Permite o uso de display() para DataFrames

# Importe o código sumplementar para visualização de visuals.py
#import visuals as vs

# Mostre matplotlib no corpo do texto (bem formatado no Notebook)
#%matplotlib inline

# Carregue o conjunto de dados dos clientes da distribuidora de atacado
data = pd.read_csv("customers.csv")
data.drop(['Region', 'Channel'], axis = 1, inplace = True)
print(data.shape)
print("Wholesale customers dataset has {} samples with {} features each.").format(data.shape())

