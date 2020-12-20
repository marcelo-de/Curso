# ---------------------------------------------------------------------------
# Clase para la entidad de Empresa
# Para obtener información de la tabla de Empresa
# ---------------------------------------------------------------------------

# Definición de la Clase
class eEmpresa:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__strEmpresaNombre    = ""
        self.__strEmpresaDireccion = ""
        self.__strEmpresaTelefono  = ""
        self.__strEmpresaRfc       = ""
        self.__strEmpresaSerial    = ""
        self.__strEmpresaLogo      = "" # Se cambio a indicar la Ruta

        
    # Setter's y Getter's
    def setStrEmpresaNombre(self,empresaNombre):
        self.__strEmpresaNombre = empresaNombre

    def getStrEmpresaNombre(self):
        return self.__strEmpresaNombre

    def setStrEmpresaDireccion(self,empresaDireccion):
        self.__strEmpresaDireccion = empresaDireccion

    def getStrEmpresaDireccion(self):
        return self.__strEmpresaDireccion

    def setStrEmpresaTelefono(self,empresaTelefono):
        self.__strEmpresaTelefono = empresaTelefono

    def getStrEmpresaTelefono(self):
        return self.__strEmpresaTelefono

    def setStrEmpresaRfc(self,empresaRfc):
        self.__strEmpresaRfc = empresaRfc

    def getStrEmpresaRfc(self):
        return self.__strEmpresaRfc

    def setStrEmpresaSerial(self,empresaSerial):
        self.__strEmpresaSerial = empresaSerial

    def getStrEmpresaSerial(self):
        return self.__strEmpresaSerial
    
    def setStrEmpresaLogo(self,empresaLogo):
        self.__strEmpresaLogo = empresaLogo

    def getStrEmpresaLogo(self):
        return self.__strEmpresaLogo


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oEmpresa = eEmpresa()

    # Le coloca datos al objeto; setter's
    oEmpresa.setStrEmpresaNombre("SuperAhorros")
    oEmpresa.setStrEmpresaDireccion("Conocida en el Centro")
    oEmpresa.setStrEmpresaTelefono("271-271-7717")
    oEmpresa.setStrEmpresaRfc("SPAR121212")
    oEmpresa.setStrEmpresaSerial("Demo")
    oEmpresa.setStrEmpresaLogo("img/logo.png")

    

    # Desplegando la información; getter's
    print("Nombre    :",oEmpresa.getStrEmpresaNombre())
    print("Direccion :",oEmpresa.getStrEmpresaDireccion())
    print("Teléfono  :",oEmpresa.getStrEmpresaTelefono())
    print("Rfc       :",oEmpresa.getStrEmpresaRfc())
    print("Serial    :",oEmpresa.getStrEmpresaSerial())
    print("Logo      :",oEmpresa.getStrEmpresaLogo())
    
    