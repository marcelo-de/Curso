# ---------------------------------------------------------------------------
# Clase para la entidad de Usuarios
# Para obtener información de la tabla de Usuarios
# ---------------------------------------------------------------------------

# Definición de la Clase
class eUsuarios:

    # Constructor
    def __init__(self):

        # Propiedades correspondientes a las Columnas de la Tabla
        self.__strUsuarioIde   = ""
        self.__strUsuarioPass  = ""
        self.__strUsuarioName  = ""
        self.__strRoleName     = ""

    # Setter's y Getter's
    def setStrUsuarioIde(self,ide):
        self.__strUsuarioIde = ide

    def getStrUsuarioIde(self):
        return self.__strUsuarioIde

    def setStrUsuarioPass(self,password):
        self.__strUsuarioPass = password

    def getStrUsuarioPass(self):
        return self.__strUsuarioPass

    def setStrUsuarioName(self,name):
        self.__strUsuarioName = name

    def getStrUsuarioName(self):
        return self.__strUsuarioName
    
    def setStrRoleName(self,roleName):
        self.__strRoleName = roleName

    def getStrRoleName(self):
        return self.__strRoleName


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un objeto de la Clase
    oUsuario = eUsuarios()

    # Le coloca datos al objeto; setter's
    oUsuario.setStrUsuarioIde("0010101")
    oUsuario.setStrUsuarioName("Jhon")
    oUsuario.setStrUsuarioPass("Rambo")
    oUsuario.setStrRoleName("Mercenario")
    

    # Desplegando la información; getter's
    print("Ide  :",oUsuario.getStrUsuarioIde())
    print("Name :",oUsuario.getStrUsuarioName())
    print("Pass :",oUsuario.getStrUsuarioPass())
    print("Role :",oUsuario.getStrRoleName())
    