# ---------------------------------------------------------------------------
# Clase para la entidad de Productos
# Para obtener información de la tabla de Productos
# ---------------------------------------------------------------------------

# Definición de la Clase
class eProductos:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__intProductoIde         = -1
        self.__strProductoCodigo      = ""
        self.__tipoProducto           = ""
        self.__strProductoMarca       = ""
        self.__strProductoNombre      = ""
        self.__strProductoDescripcion = "" 
        self.__strProductoMedida      = "" 
        self.__intProductoInicial     = -1 
        self.__intProductoEntradas    = -1 
        self.__intProductoSalidas     = -1 
        self.__intProductoActual      = -1
        self.__decProductoCosto       = -1.0 
        self.__decProductoPrecio      = -1.0 
        self.__impuesto_id            = -1
        self.__proveedor_id           = -1
        
    # Setter's y Getter's
    def setIntProductoIde(self,intProductoIde):
        self.__intProductoIde = intProductoIde

    def getIntProductoIde(self):
        return self.__intProductoIde

    def setStrProductoCodigo(self,strProductoCodigo):
        self.__strProductoCodigo = strProductoCodigo

    def getStrProductoCodigo(self):
        return self.__strProductoCodigo

    def setTipoProducto(self,tipoProducto):
        self.__tipoProducto = tipoProducto

    def getTipoProducto(self):
        return self.__tipoProducto

    def setStrProductoMarca(self,strProductoMarca):
        self.__strProductoMarca = strProductoMarca

    def getStrProductoMarca(self):
        return self.__strProductoMarca

    def setStrProductoNombre(self,strProductoNombre):
        self.__strProductoNombre = strProductoNombre

    def getStrProductoNombre(self):
        return self.__strProductoNombre

    def setStrProductoDescripcion(self,strProductoDescripcion):
        self.__strProductoDescripcion = strProductoDescripcion

    def getStrProductoDescripcion(self):
        return self.__strProductoDescripcion

    def setStrProductoMedida(self,strProductoMedida):
        self.__strProductoMedida = strProductoMedida

    def getStrProductoMedida(self):
        return self.__strProductoMedida

    def setIntProductoInicial(self,intProductoInicial):
        self.__intProductoInicial = intProductoInicial

    def getIntProductoInicial(self):
        return self.__intProductoInicial

    def setIntProductoEntradas(self,intProductoEntradas):
        self.__intProductoEntradas = intProductoEntradas

    def getIntProductoEntradas(self):
        return self.__intProductoEntradas

    def setIntProductoSalidas(self,intProductoSalidas):
        self.__intProductoSalidas = intProductoSalidas

    def getIntProductoSalidas(self):
        return self.__intProductoSalidas

    def setIntProductoActual(self,intProductoActual):
        self.__intProductoActual = intProductoActual

    def getIntProductoActual(self):
        return self.__intProductoActual

    def setDecProductoCosto(self,decProductoCosto):
        self.__decProductoCosto = decProductoCosto

    def getDecProductoCosto(self):
        return self.__decProductoCosto
        
    def setDecProductoPrecio(self,decProductoPrecio):
        self.__decProductoPrecio = decProductoPrecio

    def getDecProductoPrecio(self):
        return self.__decProductoPrecio

    def setImpuesto_id(self,impuesto_id):
        self.__impuesto_id = impuesto_id

    def getImpuesto_id(self):
        return self.__impuesto_id

    def setProveedor_id(self,proveedor_id):
        self.__proveedor_id = proveedor_id

    def getProveedor_id(self):
        return self.__proveedor_id


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oProducto = eProductos()

    # Le coloca datos al objeto; setter's
    oProducto.setIntProductoIde(10)
    oProducto.setStrProductoCodigo("1231231233")
    oProducto.setTipoProducto("CERVEZAS")
    oProducto.setStrProductoMarca("Corona")
    oProducto.setStrProductoNombre("Coronita 350")
    oProducto.setStrProductoDescripcion("Coronita Botella 350 m.l. no retornable")
    oProducto.setStrProductoMedida("Pza")
    oProducto.setIntProductoInicial(200)
    oProducto.setIntProductoEntradas(23)
    oProducto.setIntProductoSalidas(2)
    oProducto.setIntProductoActual(221)
    oProducto.setDecProductoCosto(12.34)
    oProducto.setDecProductoPrecio(24.00)
    oProducto.setImpuesto_id(5)
    oProducto.setProveedor_id(7)

    # Desplegando la información; getter's
    print("Ide          :",oProducto.getIntProductoIde())
    print("Codigo       :",oProducto.getStrProductoCodigo())
    print("Tipo         :",oProducto.getTipoProducto())
    print("Marca        :",oProducto.getStrProductoMarca())
    print("Nombre       :",oProducto.getStrProductoNombre())
    print("Descripción  :",oProducto.getStrProductoDescripcion())
    print("Medida       :",oProducto.getStrProductoMedida())
    print("Inicial      :",oProducto.getIntProductoInicial())
    print("Entradas     :",oProducto.getIntProductoEntradas())
    print("Salidas      :",oProducto.getIntProductoSalidas())
    print("Actual       :",oProducto.getIntProductoActual())
    print("Costo        :",oProducto.getDecProductoCosto())
    print("Precio       :",oProducto.getDecProductoPrecio())
    print("Impuesto     :",oProducto.getImpuesto_id())
    print("Proveedor    :",oProducto.getProveedor_id())
    
    
    