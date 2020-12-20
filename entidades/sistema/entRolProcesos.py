# ---------------------------------------------------------------------------
# Clase para la entidad de RolProcesos
# Para obtener información de la tabla de rolprocesos
# ---------------------------------------------------------------------------

# Definición de la Clase
class eRolProcesos:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__strRoleName   = ""
        self.__strProcesoIde = ""
        
    # Setter's y Getter's
    def setStrRoleName(self,rol):
        self.__strRoleName = rol

    def getStrRoleName(self):
        return self.__strRoleName

    def setStrProcesoIde(self,proceso):
        self.__strProcesoIde = proceso

    def getStrProesoIde(self):
        return self.__strProcesoIde


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oRolProceso = eRolProcesos()

    # Le coloca datos al objeto; setter's
    oRolProceso.setStrRoleName("supervisor")
    oRolProceso.setStrProcesoIde("Clientes")
    

    # Desplegando la información; getter's
    print("Rol     :",oRolProceso.getStrRoleName())
    print("Proceso :",oRolProceso.getStrProesoIde())
    