# ----------------------------------------------------------------
# Módulo funcXML.py
# Constantes, Variables y Funciones para el Manejo de archivos XML
# ----------------------------------------------------------------

# Se importa la librería para manejo de XML
from xml.dom import minidom

# Importar globales
import entidades.entGlobales as eg

# Función para obtener un dato del Archivo de Inicialización XML
def fnObtenDato(sArchivoXML,sDato):
    
    # Obtengo acceso al Documento
    docXML = minidom.parse(sArchivoXML)

    #Obtengo el dato
    dato = docXML.getElementsByTagName(sDato)[0]

    # Retorno
    return dato.firstChild.data

# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Test obtener datos
    print ("Dato:",fnObtenDato(eg.eGlobales.INICIALIZACION,"servidor"))
