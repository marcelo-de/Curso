# -------------------------------------------------------------------
# Módulo funcArchivo.py
# Constantes, Variables y Funciones con respecto al manejo de archivo
# -------------------------------------------------------------------

# Libreria para verificar existencia del archivo
import os.path
from datetime import datetime

# Librerias utilizadas
import entidades.entGlobales   as eg

# Función para verificar si un archivo existe
def fnArchivoExiste(sArchivo):
    # Llama a la función y retorna si existe
    return os.path.isfile(sArchivo) 

# Crea el Archivo de Log
def fnLogCrea():

    # Actualiza la variable global para indicar que ha sido creado
    eg.eGlobales.bLogCreado = True

    # Fecha de Hoy
    oFechaHoy = datetime.now()

    # Actualiza el Año de Operación global
    eg.eGlobales.AñoOperacion= oFechaHoy.strftime("%Y")    

    # Obtiene la Fecha y hora como cadena
    sFechaHora = oFechaHoy.strftime("%Y_%m_%d_%H_%M_%S")

    # Nombre del archivo Log
    sNombreLog = eg.eGlobales.ARCHIVO_LOG+sFechaHora

    # Crea al archivo de Log
    eg.eGlobales.aLogArchivo = open(sNombreLog, "w")

# Graba un mensaje en el Log
def fnLogGraba(modulo,funcion,tipo,mensaje):
    
    # Verifica que el log esté creado antes de nada
    if (eg.eGlobales.bLogCreado):

        # Obtengo la fecha de hoy
        oFechaHoy = datetime.now()

        # Crea la Variable con la información de time y la graba
        sInformacion = "Time    :"+oFechaHoy.strftime("%Y-%m-%d %H:%M:%S")+"\n"
        eg.eGlobales.aLogArchivo.write(sInformacion)

        # Crea la Variable con la información de Módulo y la graba
        sInformacion = "Modulo  :"+modulo+"\n"
        eg.eGlobales.aLogArchivo.write(sInformacion)

        # Crea la Variable con la informaión de Función y la graba
        sInformacion = "Funcion :"+funcion+"\n"
        eg.eGlobales.aLogArchivo.write(sInformacion)

        # Crea la Variable con la información de Tipo y la graba
        sInformacion = "Tipo    :"+tipo+"\n"
        eg.eGlobales.aLogArchivo.write(sInformacion)    

        # Crea la Variable con la información de Mensaje
        sInformacion = "Mensaje :"+mensaje+"\n\n"
        eg.eGlobales.aLogArchivo.write(sInformacion)    

# Cierra el Log
def fnLogCierra():
    
    # Verifica que el log esté creado antes de nada
    if (eg.eGlobales.bLogCreado):

        # Cierra la variable
        eg.eGlobales.bLogCreado=False
        
        # Cierra el Archivo
        eg.eGlobales.aLogArchivo.close()


# Función main
if __name__ == "__main__":
    
    # Test función de mensaje
    if (fnArchivoExiste("funciones/funcArchivo.py")):
        print("El Archivo Si existe")
    else:
        print("El Archivo No Existe")

    # Crea el ARCHIVO LOG
    print("Creando el Log ...")
    fnLogCrea()

    # Graba algunos mensajes
    print("Grabando en el Log ...")
    fnLogGraba("Sesion","Login","Informativo","Esperando captura de Usuario y Password")
    fnLogGraba("Sesion","Login","Advertencia","Falla en el acceso al Sistema")
    fnLogGraba("Sesion","Login","Error","No se logra conexion al Servidor")

    # Cierra el Archivo
    print("Cerrando el Log ...")
    fnLogCierra()
