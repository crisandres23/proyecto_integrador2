import requests
import pandas as pd
def procesar_datos(dataframe):
    # Verificar valores faltantes
    if dataframe.isnull().sum().sum() > 0:
        dataframe = dataframe.dropna()
        print("Se eliminaron las filas con valores faltantes.")
    # Verificar filas repetidas
    if dataframe.duplicated().sum() > 0:
        dataframe = dataframe.drop_duplicates()
        print("Se eliminaron las filas duplicadas.")
    # Detección y eliminación de valores atípicos (agrega tu lógica aquí)
    # Verificar si la columna 'Edad' existe en el DataFrame
    if 'age' in dataframe.columns:
        # Crear columna de categoría de edades
        dataframe['Categoria_edad'] = pd.cut(dataframe['age'], bins=[0, 12, 19, 39, 59, float('inf')], labels=['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor'])
        print("Se creó la columna 'Categoria_edad'.")
    else:
        print("La columna 'Edad' no existe en el DataFrame.")
    # Guardar resultado como CSV (especifica una ruta de archivo significativa)
    dataframe.to_csv('datos_procesados.csv', index=False)
    print("Los datos procesados han sido guardados como datos_procesados.csv")

# Leer el archivo CSV descargado
dataframe = pd.read_csv('datos.csv')
# Llamar a la función para procesar los datos
procesar_datos(dataframe)

