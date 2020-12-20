# -------------------------------------------------------------------
# Módulo entProcesos.py
# Clase para manejar información de los Procesos del Sistema
# -------------------------------------------------------------------

# Definición de la Clase
class eProcesos:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__ID            = -1
        self.__strProcesoIde = ""
        self.__strProcesoNom = ""
        
    # Setter's y Getter's
    def setID(self,ID):
        self.__ID = ID

    def getID(self):
        return self.__ID

    def setStrProcesoIde(self,procesoIde):
        self.__strProcesoIde = procesoIde

    def getStrProcesoIde(self):
        return self.__strProcesoIde

    def setStrProcesoNom(self,procesoNom):
        self.__strProcesoNom = procesoNom

    def getStrProcesoNom(self):
        return self.__strProcesoNom
    
# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto
    oProcesos = eProcesos()

    # Le coloca datos al objeto; setter's
    oProcesos.setID(10)
    oProcesos.setStrProcesoIde("Login")
    oProcesos.setStrProcesoNom("Acceso al Sistema")
    

    # Desplegando la información; getter's
    print("Agrupar Productos     :",oProcesos.getID())
    print("Bitacora Activa       :",oProcesos.getStrProcesoIde())
    print("Imprimir Ticket       :",oProcesos.getStrProcesoNom())

    