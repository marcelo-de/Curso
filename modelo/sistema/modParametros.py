# ----------------------------------------------------------------------
# Clase mParametros
# Modelo para actualizar información referente a los parámetros en la BD
# ----------------------------------------------------------------------

# Importa la libreria globales
import entidades.entGlobales           as eg
import entidades.sistema.entParametros as ep
import funciones.funcBaseDatos         as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_MENSAJES_EXITO         = 0
INT_COL_AGRUPAR_PRODUCTOS      = 1
INT_COL_VERIFICAR_EXISTENCIAS  = 2
INT_COL_IMPRIMIR_TICKET        = 3
INT_COL_BITACORA_ACTIVA        = 4
INT_COL_MENSAJE_TICKET         = 5
INT_COL_MONEDA_SIMBOLO         = 6
INT_COL_MONEDA_NOMBRE          = 7

# Definición de la Clase
class mParametros:

    # Función para obtener información de los parámetros
    def fnParametrosGet(self):

        # Crea un objeto de Parametros para retornar
        oParametros = ep.eParametros()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM parametros "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oParametros.setIntMensajesExito(registro[INT_COL_MENSAJES_EXITO])
                oParametros.setIntAgruparProductos(registro[INT_COL_AGRUPAR_PRODUCTOS])
                oParametros.setIntVerificarExistencias(registro[INT_COL_VERIFICAR_EXISTENCIAS])
                oParametros.setIntImprimirTicket(registro[INT_COL_IMPRIMIR_TICKET])
                oParametros.setIntBitacoraActiva(registro[INT_COL_BITACORA_ACTIVA])
                oParametros.setStrMensajeTicket(registro[INT_COL_MENSAJE_TICKET])
                oParametros.setStrMonedaSimbolo(registro[INT_COL_MONEDA_SIMBOLO])
                oParametros.setStrMonedaNombre(registro[INT_COL_MONEDA_NOMBRE])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto oParametros
        return oParametros

    # Función para obtener establecer los valores de la tabla
    def fnParametrosSet(self, oParametros):

        # Prepara el Query para realizar el Update
        sQuery =  " UPDATE parametros SET "
        sQuery += " intMensajesExito        = "+str(oParametros.getIntMensajesExito())+","
        sQuery += " intAgruparProductos     = "+str(oParametros.getIntAgruparProductos())+","
        sQuery += " intVerificarExistencias = "+str(oParametros.getIntVerificarExistencias())+","
        sQuery += " intImprimirTicket       = "+str(oParametros.getIntImprimirTicket())+","
        sQuery += " intBitacoraActiva       = "+str(oParametros.getIntBitacoraActiva())+","
        sQuery += " strMensajeTicket        = '"+str(oParametros.getStrMensajeTicket())+"',"
        sQuery += " strMonedaSimbolo        = '"+str(oParametros.getStrMonedaSimbolo())+"',"
        sQuery += " strMonedaNombre         = '"+str(oParametros.getStrMonedaNombre())+"'"

        # Ejecuta y Retorna
        return fbd.fnExecuteUpdateSql(sQuery, True)



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
    datParametros = mParametros()

    # Declarando un objeto de la entidad Parámetros
    oParametros = ep.eParametros()

    # Ejecutando la Consulta de  Parametros
    oParametros = datParametros.fnParametrosGet()

    # Desplegando los datos
    print("Mensajes Éxito        :",oParametros.getIntMensajesExito())
    print("Agrupar Productos     :",oParametros.getIntAgruparProductos())
    print("Verificar Existencias :",oParametros.getIntVerificarExistencias())
    print("Imprimir Ticket       :",oParametros.getIntImprimirTicket())
    print("Bitácora Activa       :",oParametros.getIntBitacoraActiva())
    print("Mensaje Ticket        :",oParametros.getStrMensajeTicket())
    print("Moneda Símbolo        :",oParametros.getStrMonedaSimbolo())
    print("Moneda Nombre         :",oParametros.getStrMonedaNombre())
    
    # Test de la función de actualizar
    print ("Se realizó la Actualización:",datParametros.fnParametrosSet(oParametros))

    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()