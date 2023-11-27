import matplotlib.pyplot as plt
import pandas as pd

# Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)

# Histograma de Edades
plt.figure(figsize=(8, 6))
plt.hist(df['age'], bins=10, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Número de Personas')
plt.show()

# Histogramas agrupados por género
variables = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
gender_labels = ['Hombres', 'Mujeres']

width = 0.35  # Ancho de las barras

for variable in variables:
    plt.figure(figsize=(8, 6))
    print(f'\nDatos para {variable.capitalize()}:')

    for i, gender in enumerate(['male', 'female']):
        subset = df[df['sex'] == gender]
        counts = subset[variable].value_counts()
        print(f'{gender_labels[i]}: {counts}')

        x = range(len(counts))
        plt.bar([pos + i * width for pos in x], counts, width=width, label=gender_labels[i], edgecolor='black')

    plt.title(f'Distribución de {variable.capitalize()} por Género')
    plt.xlabel(f'{variable.capitalize()}')
    plt.ylabel('Número de Personas')
    plt.xticks([pos + width / 2 for pos in x], counts.index)
    plt.legend()
    plt.show()
