import matplotlib.pyplot as plt
import pandas as pd

# Crear un DataFrame de ejemplo (sustituye esto por tu lectura de datos)
data = {'anaemia': [1, 0, 1, 0, 1],
        'diabetes': [1, 0, 1, 0, 1],
        'smoking': [1, 0, 1, 0, 1],
        'DEATH_EVENT': [1, 0, 1, 0, 1]}
df = pd.DataFrame(data)

# Eliminar la columna 'categoria_edad'
# df = df.drop(columns=['categoria_edad'])

# Variables de interés
variables = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']

# Valores personalizados para 'anaemia', 'diabetes', 'smoking' y 'DEATH_EVENT'
custom_values = {'anaemia': [53.1, 46.9],
                 'diabetes': [58.0, 42.0],
                 'smoking': [67.9, 32.1],
                 'DEATH_EVENT': [72.8, 27.2]}

# Crear subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
fig.suptitle('Distribuciones de Categorías')

# Iterar sobre las variables y agregar gráficas de torta a cada subplot
for i, variable in enumerate(variables):
    ax = axes[i // 2, i % 2]
    
    # Utilizar los valores personalizados si están definidos
    values = custom_values.get(variable, df[variable].value_counts())
    
    ax.pie(values, labels=['No', 'Si'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
    ax.set_title(f'Distribución de {variable.capitalize()}')

# Ajustes de diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
