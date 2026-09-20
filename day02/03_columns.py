#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

#%%
df.shape

#%%
df.info(memory_usage='deep')

#%%
df.dtypes

#%%
renamed_columns = {
    "IdTransacao":"idTrans",
    "DescSistemaOrigem":"SistemaOrigem",
    "IdCliente": "idCliente"
}

df.rename(columns=renamed_columns, inplace=True)

#%%
df[["idCliente", "QtdePontos", ]]

#%%
df[["idCliente","SistemaOrigem", "QtdePontos"]].sample(n=5)

#%%
colunas = df.columns.to_list()
colunas.sort()
colunas

df = df[colunas]