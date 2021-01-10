import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic    # es para importar los archivos ui

class dlgProveedoresAC(QDialog):

    def __init__(self):
        super().__init__()        
        self.iniciar_AC()


    def iniciar_AC(self):
        uic.loadUi('ui/dlgProvAC.ui', self)   # el achivo va con la extencion.ui

        self.setWindowTitle("Agregar nuevo Proveedor")
        self.show()




app = QApplication(sys.argv)
UIWindow = dlgProveedoresAC()
app.exec_()        
