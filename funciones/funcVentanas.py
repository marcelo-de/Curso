# ----------------------------------------------------------------------
# funcVentanas.py
# Archivo de Clases para Ventanas
# ---------------------------------------------------------------------
# Importamos librerías de PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Librería de Sistema
import sys, ctypes, threading

# Función que retorna ancho y alto de la pantalla
def fnDimensionesPantalla():
    # Carga la dll
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return (ancho,alto)

def fnCentrarVentana(ventana):
    # Obtiene el Ancho y alto de la Ventana
    ancho, alto = fnDimensionesPantalla()

    # Calcula el Left y Top de la Ventana para centrarl
    left = (ancho - ventana.width)  / 2
    top  = (alto  - ventana.height) / 2

    # Mueve al centro
    ventana.left = left
    ventana.top = top
    ventana.move(left,top)

# Se define la Clase mensajeCentrado
class mensajeCentrado(QtWidgets.QDialog):

    # El Constructor
    def __init__(self, mensaje, segundos=5):
        
        # Ejecuta el Constructor de la Ventana Padre
        super().__init__()

        # Dimensiones de la Ventana
        self.top = 0
        self.left = 0
        self.width = 500
        self.height = 50

        # Segundos a Esperar
        self.segundos = segundos

        # Define las Dimensiones de la ventana
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Bandera para que no aparezaca el Título
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Coloca la Bandera
        self.setWindowFlags(flags)

        # Crea el LineEdit para el Mensaje y lo agrega a la Ventana
        self.leMensaje = QtWidgets.QLineEdit(self)
        self.leMensaje.setText(mensaje)
        self.leMensaje.setReadOnly(True)
        self.leMensaje.setGeometry(QtCore.QRect(0, 0, 500, 50))
        self.leMensaje.setAlignment(QtCore.Qt.AlignCenter)

        # Paleta para el Color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        
        # Establece la paleta al Mensaje
        self.leMensaje.setPalette(palette)

        # Define la Fuente
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)

        # Establece la Fuente al Mensaje
        self.leMensaje.setFont(font)

        # Obtiene el tamaño de la Pantalla
        self.ancho,self.alto = fnDimensionesPantalla()

        # Centra la Ventana antes de Mostrarla
        fnCentrarVentana(self)
        
        # Muestra la Ventana  
        self.show()

        # Inicial el timer indicando los segundos y función a ejecutar
        threading.Timer(self.segundos,self.fnCierraVentana).start() 

        #Ejecuta el Loop
        self.exec_()

    # Función que detiene el timer
    def fnCierraVentana(self):
        # Cierra la ventana
        self.close()
        
# Se define la Clase mensajeEmergente 
class mensajeEmergente(QtWidgets.QDialog):

    # El Constructor
    def __init__(self, mensaje, desplazamiento=50, velocidad=25, espera = 100):
        
        # Ejecuta el Constructor de la Ventana Padre
        super().__init__()

        # Obtiene los valores de desplazamiento y velocidad
        self.desplazamiento = desplazamiento
        self.velocidad = velocidad
        self.espera = espera

        # Bandera de si está apareciendo
        self.apareciendo = True

        # Dimensiones de la Ventana
        self.top = 0
        self.left = 0
        self.width = 500
        self.height = 50

        # Define las Dimensiones de la ventana
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Bandera para que no aparezaca el Título
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Coloca la Bandera
        self.setWindowFlags(flags)

        # Crea el LineEdit para el Mensaje y lo agrega a la Ventana
        self.leMensaje = QtWidgets.QLineEdit(self)
        self.leMensaje.setText(mensaje)
        self.leMensaje.setReadOnly(True)
        self.leMensaje.setGeometry(QtCore.QRect(0, 0, 500, 50))
        self.leMensaje.setAlignment(QtCore.Qt.AlignCenter)

        # Paleta para el Color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        
        # Establece la paleta al Mensaje
        self.leMensaje.setPalette(palette)

        # Define la Fuente
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)

        # Establece la Fuente al Mensaje
        self.leMensaje.setFont(font)

        # Obtiene el tamaño de la Pantalla
        self.ancho,self.alto = fnDimensionesPantalla()

        # Calcula la posición del tope de la Ventana
        self.topeTop = self.alto-self.height

        # Calcula la posición final de Desplamiento
        self.topeLeft = self.ancho-self.width

        # Mueve la ventana a la posición 50
        self.left = self.ancho - 50
        self.top  = self.topeTop
        self.move(self.left,self.top)
                
        # Creamos un QTimer
        self.timer = QtCore.QTimer()
        
        # Lo conectamos a función
        self.timer.timeout.connect(self.fnAparecer)
        
        # Ejecutamos el timer indicando velocidad
        self.timer.start(self.velocidad)

        # Muestra la Ventana 
        #if (not self.isVisible()):            
        self.show()
       
        #Ejecuta el Loop
        self.exec_()

    # Mueve la ventana hasta el Centro    
    def fnAparecer(self):

        # Verifica si está apareciendo
        if (self.apareciendo):

            #Obtiene el left de la Ventana menos desplazamiento
            self.left = self.left - self.desplazamiento
        
            # Verifica que no se haya pasado del ancho de la ventana
            if (self.left < self.topeLeft):
                #Ajusta
                self.left = self.topeLeft
            
            # Mueve a la posiición
            #print("Apareciendo:",self.topeLeft)
            #print("Moviendo a:",self.left)
            self.move(self.left,self.top)

            # Verificamos si es igual para hacer espera
            if (self.left == self.topeLeft):
                # Cambiamos la bandera
                self.apareciendo=False

        else:
            # Verifica que la espera ya sea haya cumplido
            if (self.espera == 0):
                #Obtiene el left de la Ventana mas desplazamiento
                self.left = self.left + self.desplazamiento

                if (self.left >= self.ancho):
                    #Cerramos la ventana
                    #print("Cerramos la Ventana")            
                    self.close()

                    #Finalizamos el timer
                    #print("Finalzamos el Timer")
                    self.timer.stop()
                else:
                    # Mueve a la posiición
                    #print("Despareciendo:",self.topeLeft)
                    #print("Moviendo a:",self.left)
                    self.move(self.left,self.top)            
            else:
                # Mensaje de Espera
                self.espera = self.espera -1
                #print("Esperando :",self.espera)

 
# Función principal 
if __name__ == "__main__":
    
    # Crea la Aplicación
    App = QtWidgets.QApplication(sys.argv)

    # Crea el Objeto del Mensaje
    # mensajeCentrado = mensajeCentrado("Mensaje Centrado espera 5 Segundos")
    #input("Presiona para continuar ...")
    mensajeEmergente("Mensaje Emergente que desaparece ...")
    
	
    
    
