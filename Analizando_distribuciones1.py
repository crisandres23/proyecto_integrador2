import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.manifold import TSNE

# Leer el conjunto de datos
df = pd.read_csv("datos_procesados_nuevo.csv")

plt.figure(figsize=(10,5))
plt.hist(df['age'], bins=10, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

condiciones = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
num_condiciones = len(condiciones)
width = 0.35
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(num_condiciones)
color_hombres = 'blue'
color_mujeres = 'red'
for i, condicion in enumerate(condiciones):
    hombres = df[(df['sex'] == 1) & (df[condicion] == 1)].shape[0]
    mujeres = df[(df['sex'] == 0) & (df[condicion] == 1)].shape[0]
    ax.bar(x[i] - width/2, hombres, width, color=color_hombres, label='Hombres' if i == 0 else "")
    ax.bar(x[i] + width/2, mujeres, width, color=color_mujeres, label='Mujeres' if i == 0 else "")

ax.set_xlabel('Categoria')
ax.set_ylabel('Cantidad')
ax.set_title('Histograma agrupado por Sexo')
ax.set_xticks(x)
ax.set_xticklabels(condiciones)
ax.legend()
plt.show()