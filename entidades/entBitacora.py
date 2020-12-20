# ---------------------------------------------------------------------------
# Clase para la entidad de Bitacora
# Para control de información de la tabla de Bitácora
# ---------------------------------------------------------------------------

# Definición de la Clase
class eBitacora:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__intFolio      = 0
        self.__strUsuarioIde = ""
        self.__fecRegistro   = ""
        self.__strProcesoIde = ""
        self.__strSucursal   = ""
        self.__intTerminal   = ""
        
    # Setter's y Getter's
    def setIntFolio(self,folio):
        self.__intFolio = folio

    def getIntFolio(self):
        return self.__intFolio

    def setStrUsuarioIde(self,usuarioIde):
        self.__strUsuarioIde = usuarioIde

    def getStrUsuarioIde(self):
        return self.__strUsuarioIde

    def setFecRegistro(self,fecRegistro):
        self.__fecRegistro= fecRegistro

    def getFecRegistro(self):
        return self.__fecRegistro

    def setStrProcesoIde(self,procesoIde):
        self.__strProcesoIde = procesoIde

    def getStrProcesoIde(self):
        return self.__strProcesoIde

    def setStrSucursal(self,sucursal):
        self.__strSucursal = sucursal

    def getStrSucursal(self):
        return self.__strSucursal

    def setIntTerminal(self,terminal):
        self.__intTerminal = terminal

    def getIntTerminal(self):
        return self.__intTerminal


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys
    from datetime import datetime

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oBitacora = eBitacora()

    # Obtenemos la fecha de hoy
    xFechaHoy = datetime.now()

    # Le coloca datos al objeto; setter's
    oBitacora.setIntFolio(1)
    oBitacora.setStrUsuarioIde("jaor")
    oBitacora.setFecRegistro(xFechaHoy.strftime("%Y-%m-%d %H:%M:%S"))
    oBitacora.setStrProcesoIde("Ventas")
    oBitacora.setStrSucursal("Matriz")
    oBitacora.setIntTerminal(5)

    # Desplegando la información; getter's
    print("Folio     :",oBitacora.getIntFolio())
    print("Usuario   :",oBitacora.getStrUsuarioIde())
    print("Fecha     :",oBitacora.getFecRegistro())
    print("Proceso   :",oBitacora.getStrProcesoIde())
    print("Sucursal  :",oBitacora.getStrSucursal())
    print("Terminal  :",oBitacora.getIntTerminal())
    