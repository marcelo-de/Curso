# ---------------------------------------------------------------------------
# Clase para la entidad de Provedores
# Para obtener información de la tabla de Proveedores
# ---------------------------------------------------------------------------

# Definición de la Clase
class eProveedores:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__proveedor_id = -1
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
    def setProveedor_id(self,proveedor_id):
        self.__proveedor_id = proveedor_id

    def getProveedor_id(self):
        return self.__proveedor_id

    def setNif(self,nif):
        self.__nif = nif

    def getNif(self):
        return self.__nif

    def setTipoIF(self,nifTipo):
        self.__nifTipo = nifTipo

    def getTipoIF(self):
        return self.__nifTipo

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
    oProveedor = eProveedores()

    # Le coloca datos al objeto; setter's
    oProveedor.setProveedor_id(10)
    oProveedor.setNif("NIF-123123")
    oProveedor.setTipoIF("NIE")
    oProveedor.setNombre("JAOR")
    oProveedor.setDireccion("Conocida")
    oProveedor.setCodigoPostal("12345")
    oProveedor.setPoblacion("Ciudad de México")
    oProveedor.setProvincia("Distrito Federal")
    oProveedor.setPais("México")
    oProveedor.setTelefono("123-122-9090")
    oProveedor.setMovil("281-345-5678")
    oProveedor.setEmail("elemail@hotmail.com")
    oProveedor.setWeb("www.myweb.com")

    # Desplegando la información; getter's
    print("id        :",oProveedor.getProveedor_id())
    print("nif       :",oProveedor.getNif())
    print("nif tipo  :",oProveedor.getTipoIF())
    print("nombre    :",oProveedor.getNombre())
    print("dirección :",oProveedor.getDireccion())
    print("c postal  :",oProveedor.getCodigoPostal())
    print("población :",oProveedor.getPoblacion())
    print("provincia :",oProveedor.getProvincia())
    print("pais      :",oProveedor.getPais())
    print("Teléfono  :",oProveedor.getTelefono())
    print("Móvil     :",oProveedor.getMovil())
    print("Email     :",oProveedor.getEmail())
    print("Web       :",oProveedor.getWeb())
    
    