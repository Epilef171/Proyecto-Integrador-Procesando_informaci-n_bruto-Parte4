import requests
import csv

def descargar_y_guardar_csv(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            archivo_csv.write(response.text)

        print(f"Descarga y guardado exitoso en {nombre_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")


