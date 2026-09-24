#%%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
p = [1, 20, 90, 70, 0, 80, 4]
filtro=[]

for ps in p:
    filtro.append(ps>=50)

resultado=[]

for ps in range(len(p)):
    if filtro[ps]:
        resultado.append(p[ps])

resultado.sort()
resultado

#%%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = pd.Series([True, False, True])
#filtro = brinquedo["idade"] >= 18
brinquedo[filtro]

#%%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

#%%
filtro = df["QtdePontos"] >= 50
df = df[filtro]
df

#%%
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] >= 100)
df[filtro]

# E = & ou *
#%%
filtro =  (df["QtdePontos"] < 10) | (df["QtdePontos"] >= 90) & (df["QtdePontos"] <= 100)
df[filtro]

# OU = |