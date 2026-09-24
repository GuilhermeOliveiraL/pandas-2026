#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes
# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()

clientes_0["flag_1"] = 1
clientes_0

# válido apenas pra 2.3.3, inválido a partir da 3.0