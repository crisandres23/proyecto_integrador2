from datasets import load_dataset
import numpy as pd

dataset = load_dataset("mstz/heart_failure") # Cargar el dataset
data = dataset["train"]
edades = data["age"]
edades_pd = pd.array(edades)

promedio_edad = pd.mean(edades_pd) # Calcular el promedio de edad directamente desde el arreglo de NumPy
print(f'Promedio de Edad: {promedio_edad}')