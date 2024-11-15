from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
from dotenv import load_dotenv
import sys
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.interaccionWeb import *
from pageObjects.descargaArchivo import *
from pageObjects.registroProceso import *
from pageObjects.config import *
from dotenv import load_dotenv

def main():
    load_dotenv()
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    DIRECTORIO_LOCAL = directorio_local

    descargaArchivo = DescargaArchivo(CONNECTION_STRING,CONTAINER_NAME,DIRECTORIO_LOCAL)
    blob_mas_reciente = descargaArchivo.obtener_blob_mas_reciente()
    if blob_mas_reciente:
        descargaArchivo.descargar_blob(blob_mas_reciente)
   
    # INICIALIZAR EL DRIVER
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url_qa_login)
    user = os.getenv('USUARIO_LOGIN')
    password = os.getenv('CONTRASEÑA_LOGIN')
    
    # INGRESAR A LA PAGINA E IR A MANTENEDOR
    registroP = registroProceso(DIRECTORIO_LOCAL, f"Resultado _{blob_mas_reciente}")
    interaccionW = InteraccionWeb(driver, registroP)
    interaccionW.login(user,password)
    driver.get(url_qa_mantenedor)
    driver.maximize_window()
    time.sleep(5)
    
    # Crear excel para reporte
    registroP.escribir_encabezados()
    #Ingresar nuevo ejecutivo
    #interaccionW.nuevoEjecutivo(f'{DIRECTORIO_LOCAL}/{blob_mas_reciente}')

     # Mantención de roles
    #interaccionW.modificar_roles(f'{DIRECTORIO_LOCAL}/{blob_mas_reciente}')

    # Dar de baja a los ejecutivo
    interaccionW.baja_usuario(f'{DIRECTORIO_LOCAL}/{blob_mas_reciente}')
    #time.sleep(2)
    


    

if __name__ == "__main__":
    main()    
    
    