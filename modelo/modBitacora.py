# -----------------------------------------------------------------
# Clase mBitacora
# Modelo para controlar información de la tabla Bitácora
# -----------------------------------------------------------------

# Librería para la Fecha Hora
from datetime import datetime

# Importa la libreria globales
import entidades.entGlobales   as eg
import entidades.entBitacora   as eb
import funciones.funcBaseDatos as fbd


# Constantes para las Columnas de la Tabla de Bitácora
INT_COL_FOLIO    = 0
INT_COL_USUARIO  = 1
INT_COL_REGISTRO = 2
INT_COL_PROCESO  = 3
INT_COL_SUCURSAL = 4
INT_COL_TERMINAL = 5

# Definición de la Clase
class mBitacora:

    # Función para insertar un registro en la bitácora
    def fnBitacoraRegistrar(self,proceso):

        # Fecha de Hoy
        oFechaHoy = datetime.now()

        # Prepara el Query para Insertar
        sQuery =  " INSERT INTO bitacora "
        sQuery += " (strUsuarioIde, fecRegistro, strProcesoIde, strSucursal, intTerminal) VALUES"
        sQuery += " ('"+eg.eGlobales.UsuarioIde+"',"
        sQuery += "  '"+oFechaHoy.strftime("%Y-%m-%d %H:%M:%S")+"',"
        sQuery += "  '"+proceso+"',"
        sQuery += "  '"+eg.eGlobales.Sucursal+"',"
        sQuery += "   "+eg.eGlobales.Terminal+")"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,True)

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
    datBitacora = mBitacora()

    # Actualizo el usuario de Ingreseo
    eg.eGlobales.UsuarioIde="jaor"

    # Ejecutando el Registro en la Bitácora
    datBitacora.fnBitacoraRegistrar("Ventas")

    # Realiza commit
    fbd.fnCommit()

    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
