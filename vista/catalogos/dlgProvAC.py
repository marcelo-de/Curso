import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic    # es para importar los archivos ui

class dlgProveedorAC(QDialog):

    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("ui/dlgProvAC.ui", self)
        self.setWindowTitle("Modificacion de Proveedores")
        self.show()




app = QApplication(sys.argv)
UIWindow = dlgProveedorAC()
app.exec_()        
