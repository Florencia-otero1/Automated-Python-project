from azure.storage.blob import BlobServiceClient
from datetime import datetime
import os

class DescargaArchivo:
    def __init__(self, connection_string, container_name, directorio_local):
        self.connection_string = connection_string
        self.container_name = container_name
        self.directorio_local = directorio_local
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def obtener_blob_mas_reciente(self):
        
        # busca el blob con la fecha más reciente dentro del container de nombre "eCommerce"

        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            blobs_con_fechas = []

            # obtener lista de blobs y filtrar aquellos con la fecha dentro del nombre
            for blob in container_client.list_blobs():
                blob_nombre = blob.name
                try:
                    fecha_blob = datetime.strptime(blob_nombre[:8], "%Y%m%d")
                    blobs_con_fechas.append((fecha_blob, blob_nombre))
                except ValueError:
                    pass # ignorar archivos sin fecha valida al inicio

            if not blobs_con_fechas:
                print("No se encontraron archivos con fecha valida en el nombre")
                return None


            blobs_con_fechas.sort(reverse=True, key=lambda x: x[0]) # ordenar en orden descendente
            fecha_mas_reciente, blob_mas_reciente = blobs_con_fechas[0]

            print(f"archivo más reciente encontrado: {blob_mas_reciente} con fecha {fecha_mas_reciente}")
            return blob_mas_reciente
        except Exception as e:
            print(f"Ocurrio un error al listar los blobs: {e}")
            return None
        
    def descargar_blob(self, blob_name):
        # descargar el blob especificado y guardarlo en directorio local
        try:
            blob_client = self.blob_service_client.get_blob_client(self.container_name, blob_name)
            ruta_descarga = os.path.join(self.directorio_local, blob_name)

            with open(ruta_descarga, "wb") as archivo_descarga:
                archivo_bytes = blob_client.download_blob().readall()
                archivo_descarga.write(archivo_bytes)

            print(f"Archivo descargado exitosamente a: {ruta_descarga}")
        except Exception as e:
            print(f"Ocurrio un error al descargar el archivo: {e}")
