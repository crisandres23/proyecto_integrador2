import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

## Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)

# Eliminar la columna objetivo y la columna 'categoria_edad'
X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values

# Crear un array unidimensional para la columna objetivo 'DEATH_EVENT'
y = df['DEATH_EVENT'].values

# Reducción de dimensionalidad con t-SNE
X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

# Crear un DataFrame con los datos reducidos y la columna objetivo
df_embedded = pd.DataFrame(X_embedded, columns=['Dim_1', 'Dim_2', 'Dim_3'])
df_embedded['DEATH_EVENT'] = y

# Graficar de dispersión 3D con Plotly
fig = px.scatter_3d(
    df_embedded,
    x='Dim_1',
    y='Dim_2',
    z='Dim_3',
    color='DEATH_EVENT',
    labels={'color': 'DEATH_EVENT'},
    title='Visualización 3D con t-SNE'
)

# Mostrar el gráfico
fig.show()

