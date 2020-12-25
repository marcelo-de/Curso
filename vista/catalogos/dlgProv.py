#   ------------------------------------------------------------------------------------------------------------
#   ventana funcional llamando a un archivo.ui
#    buscar lo siguiente en youtube.
#  Python Curso V2: 462 2/2 Cargar un Archivo de Interfaz Grafica de Usuario
#   ------------------------------------------------------------------------------------------------------------
    
import sys
from PyQt5.QtWidgets  import QApplication, QMainWindow, QPushButton, QMessageBox, QDialog

from PyQt5 import uic    # es para importar los archivos ui
    

#class Aplicacion(QMainWindow):
class Aplicacion(QDialog):    

    def __init__(self):
        super().__init__()
        self.inicializarGui()
        
    def inicializarGui(self):
        uic.loadUi('vista/catalogos/wPrueba.ui', self)   # el achivo va con la extencion.
            
            # AQUI EL CODIGO         
        self.btn_saludar = self.findChild(QPushButton,'btn_saludar')
        self.btn_saludar.clicked.connect(self.saludar)

        self.show()

    def saludar(self):
        

        
        msg = QMessageBox()
        msg.setWindowTitle("tutorial on Pyqt5")
        msg.setText("Aqui el texto que infoma del problema o la decicion a tomar")
        #msg.setIcon(QMssageBox.Critical)
        #msg.setStandardButton(QMessageBox.Ok | QMessageBox.Cancel|QMessageBox.Ignore)
        #msg.setDefautlButton(QMessageBox.Ignore)
        msg.setInformativeText("Texto informativo en la parte de abajo, Ya!! ")
        msg.setDetailedText("Detales dentro del cuadro de ayuda")    

        msg = msg.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


