# -----------------------------------------------------------------
# Clase mProcesos
# Modelo para obtener información referente a Procesos
# -----------------------------------------------------------------

# Importa las librerias
import entidades.entGlobales            as eg
import entidades.sistema.entProcesos    as ep
import funciones.funcBaseDatos          as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_ID          = 0
INT_COL_PROCESO_IDE = 1
INT_COL_PROCESO_NOM = 2

# Definición de la Clase
class mProcesos:

    # Función para obtener los Procesos
    def fnListaProcesosGet(self):

        # Objeto lista a devolver
        lstProcesos = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM procesos "
        sQuery += " WHERE  ID > 0"
        sQuery += " AND    ID < 99"

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                oProceso = ep.eProcesos()

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                oProceso.setID(registro[INT_COL_ID])
                oProceso.setStrProcesoIde(registro[INT_COL_PROCESO_IDE])
                oProceso.setStrProcesoNom(registro[INT_COL_PROCESO_NOM])

                # Agrega el Proceso a la Lista
                lstProcesos.append(oProceso)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstProcesos
        

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
    datRolProcesos = mProcesos()

    # Obtiene la lista de Procesos
    listaProcesos = datRolProcesos.fnListaProcesosGet()

    # Imprime la lista de Procesos
    for oProceso in listaProcesos:
        print(oProceso.getID(),oProceso.getStrProcesoIde(),oProceso.getStrProcesoNom())

    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()















