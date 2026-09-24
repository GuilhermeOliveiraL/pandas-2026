#%%
import pandas as pd

#%%
df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df.info()

#%%
filtro = (df["IdProduto"] == "5") | (df["IdProduto"] == "11")
df[filtro]

#%%
filtro = df["IdProduto"].isin(["5","11"])
df[filtro]

#%%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

#%%
clientes[~clientes["DtCriacao"].notna()]


# isin = lista de condiçoes positivas de um valor
# isna = quando for nulo
# notna = quando nao for nulo
# ~ = negação