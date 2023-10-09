from datasets import load_dataset
import numpy as np
import pandas as pd

dataset = load_dataset("mstz/heart_failure") # Cargar el dataset
data = dataset["train"]

edades = data["age"]
edades_pd = np.array(edades)
promedio_edad = np.mean(edades_pd) # Calcular el promedio de edad directamente desde el arreglo de NumPy
print(f'Promedio de Edad: {promedio_edad}')

df = pd.DataFrame(data)
personas_perecidas = df[df["is_dead"] == 1]
personas_vivas = df[df["is_dead"] != 1]

promedio_edad_perecidas = personas_perecidas["age"].mean()
promedio_edad_vivas = personas_vivas["age"].mean()

print(df)

tipos_de_datos = df.dtypes
print(tipos_de_datos)


cantidad_fumadores = df.groupby('is_male')['is_smoker'].sum()
print(cantidad_fumadores)
