# -------------------------------------------------------------------
# Módulo entParametros.py
# Clase para manejar información de Parámetros del Sistema
# -------------------------------------------------------------------

# Definición de la Clase
class eParametros:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__intMensajesExito        = -1
        self.__intAgruparProductos     = -1
        self.__intVerificarExistencias = -1
        self.__intImprimirTicket       = -1
        self.__intBitacoraActiva       = -1
        self.__strMensajeTicket        = ""
        self.__strMonedaSimbolo        = ""
        self.__strMonedaNombre         = ""

        
    # Setter's y Getter's
    def setIntMensajesExito(self,mensajeExito):
        if (mensajeExito<0 or mensajeExito>1):
            print("Error al asignar el Mensaje de Exito:",mensajeExito, "; valores posibles:0,1")
        else:    
            self.__intMensajesExito = mensajeExito

    def getIntMensajesExito(self):
        return self.__intMensajesExito

    def setIntAgruparProductos(self,agruparProductos):
        if (agruparProductos<0 or agruparProductos>1):
            print("Error al asignar Agrupar Productos:",agruparProductos, "; valores posibles:0,1")
        else:    
            self.__intAgruparProductos = agruparProductos

    def getIntAgruparProductos(self):
        return self.__intAgruparProductos

    def setIntVerificarExistencias(self,verificarExistencias):
        if (verificarExistencias<0 or verificarExistencias>1):
            print("Error al asignar Verificar Existencias:",verificarExistencias, "; valores posibles:0,1")
        else:    
            self.__intVerificarExistencias = verificarExistencias

    def getIntVerificarExistencias(self):
        return self.__intVerificarExistencias

    def setIntImprimirTicket(self,imprimirTicket):
        if (imprimirTicket<0 or imprimirTicket>1):
            print("Error al asignar Imprimir Ticket:",imprimirTicket, "; valores posibles:0,1")
        else:    
            self.__intImprimirTicket = imprimirTicket

    def getIntImprimirTicket(self):
        return self.__intImprimirTicket

    def setIntBitacoraActiva(self,bitacoraActiva):
        if (bitacoraActiva<0 or bitacoraActiva>1):
            print("Error al asignar Bitácora Activa:",bitacoraActiva, "; valores posibles:0,1")
        else:
            self.__intBitacoraActiva = bitacoraActiva

    def getIntBitacoraActiva(self):
        return self.__intBitacoraActiva

    def setStrMensajeTicket(self,mensajeTicket):
        if (len(mensajeTicket) > 40):
            print("Error al asignar Mensaje Ticket:",mensajeTicket, "; longitud máxima 40 caracteres")
        else:
            self.__strMensajeTicket = mensajeTicket

    def getStrMensajeTicket(self):
        return self.__strMensajeTicket

    def setStrMonedaSimbolo(self,monedaSimbolo):
        if (len(monedaSimbolo) > 1):
            print("Error al asignar Moneda Símbolo:",monedaSimbolo, "; longitud máxima 1 caracteres")
        else:
            self.__strMonedaSimbolo = monedaSimbolo

    def getStrMonedaSimbolo(self):
        return self.__strMonedaSimbolo

    def setStrMonedaNombre(self,monedaNombre):
        if (len(monedaNombre) > 10):
            print("Error al asignar Moneda Nombre:",monedaNombre, "; longitud máxima 10 caracteres")
        else:
            self.__strMonedaNombre = monedaNombre

    def getStrMonedaNombre(self):
        return self.__strMonedaNombre
    
# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oParametros = eParametros()

    # Le coloca datos al objeto; setter's
    oParametros.setIntAgruparProductos(1)
    oParametros.setIntBitacoraActiva(1)
    oParametros.setIntImprimirTicket(1)
    oParametros.setIntMensajesExito(1)
    oParametros.setIntVerificarExistencias(1)
    oParametros.setStrMensajeTicket("! Felices Fiestas !")
    oParametros.setStrMonedaNombre("Pesos M.N.")
    oParametros.setStrMonedaSimbolo("$")
    

    # Desplegando la información; getter's
    print("Agrupar Productos     :","Sí" if (oParametros.getIntAgruparProductos()==1) else "No")
    print("Bitacora Activa       :","Sí" if (oParametros.getIntBitacoraActiva()==1) else "No")
    print("Imprimir Ticket       :","Sí" if (oParametros.getIntImprimirTicket()==1) else "No")
    print("Mensajes Éxito        :","Sí" if (oParametros.getIntMensajesExito()==1) else "No")
    print("Verificar Existencias :","Sí" if (oParametros.getIntVerificarExistencias()==1) else "No")
    print("Mensaje Ticket        :",oParametros.getStrMensajeTicket())
    print("Moneda Nombre         :",oParametros.getStrMonedaNombre())
    print("Moneda Simbolo        :",oParametros.getStrMonedaSimbolo())

    