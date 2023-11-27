import matplotlib.pyplot as plt
import pandas as pd
# Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)

# Eliminar la columna 'categoria_edad'
df = df.drop(columns=['categoria_edad'])

# Variables de interés
variables = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']

# Crear subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
fig.suptitle('Distribuciones de Categorías')

# Iterar sobre las variables y agregar gráficas de torta a cada subplot
for i, variable in enumerate(variables):
    ax = axes[i // 2, i % 2]
    
    counts = df[variable].value_counts()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
    ax.set_title(f'Distribución de {variable.capitalize()}')

# Ajustes de diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
