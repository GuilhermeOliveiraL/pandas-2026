#%%
import pandas as pd
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes

#%%
## AMOSTRAS
df_clientes.head(n=10)
# Head pega cabeçalho + primeiras linhas do dataset (n=x, x = quantidade de linhas)

#%%
df_clientes.tail(1)
# tail pega últimas linhas do dataset

#%%
df_clientes.shape
# Pega (qtd. colunas, qtd. linhas)

#%%
df_clientes.columns
# Pega as colunas do df

#%%
df_clientes.sample(5)
# Pega amostra aleatória do DF

#%%
df_clientes.columns
# Pega as colunas do df

#%%
df_clientes.index
# Pega o range de index do DF

#%%
df_clientes.info(memory_usage='deep', max_cols=2)
# pega informaçoes importantes do df

#%%
df_clientes.dtypes["idCliente"]
