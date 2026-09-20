#%%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

series_idades = pd.Series(idades)
series_idades
#%%
series_idades
#%%
idades[0]

#%%
series_idades[0]

#%%
series_idades = series_idades.sort_values()

#%%
# O iloc (Integer Location) acessa pela posição física (0ª, 1ª, 2ª... linha), 
# ignorando o valor do índice.

series_idades.iloc[0]

#%%
series_idades.iloc[::-1]

#%%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades, index=indexs)
series_idades

#%%
series_idades.loc["Téo"]

# iloc = Integer Location → acessa pela posição (0ª, 1ª, 2ª... linha).
# loc = Label Location → acessa pelo índice (label/rótulo da linha).