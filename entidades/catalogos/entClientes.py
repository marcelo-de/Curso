# ---------------------------------------------------------------------------
# Clase para la entidad de Clientes
# Para obtener información de la tabla de Clientes
# ---------------------------------------------------------------------------

# Definición de la Clase
class eClientes:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__cliente_id   = -1
        self.__nif          = ""
        self.__tipoIF       = ""
        self.__nombre       = ""
        self.__direccion    = ""
        self.__codigopostal = "" 
        self.__poblacion    = "" 
        self.__provincia    = "" 
        self.__pais         = "" 
        self.__telefono     = "" 
        self.__movil        = "" 
        self.__email        = "" 
        self.__web          = "" 

        
    # Setter's y Getter's
    def setCliente_id(self,cliente_id):
        self.__cliente_id = cliente_id

    def getCliente_id(self):
        return self.__cliente_id

    def setNif(self,nif):
        self.__nif = nif

    def getNif(self):
        return self.__nif

    def setTipoIF(self,tipoIF):
        self.__tipoIF = tipoIF

    def getTipoIF(self):
        return self.__tipoIF

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setDireccion(self,direccion):
        self.__direccion = direccion

    def getDireccion(self):
        return self.__direccion

    def setCodigoPostal(self,codigopostal):
        self.__codigopostal = codigopostal

    def getCodigoPostal(self):
        return self.__codigopostal

    def setPoblacion(self,poblacion):
        self.__poblacion = poblacion

    def getPoblacion(self):
        return self.__poblacion

    def setProvincia(self,provincia):
        self.__provincia = provincia

    def getProvincia(self):
        return self.__provincia

    def setPais(self,pais):
        self.__pais = pais

    def getPais(self):
        return self.__pais

    def setTelefono(self,telefono):
        self.__telefono = telefono

    def getTelefono(self):
        return self.__telefono

    def setMovil(self,movil):
        self.__movil = movil

    def getMovil(self):
        return self.__movil

    def setEmail(self,email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setWeb(self,web):
        self.__web = web

    def getWeb(self):
        return self.__web

# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    ocliente = eClientes()

    # Le coloca datos al objeto; setter's
    ocliente.setCliente_id(10)
    ocliente.setNif("NIF-123123")
    ocliente.setTipoIF("NIE")
    ocliente.setNombre("JAOR")
    ocliente.setDireccion("Conocida")
    ocliente.setCodigoPostal("12345")
    ocliente.setPoblacion("Ciudad de México")
    ocliente.setProvincia("Distrito Federal")
    ocliente.setPais("México")
    ocliente.setTelefono("123-122-9090")
    ocliente.setMovil("281-345-5678")
    ocliente.setEmail("elemail@hotmail.com")
    ocliente.setWeb("www.myweb.com")

    # Desplegando la información; getter's
    print("id        :",ocliente.getCliente_id())
    print("nif       :",ocliente.getNif())
    print("nif tipo  :",ocliente.getTipoIF())
    print("nombre    :",ocliente.getNombre())
    print("dirección :",ocliente.getDireccion())
    print("c postal  :",ocliente.getCodigoPostal())
    print("población :",ocliente.getPoblacion())
    print("provincia :",ocliente.getProvincia())
    print("pais      :",ocliente.getPais())
    print("Teléfono  :",ocliente.getTelefono())
    print("Móvil     :",ocliente.getMovil())
    print("Email     :",ocliente.getEmail())
    print("Web       :",ocliente.getWeb())
    
    