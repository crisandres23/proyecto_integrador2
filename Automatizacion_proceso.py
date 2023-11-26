import sys
import requests
import pandas as pd
import numpy as np

def procesar_datos(url):
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Error al obtener la URL")
        sys.exit()
    
    #df = pd.read_html(response.text)

    nombre_archivo = "datos_procesados.csv"
    with open(nombre_archivo, "w", encoding = "utf-8") as archivo:
        archivo.write(response.text)
    return pd.read_csv(nombre_archivo)
 
def clasificar_datos(df):
    bins =[ 0 , 12, 19, 39, 59, np.inf]
    etiquetas =['niño', 'adolescente', 'adulto_joven', 'adulto', 'adulto_mayor']
    df['categoria_edad'] = pd.cut(df['age'],bins= bins, labels = etiquetas)
    return df

def main():
    
    # Obtener la URL desde los argumentos de la línea de comandos
    url = sys.argv[1]
    print(url)
    df = procesar_datos(url)
    print(df)
    df_convertido = clasificar_datos(df)
    df_convertido.to_csv("datos_procesados_nuevo.csv", index=False)
    
if __name__ == '__main__':
    main()
    