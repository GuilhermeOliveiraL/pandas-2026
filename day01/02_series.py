#%%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

media = sum(idades) / len(idades)

diffs = 0

for i in idades:
    diffs += (i - media)**2

variancia = diffs / (len(idades)-1)


print(f'Média: {media}')
print(f'Variância: {variancia}')

#%%
#%%

# Uma Series é uma sequência de valores rotulados por um índice. 
# Podem guardar dados do tipos diferentes, mas converte-os para o mesmo tipo.

import pandas as pd

series_idades = pd.Series(idades)
series_idades

#%%
# Métodos das Series

media_idades = series_idades.mean()
var_idades = media_idades.var()
summary_idades = series_idades.describe()


print(f'Média: {media_idades}')
print(f'Variância: {var_idades}')

print(f'Resumo: {summary_idades}')