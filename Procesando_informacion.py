import requests

#crear la funcion descargar_datos
def descargar_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        #abrir el archivo datos.csv
        with open('datos.csv', 'w') as archivo:
            archivo.write(response.text)
        print("Los datos han sido descargados y guardados como datos.csv")
    else:
        print("No se pudo descargar los datos. Código de respuesta:", response.status_code)

# llamar a la funcion descargar_datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
descargar_datos(url_datos)