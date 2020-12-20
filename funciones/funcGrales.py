# -------------------------------------------------------------------
# Módulo funcGrales.py
# Constantes, Variables y Funciones Generales
# -------------------------------------------------------------------

# Importamos la Librería QMessageBox
from PyQt5 import QtWidgets

# Importamos Generales
import entidades.entGlobales   as eg

# Definimos una función desplegar un MessageBox de Información
def fnMensajeInformacion(sMensaje, sInformacion):

    # Crea un MessageBox
    msg = QtWidgets.QMessageBox()

    # Establece el Icomo
    msg.setIcon(QtWidgets.QMessageBox.Information)

    # Coloca el Mensaje a Desplegar
    msg.setText(sMensaje)
    msg.setInformativeText(sInformacion)
    msg.setWindowTitle(eg.eGlobales.SISTEMA)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    
    # Ejecuta el MessageBox
    msg.exec_()
    return

# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtCore, QtGui, QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Test función de mensaje
    fnMensajeInformacion("Titulo","Mensaje","Informacion")
