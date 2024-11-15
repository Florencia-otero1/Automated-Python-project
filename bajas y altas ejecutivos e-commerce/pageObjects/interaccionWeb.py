from datetime import datetime
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from pageObjects.config import *

class InteraccionWeb:
    # elementos para login
    __tbx_email = (By.XPATH, '//*[@id="mat-input-0"]')
    __btn_continuar_login = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-login/div/div/div/div[1]/div[1]/ml-login/div[2]/mat-card/div[3]/p/at-button/at-basic-button/button')
    __tbx_password = (By.XPATH, '//*[@id="mat-input-2"]')
    __btn_ingresar_login = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-login/div/div/div/div[1]/div[1]/ml-login/div[2]/mat-card/div[3]/p/at-button/at-basic-button/button')

    # elementos para bajas
    __tbx_ingresar_correo = (By.XPATH, '//*[@id="mat-input-0"]')
    __tbx_ingresar_correo_fullxpath = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/grid-admin/div[1]/div[1]/div[2]/div[1]/mat-form-field/div/div[1]/div[1]/input')                                        
    __btn_ingresar3puntitos = (By.XPATH, '//*[@id="icon-actions"]')
    __btn_desactivar = (By.XPATH, '//span[contains(text(),"Desactivar ejecutivo")]')
    __btn_llenar_campo_fecha = (By.XPATH,'/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/dialog-grid[1]/div[1]/div[1]/div[2]/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]')
    __btn_cancelar = (By.XPATH,'/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/dialog-grid[1]/div[1]/div[1]/div[2]/div[4]/div[2]/button[1]')
    __btn_confirmar_baja = (By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/dialog-grid/div/div/div[2]/div[4]/div[1]/button')                                        

    # elementos para cambios de roles
    __btn_asignar_o_modificar_rol = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/button[1]/span')
    __cbx_roles = (By.XPATH, "/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-roles-user/div/div/div[3]/div/div[1]/mat-checkbox/label/span[1]/input")                            
    __cbx_roles_click = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-roles-user/div/div/div[3]/div[1]/div[1]/mat-checkbox/label/span[1]')                                    
    __cbx_roles_2 = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-roles-user/div/div/div[3]/div[2]/div[1]/mat-checkbox/label/span[1]/input')
    __cbx_roles_click_2 = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-roles-user/div/div/div[3]/div[2]/div[1]/mat-checkbox/label/span[1]')
     
          
    # elementos para nuevos ejecutivos
    __btn_ingresar_nuevo_ejecutivo = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/grid-admin/div[1]/div[1]/div[2]/div[3]/button')             
    __tbx_formulario_correo = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[1]/at-input/mat-form-field/div/div[1]/div[1]/input')  
    __tbx_formulario_rut = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[2]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_nombre = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[3]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_apellido_1 = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[4]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_apellido_2 = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[5]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_fecha_nacimiento = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[6]/at-input/mat-form-field/div/div[1]/div[1]/input') 
    __tbx_formulario_numero = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[8]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_correo_jefe = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-data-user/div/div/div/form/div/div[9]/at-input/mat-form-field/div/div[1]/div[1]/div/input')
    __btn_formulario_continuar = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[3]/button')
    __tbx_formulario_ingresar_rol = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-roles-user/div/div/mat-form-field/div/div[1]/div[1]/input')
    __btn_formulario_continuar_2 = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[3]/button')
    __tbx_formulario_fecha_activacion = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-summary-user/div/div/div[4]/form/div/div[2]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __tbx_formulario_fecha_desactivacion = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[2]/step-summary-user/div/div/div[4]/form/div/div[4]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __btn_formulario_confirmar_agente = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-user/div/div/div/div/div[3]/button')
    
         
    def __init__(self, driver: WebDriver, registro_proceso):
        self.driver = driver
        self.registro_proceso = registro_proceso

    def login(self, usuario: str, contraseña: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_email)).send_keys(usuario)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_continuar_login)).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_password)).send_keys(contraseña)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_ingresar_login)).click()
        time.sleep(5)

    def nuevoEjecutivo(self, file_path):
        # Abre el excel dado en el filepath y busca la hoja Altas
        df = pd.read_excel(file_path, sheet_name='Altas')
        # itera segun la cantidad de filas que hay
        for index, row in df.iterrows():
            try:
                #actualiza el driver (para resolver error que se daba al no encontraba el boton nuevo ejecutivo)
                self.driver.get(url_qa_mantenedor)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_ingresar_nuevo_ejecutivo)).click()        
                time.sleep(5)
                #envia la info del excel a su casilla correspondiente en el formulario de ingreso
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_correo)).send_keys(row['Correo'])            
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_rut)).send_keys(row['RUT'])
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_nombre)).send_keys(row['Nombre'])        
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_apellido_1)).send_keys(row['Apellido 1'])
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_apellido_2)).send_keys(row['Apellido 2'])
                fecha = pd.to_datetime(row['Fecha nacimiento'], dayfirst=True).strftime('%d/%m/%Y')                
                print(fecha)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_nacimiento)).send_keys(fecha)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_numero)).send_keys(row['Teléfono (Sin +56)'])            
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_correo_jefe)).send_keys(row['Correo del Jefe'])
                time.sleep(3)
                btn_continuar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_continuar))
                # centra la pantalla en el boton continuar
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_continuar)
                time.sleep(1)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_continuar)).click()
                time.sleep(2)                
            except Exception as e:
                print("Error al llenar los datos del formulario")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="alta", 
                        correo=row['Correo'], 
                        rut=row['RUT'], 
                        estado_ejecucion=estado_ejecucion,
                        error = "Error en los datos personales requeridos en el formulario de ingreso de nuevo ejecutivo"
                )
                continue

            try:
                # llamada metodo asignar roles
                self.asignar_roles(row)  
                btn_continuar_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_continuar_2))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_continuar_2)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_continuar_2)).click()
                time.sleep(2)
            except Exception as e:
                print ("Error al ingresar los roles")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="alta", 
                        correo=row['Correo'], 
                        rut=row['RUT'], 
                        estado_ejecucion=estado_ejecucion,
                        error = "Error en la asignación de roles para el nuevo ejecutivo"
                )
                continue

            try:                
                # se asigna el valor a la fecha segun lo que viene en el excel
                fecha_actual = datetime.now().strftime('%d/%m/%Y')
                fecha_activacion_usuario = row['Fecha de Activación']          
                fecha_desactivacion_usuario = row['Fecha de desactivación']
                # Si fecha activación viene vacio le asignamos la fecha actual, ya que no puede ser nulo
                if pd.isna(row["Fecha de Activación"]) or fecha_activacion_usuario == '':
                    fecha_activacion_usuario = fecha_actual                   
                # Si la fecha de activación no es nulo                  
                if not pd.isna(fecha_activacion_usuario):
                    try:
                        # Intenta agregar los guiones a la fecha de activación
                        fecha_activacion_usuario = row['Fecha de Activación'].strftime('%d/%m/%Y')
                    except:
                        # Si no puede se deja como esta (aqui entra cuando no se puede hacer el strftime, el unico caso que cumple esto es cuando ya viene con ese formato)
                        fecha_activacion_usuario = fecha_activacion_usuario
                    # Limpia el formulario fecha de activación                    
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_activacion)).clear()
                    # Otra forma de limpiar el campo si la primera no funciona
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_activacion)).send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                    time.sleep(2)
                    # Envia la fecha de activación
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_activacion)).send_keys(fecha_activacion_usuario)
                    time.sleep(2)
                    tbx_fecha_desactivacion = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__tbx_formulario_fecha_desactivacion))
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", tbx_fecha_desactivacion)
                    time.sleep(1)
                    WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_desactivacion)).click()
                    # Si la fecha de desactivación no es nulo hace lo mismo que arriba (en este caso la fecha de desactivación si puede ser nulo)
                if not pd.isna(row['Fecha de desactivación']):
                    fecha_desactivacion_usuario = row["Fecha de desactivación"].strftime('%d/%m/%Y')
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_desactivacion)).clear()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_desactivacion)).send_keys(Keys.CONTROL,'a',Keys.BACKSPACE)
                    time.sleep(2)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__tbx_formulario_fecha_desactivacion)).send_keys(fecha_desactivacion_usuario)
                time.sleep(2)
                # Creamos la variable btn_confirmar_agente para poder aplicar la función JS.
                btn_confimar_agente = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_confirmar_agente))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_confimar_agente)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_confimar_agente)).click()
                time.sleep(5)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_ingresar_nuevo_ejecutivo))
                # Si llega hasta aqui es porque logro realizar la carga, por lo que se escribe en el excel que fue cargado
                estado_ejecucion = "Cargado"
            except Exception as e:
                print(f"Error en la fecha de activación o desactivación")               
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="alta", 
                        correo=row['Correo'], 
                        rut=row['RUT'], 
                        estado_ejecucion=estado_ejecucion,
                        error = "Error en la fecha de activación o desactivación"
                )
                continue
            self.registro_proceso.escribir_resultado(
                    tipo_operacion="alta", 
                    correo=row['Correo'], 
                    rut=row['RUT'], 
                    estado_ejecucion=estado_ejecucion,                    
                    error = ""
            )


    def asignar_roles(self, row):
        # los campos vacios les escribe "" (para evitar error de NAN)
        row = row.fillna('')
        for i in range(1, 30):  # Para roles 1 a 29            
            # le asigna a rol lo que viene en la casilla rol, le quita los espacios y la deja en mayuscula            
            rol = str(row[f'Rol{i}']).strip().upper()                                               
            if rol != "":
                # Envia el rol en la barra de buscador de rol, a fin de que solo aparezca el elemento que coincide con ese rol
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).send_keys(rol)                               
                btn_rol = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles_click))
                # Obtiene los atributos aria-checked y name, a fin de comprobar si la casilla esta marcada y si el nombre corresponde al rol enviado
                isChecked = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("aria-checked")                
                nombre_rol = WebDriverWait(self.driver , 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("name")
                # Se inicializan las variables en caso de que la primera casilla no sea el rol que buscamos, esto ya que se da el caso que en algunas busquedas
                # textuales aparece un rol antes que el que buscamos (ejemplo: al buscar asesor, el primer checkbox que aparece es asesor_test y el segundo checkbox es asesor)
                btn_rol_2 = None
                isChecked_2 = None
                nombre_rol_2 = None
                # intenta obtener la segunda casilla, si no puede es porque no existe                
                try:                    
                    btn_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_click_2))
                    isChecked_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("aria-checked")
                    nombre_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("name")
                except:
                    print("no existe el boton rol 2...")
                print(nombre_rol)
                print(isChecked)
                # Si el aria-checked es false y el name coincide con el string del rol, lo apreta                
                if isChecked == 'false' and nombre_rol == str(rol):
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol)  
                    time.sleep(1)                                 
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol)).click()
                    time.sleep(2)
                # Si no entra al primer if significa que hay otro checkbox antes, por lo que comprueba la casilla isChecked y name del segundo checkbox
                elif isChecked_2 == 'false' and nombre_rol_2 == rol:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol_2)  
                    time.sleep(1)                                 
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol_2)).click()
                    time.sleep(2)
                # Si ninguna de las 2 coincide significa que la casilla no existe (o que aparecia 3ra al buscar el rol)
                else:                    
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                    time.sleep(1)   
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                time.sleep(1)
            # Si la casilla rol viene vacia, salta a la siguiente fila
            else:
                break
            

                 
    
    def verificar_datos_en_pagina(self, fila):
        self.driver.get(url_qa_mantenedor)
        #print(f"Procesando fila: {fila}")  # Imprime la fila para depurar    
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_ingresar_correo)).click()    
        time.sleep(3)    # Verificar si hay correo en la columna correspondiente    
        correo = fila.iloc[0] if pd.notna(fila.iloc[0]) else None    
        rut = fila.iloc[1] if pd.notna(fila.iloc[1]) else None    # Si el correo existe, lo escribe; si no, escribe el RUT    
        campo_a_escribir = self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')    
        campo_a_escribir.clear()    
        if correo:
            campo_a_escribir.send_keys(correo)            
        elif rut:
            campo_a_escribir.send_keys(rut)
        else:        
            print("No se encontró ni correo ni RUT en esta fila.")    
            time.sleep(3)

    def abrir_menu_3puntitos(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_ingresar3puntitos)).click()    
        time.sleep(1)

    def desactivar_usuario(self):    
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_desactivar)).click()    
        time.sleep(2)
    def confirmar_baja(self):
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable(self.__btn_confirmar_baja)).click()
        time.sleep(2)

    def llenar_campo_fecha(self, fila):
        """
        Llena el campo de fecha con la fecha de la fila o con la fecha actual si no hay valor en la fila.
        """
        # Intenta obtener la fecha de la columna; si es NaT o vacío, usa la fecha actual
        fecha_fila = fila.get("Fecha de desactivación")
        
        # Verifica si fecha_fila es una cadena; si es así, conviértela a un objeto datetime
        if isinstance(fecha_fila, str):
            try:
                fecha_fila = datetime.strptime(fecha_fila, '%d/%m/%Y')
            except ValueError:
                print(f"Error al convertir la fecha: {fecha_fila}")
                return        
        # Si la fecha es NaT o None, usa la fecha actual
        if pd.isnull(fecha_fila):
            fecha_fila = datetime.now()        
        # Formatea la fecha como cadena en el formato 'D/M/AAAA' sin ceros iniciales
        fecha_fila_str = f"{fecha_fila.day}/{fecha_fila.month}/{fecha_fila.year}"        
        # Espera y hace clic en el botón para abrir el campo de fecha
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_llenar_campo_fecha)).click()
        time.sleep(3)        
        # Define el campo de fecha en el formulario y envía la fecha formateada
        campo_fecha = (By.XPATH, '/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/dialog-grid[1]/div[1]/div[1]/div[2]/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(campo_fecha)).send_keys(fecha_fila_str)
        time.sleep(2)

    def cancelar_baja(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_cancelar)).click()
        time.sleep(3)
    
    def baja_usuario(self, file_path):
        df = pd.read_excel(file_path, sheet_name="Bajas")
        for index, row in df.iterrows():
            try:                
                self.verificar_datos_en_pagina(row)
                self.abrir_menu_3puntitos()
                self.desactivar_usuario()
                self.llenar_campo_fecha(row)                
                self.confirmar_baja()                
                estado_ejecucion = "Cargado"
            except Exception as e:
                print(f"No se pudo generar la baja en la fila {index + 1}: {e}")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="baja", 
                        correo=row['Correo'], 
                        rut=row['RUT'], 
                        estado_ejecucion=estado_ejecucion,
                        error = "No se pudo generar la baja."
                    )
                continue
            self.registro_proceso.escribir_resultado(
                    tipo_operacion="baja", 
                    correo=row['Correo'],
                    rut=row['RUT'],
                    estado_ejecucion=estado_ejecucion,
                    error = ""
            )
    def tipo_carga(self, row):
         # los campos vacios les escribe "" (para evitar error de NAN)
        row = row.fillna('')
        for i in range(1, 30):  # Para roles 1 a 29
            # Lee la casilla tipo carga
            tipoCarga = row['Tipo Carga']
            if tipoCarga == "Alta":
                    # le asigna a rol lo que viene en la casilla rol, le quita los espacios y la deja en mayuscula            
                rol = str(row[f'Rol{i}']).strip().upper()                                               
                if rol != "":
                    # Envia el rol en la barra de buscador de rol, a fin de que solo aparezca el elemento que coincide con ese rol
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).send_keys(rol)                               
                    btn_rol = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles_click))
                    # Obtiene los atributos aria-checked y name, a fin de comprobar si la casilla esta marcada y si el nombre corresponde al rol enviado
                    isChecked = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("aria-checked")                
                    nombre_rol = WebDriverWait(self.driver , 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("name")
                    # Se inicializan las variables en caso de que la primera casilla no sea el rol que buscamos, esto ya que se da el caso que en algunas busquedas
                    # textuales aparece un rol antes que el que buscamos (ejemplo: al buscar asesor, el primer checkbox que aparece es asesor_test y el segundo checkbox es asesor)
                    btn_rol_2 = None
                    isChecked_2 = None
                    nombre_rol_2 = None
                    # intenta obtener la segunda casilla, si no puede es porque no existe                
                    try:                    
                        btn_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_click_2))
                        isChecked_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("aria-checked")
                        nombre_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("name")
                    except:
                        print("no existe el boton rol 2...")
                    print(nombre_rol)
                    print(isChecked)
                    # Si el aria-checked es false y el name coincide con el string del rol, lo apreta                
                    if isChecked == 'false' and nombre_rol == str(rol):
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol)  
                        time.sleep(1)                                 
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol)).click()
                        time.sleep(2)
                    # Si no entra al primer if significa que hay otro checkbox antes, por lo que comprueba la casilla isChecked y name del segundo checkbox
                    elif isChecked_2 == 'false' and nombre_rol_2 == rol:
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol_2)  
                        time.sleep(1)                                 
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol_2)).click()
                        time.sleep(2)
                    # Si ninguna de las 2 coincide significa que la casilla no existe (o que aparecia 3ra al buscar el rol)
                    else:                    
                        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                        time.sleep(1)   
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                    time.sleep(1)
                # Si la casilla rol viene vacia, salta a la siguiente fila
                else:
                    break
            elif tipoCarga == "Baja":
                # le asigna a rol lo que viene en la casilla rol, le quita los espacios y la deja en mayuscula            
                rol = str(row[f'Rol{i}']).strip().upper()                                               
                if rol != "":
                    # Envia el rol en la barra de buscador de rol, a fin de que solo aparezca el elemento que coincide con ese rol
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).send_keys(rol)                               
                    btn_rol = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles_click))
                    # Obtiene los atributos aria-checked y name, a fin de comprobar si la casilla esta marcada y si el nombre corresponde al rol enviado
                    isChecked = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("aria-checked")                
                    nombre_rol = WebDriverWait(self.driver , 10).until(EC.presence_of_element_located(self.__cbx_roles)).get_attribute("name")
                    # Se inicializan las variables en caso de que la primera casilla no sea el rol que buscamos, esto ya que se da el caso que en algunas busquedas
                    # textuales aparece un rol antes que el que buscamos (ejemplo: al buscar asesor, el primer checkbox que aparece es asesor_test y el segundo checkbox es asesor)
                    btn_rol_2 = None
                    isChecked_2 = None
                    nombre_rol_2 = None
                    # intenta obtener la segunda casilla, si no puede es porque no existe                
                    try:                    
                        btn_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_click_2))
                        isChecked_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("aria-checked")
                        nombre_rol_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__cbx_roles_2)).get_attribute("name")
                    except:
                        print("no existe el boton rol 2...")
                    print(nombre_rol)
                    print(isChecked)
                    # Si el aria-checked es false y el name coincide con el string del rol, lo apreta                
                    if isChecked == 'true' and nombre_rol == str(rol):
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol)  
                        time.sleep(1)                                 
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol)).click()
                        time.sleep(2)
                    # Si no entra al primer if significa que hay otro checkbox antes, por lo que comprueba la casilla isChecked y name del segundo checkbox
                    elif isChecked_2 == 'true' and nombre_rol_2 == rol:
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_rol_2)  
                        time.sleep(1)                                 
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_rol_2)).click()
                        time.sleep(2)
                    # Si ninguna de las 2 coincide significa que la casilla no existe (o que aparecia 3ra al buscar el rol)
                    else:                    
                        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                        time.sleep(1)   
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_formulario_ingresar_rol)).clear()
                    time.sleep(1)
                # Si la casilla rol viene vacia, salta a la siguiente fila
                else:
                    break

            

            
    def modificar_roles(self, path_file):
        # Lee la hoja Carga Masiva de Roles en el archivo del path_file
        df = pd.read_excel(path_file, sheet_name='Carga Masiva de Roles')
        # Itera 1 vez por cada fila en la hoja
        for index,row in df.iterrows():
            try:
                # Llama al metodo que busca al usuario por su correo
                self.verificar_datos_en_pagina(row)
                # Abre el menu para apretar boton de modificar rol
                self.abrir_menu_3puntitos()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_asignar_o_modificar_rol)).click()
                time.sleep(2)
                # Llama al metodo asignar_roles, que asigna los roles segun la fila que esta leyendo
                self.tipo_carga(row)
                time.sleep(2)
                # Navega por el resto del formulario para confirmar la carga de roles
                btn_formulario_continuar_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_continuar_2))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", btn_formulario_continuar_2)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_continuar_2)).click()
                time.sleep(2)
                btn_confimar_agente = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_formulario_confirmar_agente))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_confimar_agente)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(btn_confimar_agente)).click()
                time.sleep(3)
                # Si logra llegar hasta aqui, es porque la carga fue realizada con exito
                estado_ejecucion = "Cargado"
            except Exception as e:
                # Si entra aqui es porque la carga se cayo en alguno de sus pasos. Se marca como No Cargado en el excel
                print(f"No se pudo realizar la modificación de roles en la fila {index + 1}: {e}")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado_modificacion(
                        tipo_operacion="cambio de rol", 
                        correo=row['Correo'], 
                        rut=row['RUT'], 
                        estado_ejecucion=estado_ejecucion,
                        tipo_modificacion= row['Tipo Carga'],
                        error = "Error en la modificación de los roles, ¿Ingresaron un rol que no existe?"
                )
                continue
            
            self.registro_proceso.escribir_resultado_modificacion(
                    tipo_operacion="cambio de rol", 
                    correo=row['Correo'], 
                    rut=row['RUT'], 
                    estado_ejecucion=estado_ejecucion,
                    tipo_modificacion= row['Tipo Carga'],
                    error = ""
            )
            





        
    

        
    



        
        