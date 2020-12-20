# ----------------------------------------------------------------------------------
# dlgMensaje.py
# Diálogo para mostrar Mensajes con Aceptar y Cancelar(opcional) 
# ----------------------------------------------------------------------------------

# Librería de Sistema
import sys

# Libreria
from PyQt5 import QtCore, QtGui, QtWidgets

# Librerías Propietarias
import entidades.entGlobales   as eg

# Define la clase
class dlgMensaje(QtWidgets.QDialog):

    # Construtor de la Clase
    def __init__(self,tituloMensaje, contenidoMensaje, botonCancelar):
        
        # Llamo a super de la Clase
        super(dlgMensaje, self).__init__()

        # Bandera para que no aparezaca el Título
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Coloca la Bandera
        self.setWindowFlags(flags)

        # Establezco el nombre del Objeto
        self.setObjectName("dlgMensaje")        

        # Establece que es Modal
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setModal(True)

        # Establece las dimensiones del Diálogo
        self.resize(528, 230)

        # Define el objeto de Fuente
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)

        # Establece el groupBox
        self.gbParametros = QtWidgets.QGroupBox(self)
        self.gbParametros.setGeometry(QtCore.QRect(0, 0, 528, 230))
        self.gbParametros.setObjectName("gbMensaje")

        # Etiqueta de Título
        self.lblTitulo = QtWidgets.QLabel(self)
        self.lblTitulo.setGeometry(QtCore.QRect(10, 10, 510, 30))
        self.lblTitulo.setFont(font)
        self.lblTitulo.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")

        # Texto del Mensaje
        self.teMensaje = QtWidgets.QTextEdit(self)
        self.teMensaje.setGeometry(QtCore.QRect(10, 50, 510, 120))
        self.teMensaje.setFont(font)
        self.teMensaje.setReadOnly(True)
        self.teMensaje.setObjectName("teMensaje")

        # Botón de Cancelar
        self.pbCancelar = QtWidgets.QPushButton(self)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 180, 170, 40))
        self.pbCancelar.setFont(font)
        
        # Crea objeto para iconos
        icon = QtGui.QIcon()
        
        # Establec el ícono
        icon.addPixmap(QtGui.QPixmap("img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        # Lo asigna al botón cancelar
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setAutoDefault(False)
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbCancelar.clicked.connect(self.close) 

        if (not botonCancelar):
            # Lo oculta
            self.pbCancelar.setHidden(True)

        # Botón de Aceptar
        self.pbAceptar = QtWidgets.QPushButton(self)
        self.pbAceptar.setGeometry(QtCore.QRect(350, 180, 171, 41))
        self.pbAceptar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setAutoDefault(False)
        self.pbAceptar.setObjectName("pbAceptar")
        self.pbAceptar.clicked.connect(self.fnProcesaClickAceptar) 

        # Retranslate
        self.retranslate(tituloMensaje, contenidoMensaje)
        # Slot?
        QtCore.QMetaObject.connectSlotsByName(self)

        # Coloca el Foco
        self.pbAceptar.setFocus()

        # Establece como default botón presiondo cancelar
        eg.eGlobales.BotonPresionado = eg.eGlobales.BOTON_CANCELAR
        
        

    def retranslate(self, titulo, mensaje,):   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Mensaje"))
        self.lblTitulo.setText(_translate("Dialog", titulo))
        self.teMensaje.setText(_translate("Dialog", mensaje))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar"))
        self.pbAceptar.setText(_translate("Dialog", "Aceptar"))


    # Función para procesar el Click del Botón de Aceptar
    def fnProcesaClickAceptar(self):

        # Cambia el valor de la variable Global
        eg.eGlobales.BotonPresionado = eg.eGlobales.BOTON_ACEPTAR

        # Cierra 
        self.close()


    
# Función main
if __name__ == '__main__':

    # Importa la librería sys
    import sys

    # Crea el Objeto de la Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea un Mensaje
    sMensaje =  "El Sistema no logró la Conexión debido a que conector de MySql no se encuentra activado.\n"
    sMensaje += "Ejecuta el Conector antes de lanzar la aplicación.\n"
    sMensaje += "Si el problema persiste consulta con el Administrador del Sistema."
    
     
    # Crea el objeto para el Dialogo de Empresa
    dialog = dlgMensaje("! Advertencia !", sMensaje,False)

    # Muestra el Diálogo
    dialog.show()

    #Lanza la aplicación
    dialog.exec_()

    # Verifico que botón se presiono
    print("Boton Presionado:",eg.eGlobales.BotonPresionado)

    # Finaliza aplicación
    sys.exit()

    