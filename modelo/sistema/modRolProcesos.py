# -----------------------------------------------------------------
# Clase mRolProcesos
# Modelo para obtener información referente a RolProcesos
# -----------------------------------------------------------------

# Importa las librerias
import entidades.entGlobales            as eg
import entidades.sistema.entRolProcesos as erp
import funciones.funcBaseDatos          as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_ROLE_NAME   = 0
INT_COL_PROCESO_IDE = 1

# Definición de la Clase
class mRolProcesos:

    # Función para obtener si un role tiene acceso a un proceso
    def fnBoolRolProcesoAcceso(self, role, proceso):

        # Se retornará verdadero o falso
        resultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM rolprocesos "
        sQuery += " WHERE strRoleName   = '"+role+"'"
        sQuery += " AND   strProcesoIde = '"+proceso+"'"

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount > 0):

                # Cambia el Valor a True
                resultado = True

        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return resultado

    # Función para obtener los roles
    def fnRolesListaGet(self):

        # Objeto lista a devolver
        lstRoles = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT DISTINCT(strRoleName) FROM rolprocesos "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                sRol =""

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                sRol = registro[0]

                # Agrega el Proceso a la Lista
                lstRoles.append(sRol)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstRoles

    # Función para obtener los Procesos de un Rol
    def fnProcesosListaGetByRol(self, rol):

        # Objeto lista a devolver
        lstProcesos = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT strProcesoIde FROM rolprocesos "
        sQuery += " WHERE  strRoleName ='"+rol+"'"

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                sProceso =""

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                sProceso = registro[0]

                # Agrega el Proceso a la Lista
                lstProcesos.append(sProceso)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstProcesos

    # Función para eliminar rol-procesos
    def fnRolProcesosDel(self, rol):

        # Prepara el Query para Eliminar
        sQuery =  " DELETE FROM rolprocesos "
        sQuery += " WHERE  strRoleName = '"+rol+"'"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función que verifica que el usuario exista
    def fnBoolRolProcesoExiste(self,rol,proceso):

        # Crea variable de resultado
        bResultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT strRoleName FROM rolprocesos "
        sQuery += " WHERE  strRoleName    = '"+rol+"'"
        sQuery += " AND    strProcesoIde  = '"+proceso+"'"
        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Cambia la variable de Resultado
                bResultado= True
                
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return bResultado

    # Función para insertar un Rol-Procesos
    def fnRolProcesoIns(self,rol,proceso):

        # Prepara el Query para Actualizar
        sQuery =  " INSERT INTO rolprocesos "
        sQuery += " (strRoleName,strProcesoIde) VALUES"
        sQuery += " ('"+rol+"',"
        sQuery += "  '"+proceso+"')"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)
        

# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Conectando al Servidor
    print("Conectando al Servidor ...")
    fbd.fnConexionServidor()

    # Declarando un objeto del Modelo
    datRolProcesos = mRolProcesos()

    # Ejecutando la Consulta para verifica si un rol tiene acceso a un proceso
    if (datRolProcesos.fnBoolRolProcesoAcceso("supervisor","Clientes")):
        # Mensaje
        print("El Role supervisor si tiene acceso al Proceso Clientes")
    else:
        # Mensaje
        print("El Role supervisor no tiene acceso al Proceso Clientes")    

    # Ejecutando la Consulta para verifica si un rol tiene acceso a un proceso
    if (datRolProcesos.fnBoolRolProcesoAcceso("supervisor","Importaciones")):
        # Mensaje
        print("El Role supervisor si tiene acceso al Proceso Importaciones")
    else:
        # Mensaje
        print("El Role supervisor no tiene acceso al Proceso Importaciones")        
    print("---------------")

    # Desplegando la lista de los Roles Disponibles
    listaRoles = datRolProcesos.fnRolesListaGet()

    # Despliega cada uno de ellos
    for sRol in listaRoles:
        print(sRol)
    print("---------------")
    
    # Desplegando la lista de Procesos por Rol
    listaProcesos = datRolProcesos.fnProcesosListaGetByRol("supervisor")

    # Despliega cada uno de ellos
    for sProceso in listaProcesos:
        print(sProceso)

    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()















