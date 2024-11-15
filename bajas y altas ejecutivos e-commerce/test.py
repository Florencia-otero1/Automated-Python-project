from azure.storage.blob import BlobServiceClient
import os
from datetime import datetime

# Configuración de acceso
CONNECTION_STRING = ""  # cadena de conexión privada
CONTAINER_NAME = ""  # nombre del contenedor privado
DIRECTORIO_LOCAL = r"" # directorio local


def obtener_blob_mas_reciente():
    try:
        # Conectar al servicio de blobs
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        blobs_con_fechas = []

        # Obtener lista de blobs y filtrar por aquellos con fecha válida al inicio del nombre
        for blob in container_client.list_blobs():
            blob_nombre = blob.name
            try:
                # Extraer la fecha del inicio del nombre (formato YYYYMMDD)
                fecha_blob = datetime.strptime(blob_nombre[:8], "%Y%m%d")
                blobs_con_fechas.append((fecha_blob, blob_nombre))
            except ValueError:
                pass  # Ignorar archivos sin fecha válida al inicio

        # Verificar si se encontraron archivos con fechas válidas
        if not blobs_con_fechas:
            print("No se encontraron archivos con fecha válida en el nombre.")
            return None

        # Ordenar blobs por fecha y obtener el más reciente
        blobs_con_fechas.sort(reverse=True, key=lambda x: x[0])  # Orden descendente
        fecha_mas_reciente, blob_mas_reciente = blobs_con_fechas[0]

        print(f"Archivo más reciente encontrado: {blob_mas_reciente} con fecha {fecha_mas_reciente}")
        return blob_mas_reciente

    except Exception as e:
        print(f"Ocurrió un error al listar los blobs: {e}")
        return None

def descargar_blob(blob_name):
    try:
        # Crear el cliente del servicio Blob
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(CONTAINER_NAME, blob_name)

        # Descargar el blob
        ruta_descarga = f"{DIRECTORIO_LOCAL}\\{blob_name}"
        with open(ruta_descarga, "wb") as archivo_descarga:
            archivo_bytes = blob_client.download_blob().readall()
            archivo_descarga.write(archivo_bytes)

        print(f"Archivo descargado exitosamente a: {ruta_descarga}")

    except Exception as e:
        print(f"Ocurrió un error al descargar el archivo: {e}")

blob_mas_reciente = obtener_blob_mas_reciente()
if blob_mas_reciente:
    descargar_blob(blob_mas_reciente)