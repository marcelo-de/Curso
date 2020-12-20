# ------------------------------------------------------------------
# Módulo funcBaseDatos.py
# Constantes, Variables y Funciones para el Manejo de Bases de Datos
# ------------------------------------------------------------------

# Librería de mysql
# pip install mysql-conector
import mysql.connector

# Importamos las librerias propietarias
import entidades.entGlobales as eg
import funciones.funcArchivo as fa
import funciones.funcXML     as fx
import funciones.funcGrales  as fg


# Función para conectarse a mySql
def fnConexionServidor():
    
    # Grabamos en el Log
    fa.fnLogGraba("funcBaseDatos","fnConexionServidor","Informativo","Verificando archivo de Inicialización")

    # Verifico que el archivo exista
    if (fa.fnArchivoExiste(eg.eGlobales.INICIALIZACION)):

        # Obteniendo los datos del Archivo de Inicializacion
        servidor = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"servidor")
        usuario  = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"usuario")
        password = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"password").rstrip()
        database = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"database")
        sucursal = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"sucursal")
        terminal = fx.fnObtenDato(eg.eGlobales.INICIALIZACION,"terminal")       
        
        # Captura Errores
        try:
        
            # Creamos una conexión e intentamos conectar
            eg.gConnMySql = mysql.connector.connect(host     = servidor, 
                                                    user     = usuario, 
                                                    passwd   = password,
                                                    database = database)
        
            # Coloca los datos eg del Sistema
            eg.eGlobales.Sucursal=sucursal
            eg.eGlobales.Terminal=terminal

            # Retorna verdadero
            return True

        # Captura del Error    
        except mysql.connector.errors.InterfaceError as err:
            
            # Despliega el Mensaje de Error
            print(err.msg)
            fg.fnMensajeInformacion("Error en Conexión a MySql",err.msg)
            return False

        except mysql.connector.errors.ProgrammingError as err:
            # Despliega el Mensaje de Error por Usuario y Clave
            fg.fnMensajeInformacion("Error en Usuario-Clave",err.msg)
            return False

        except mysql.connector.Error as err:  
            # Despliega el Mensaje de Error
            fg.fnMensajeInformacion("Error al Conectar al Servidor:",err.msg)
            return False     

    else:
        # Despliega mensaje de que no existe archivo de Inicialización
        fg.fnMensajeInformacion("Error en Archivo de Inicialización",mysql.connector.errors)
        return False

# Función para cerrar la Conexión
def fnConexionCerrar():

    # Grabando en el Log
    fa.fnLogGraba("funcBaseDatos","fnConexionCerrar","Informativo","Cerrando la Conexión al Servidor")

    # Cierra la Conexión
    eg.gConnMySql.close()

    

# Función para ejecutar Consultas
def fnExecuteSql(sQuery):
    
    # Creo el Cursor para Consultas
    eg.gCursor = eg.gConnMySql.cursor(buffered=True)

    # Captura el Error
    try:
        # Ejecuta la Consulta con el Cursor
        eg.gCursor.execute(sQuery)

        # Hace commit
        eg.gConnMySql.commit()

        # Retorna Verdadero
        return True

    # Captura el Error    
    except mysql.connector.errors.ProgrammingError as err:
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnExecuteSql:Error al Ejecutar Query:"+sQuery,err.msg)
        return False    

    except mysql.connector.Error as err:  
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnExecuteSql:Error al Ejecutar Query:"+sQuery,err.msg)
        return False    
    

# Función para ejecutar Updates
def fnExecuteUpdateSql(sQuery, realizarCommit):
    
    # Creo el Cursor para Consultas
    eg.gCursor = eg.gConnMySql.cursor(buffered=True)

    # Captura el Error
    try:
        # Ejecuta la Consulta con el Cursor
        eg.gCursor.execute(sQuery)

        # Verifica si debe realizar commit
        if (realizarCommit):
            # Hace un commit de la actualización
            eg.gConnMySql.commit()

        # Retorna Verdadero
        return True

    # Captura el Error    
    except mysql.connector.errors.ProgrammingError as err:
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnExecuteUpdateSql:Error al Ejecutar Query:"+sQuery,err.msg)
        return False    

    except mysql.connector.Error as err:  
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnExecuteUpdateSql:Error al Ejecutar Query:"+sQuery,err.msg)
        return False    


# Función para ejecutar Commit
def fnCommit():
    
    # Captura el Error
    try:
        # Hace un commit de la actualización
        eg.gConnMySql.commit()

        # Retorna Verdadero
        return True
  

    except mysql.connector.Error as err:  
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnCommit:",err.msg)
        return False        

# Función para obtener el ultimo id insertado
def fnLastInsertId():

    # variable resultado
    resultado = -1

    # Prepara el Query para Actualizar
    sQuery =  " SELECT last_insert_id()"

    # Intenta Ejecuta la Sentencia de
    if (fnExecuteSql(sQuery)):

        # Verifica que haya habido resultados
        if (eg.gCursor.rowcount>0):

                # Lee el Registro
            registro = eg.gCursor.fetchone()

            # Coloca los datos en el objeto
            resultado =registro[0]
            
    # Cierra el Cursor
    eg.gCursor.close()
    
    # Retorna el Objeto Usuario
    return resultado

# Función para ejecutar Callback
def fnRollback():
    
    # Captura el Error
    try:
        # Hace un rollbak de la actualización
        eg.gConnMySql.rollback()

        # Retorna Verdadero
        return True 

    except mysql.connector.Error as err:  
        # Despliega el Mensaje de Error
        fg.fnMensajeInformacion("fnRollback:",err.msg)
        return False    


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Test Conexion a BD
    print("Conectando al Servidor ...")
    if (fnConexionServidor()):

        #Test la Consulta
        print ("Ejecutando consulta de la tabla de usuarios ...")
        fnExecuteSql("SELECT * FROM usuarios")

        # Imprime registros encontrados
        print("Registros encontrados:",eg.gCursor.rowcount)

        print("Desplegando los registros de la tabla de usuarios")
        # Ciclo para desplegar los datos obtenidos
        while True:
        
            # Lee el Registro
            registro = eg.gCursor.fetchone()

            # Verifica si ya no hay registros
            if (registro is None):
                # Sale del ciclo
                break
            
            # Imprime        
            print(registro)    


        # Cierra el Cursor
        print("Cerrando Cursor ...")
        eg.gCursor.close()

        # Obteniendo el ultimo insert
        print("Ultimo Insert:",fnLastInsertId())

        # Cierra la Conexión
        print("Cerrando Conexión ...")
        fnConexionCerrar()