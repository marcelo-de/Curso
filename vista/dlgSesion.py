# ----------------------------------------------------------------------
# dlgSesion.py
# Forma inicial del POS que presenta un diálogo para el Inicio de Sesión
# ----------------------------------------------------------------------

# Importa la librería sys
import sys

# Librerias
from PyQt5 import QtCore, QtGui, QtWidgets

# Importamos librerías propietarias
import funciones.funcGrales            as fg
import entidades.entGlobales           as eg
import funciones.funcBaseDatos         as fbd
import funciones.funcVentanas          as fv
import entidades.sistema.entUsuarios   as eu
import modelo.sistema.modUsuarios      as mu
import modelo.modBitacora              as mb
import vista.mwPrincipal
import funciones.funcArchivo           as fa


# Clase para definir el Inicio de Sesión
class Ui_dlgSesion():

    # Variable para datos en Bitácora
    datBitacora = mb.mBitacora()

    # Variable de Clase para controlar el Ingreso
    accesoConcedido = False

    # Define el Método setupUi
    def setupUi(self, dlgSesion):

        # Grabando en el Log
        fa.fnLogGraba("dlgSesion","setupUi","Informativo","Creando el Diálogo ...")


        #Creo la variable de instancia
        self.dlgSesion = dlgSesion

        # Declara un objeto de Paleta de Colores
        palette = QtGui.QPalette()

        # Obtiene una Brocha
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))

        # Establece Estilo
        brush.setStyle(QtCore.Qt.SolidPattern)

        # Establece la Brocha con el Color para el texto de la Paleta para el Objeto Activo
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)

        # Establece la Brocha para el Color gris
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))

        # Establezco la brocha para la Base
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        # Configura la brocha para los diversos estados posibles del Objeto
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        
        # Establece la Brocha con el Color para el texto de la Paleta para el Objeto Inactivo
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)

        # Establece el Color de la Brocha
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        
        # Establece la Brocha con el Color para el texto de la Paleta para el Objeto Inactivo
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

        # Establece el color para Deshabilitado
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
    
        # Coloca la brocha para la paleta cuando está deshabilitado el Texto
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)

        # Establece la brocha para la Base
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))

        # Establece la brocha en la paleta para deshabilitado Base
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        
        # Coloca el nombre del Diálogo
        dlgSesion.setObjectName("dlgSesion")

        # Establece el tamaño del diálogo
        dlgSesion.resize(400, 278)

        # Crea un objeto icon
        icon = QtGui.QIcon()

        # Carga la imagen desde Disco
        icon.addPixmap(QtGui.QPixmap("img/jsIco50x50.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Establece el Icono en el Diálogo
        dlgSesion.setWindowIcon(icon)
        
        # Estabelce Modal
        dlgSesion.setModal(True)

        # Crea el GroupBox en el Diálogo
        self.gbSesion = QtWidgets.QGroupBox(dlgSesion)

        # Establece el tamaño del GroupBox
        self.gbSesion.setGeometry(QtCore.QRect(10, 10, 381, 201))

        # Coloca el nombre
        self.gbSesion.setObjectName("gbSesion")

        # Crea y Define la fuente
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)

        # Crea la etiqueta usuario dentro del GroupBox
        self.lblUsuario = QtWidgets.QLabel(self.gbSesion)
        
        # Establece el tamaño de la Etiqueta
        self.lblUsuario.setGeometry(QtCore.QRect(20, 30, 111, 31))
        
        # Configura la etiqueta de Usuario
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")

        # Se repite el mismo proceso para el password
        self.lblClave = QtWidgets.QLabel(self.gbSesion)
        self.lblClave.setGeometry(QtCore.QRect(20, 70, 111, 31))

        # Establece la fuente y nombre de Objeto para el lblClave
        self.lblClave.setFont(font)
        self.lblClave.setObjectName("lblClave")

        # Crea la etiqueta de Nombre y lo agrega al GroupBox
        self.lblNombre = QtWidgets.QLabel(self.gbSesion)

        # Establece posición y tamaño del lblNombre
        self.lblNombre.setGeometry(QtCore.QRect(20, 110, 111, 31))

        # Establece Nombre y Fuente para la etiqueta del Nombre
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
                
        # Repite el Proceso para el Role
        self.lblRole = QtWidgets.QLabel(self.gbSesion)
        self.lblRole.setGeometry(QtCore.QRect(20, 150, 111, 31))
        self.lblRole.setFont(font)
        self.lblRole.setObjectName("lblRole")
        

        # Crea el lineEdit del usuario y establece su tamaño
        self.leUsuario = QtWidgets.QLineEdit(self.gbSesion)
        self.leUsuario.setGeometry(QtCore.QRect(140, 30, 221, 31))

        # Establece la fuente, Longitud y el Nombre del Objeto
        self.leUsuario.setFont(font)
        self.leUsuario.setMaxLength(10)
        self.leUsuario.setObjectName("leUsuario")

        # Establece la Función para Enter
        self.leUsuario.returnPressed.connect(self.fnProcesaEnter) 
        
        # Establece la función para saber si se presiona una tecla
        self.leUsuario.keyPressEvent = self.keyPressEvent
       
        # Repite el mismo proceso para el password
        self.leClave = QtWidgets.QLineEdit(self.gbSesion)
        self.leClave.setGeometry(QtCore.QRect(140, 70, 221, 31))
        self.leClave.setFont(font)
        self.leClave.setMaxLength(10)
        
        # Establece el modo de Echo, es decir que sea como password
        self.leClave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leClave.setObjectName("leClave")

        # Establece la Función para Enter
        self.leClave.returnPressed.connect(self.fnProcesaEnter)

        # Establece el control de evento para cuando se presiona una tecla
        self.leClave.keyPressEvent = self.keyPressEvent


        # Crea el lineEdit para el Nombre y define su posición y tamaño
        self.leNombre = QtWidgets.QLineEdit(self.gbSesion)
        self.leNombre.setGeometry(QtCore.QRect(140, 110, 221, 31))
        self.leNombre.setFont(font)
        self.leNombre.setObjectName("leNombre")
        
        # Establece la Longitud y que solo es de Lectura
        self.leNombre.setMaxLength(50)
        self.leNombre.setReadOnly(True)
        
        # Establece la paleta
        self.leNombre.setPalette(palette)

        # Repite el mismo proceso para el Role
        self.leRole = QtWidgets.QLineEdit(self.gbSesion)
        self.leRole.setGeometry(QtCore.QRect(140, 150, 221, 31))
        self.leRole.setFont(font)
        self.leRole.setObjectName("leRole")
        self.leRole.setMaxLength(50)
        self.leRole.setReadOnly(True)
       
        # Establece la paleta
        self.leRole.setPalette(palette)

        # Crea el botón de Aceptar dentro del Diálogo y establece tamaño, posición y fuente
        self.pbAceptar = QtWidgets.QPushButton(dlgSesion)
        self.pbAceptar.setGeometry(QtCore.QRect(230, 220, 161, 41))
        self.pbAceptar.setFont(font)
        
        # Usa el objeto ico para agregar la imagen al botón de Aceptar
        icon.addPixmap(QtGui.QPixmap("img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Establece el Icono en el Botón de Aceptar, el tamaño y el nombre
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setObjectName("pbAceptar")
        self.pbAceptar.setAutoDefault(False)
        self.pbAceptar.setDefault(False)

        # Asocia el KeyPressEvent
        self.pbAceptar.keyPressEvent = self.keyPressEvent

        # Controla el Evento Click
        self.pbAceptar.clicked.connect(self.fnProcesaClickAceptar) 
        
        # Repite el mismo proceso para el botón de Cancelar
        self.pbCancelar = QtWidgets.QPushButton(dlgSesion)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 220, 161, 41))
        self.pbCancelar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbCancelar.setAutoDefault(False)

        # Controla el Evento Click del Botón Cancelar para Cerrar
        self.pbCancelar.clicked.connect(dlgSesion.close) 

        # Retranslada el diálogo
        self.retranslateUi(dlgSesion)
        QtCore.QMetaObject.connectSlotsByName(dlgSesion)

    def retranslateUi(self, dlgSesion):
        _translate = QtCore.QCoreApplication.translate
        dlgSesion.setWindowTitle(_translate("dlgSesion", "Inicio de Sesion"))
        self.gbSesion.setTitle(_translate("dlgSesion", "Usuario y Password"))
        self.lblUsuario.setText(_translate("dlgSesion", "Usuario:"))
        self.leUsuario.setToolTip(_translate("dlgSesion", "Nombre de Usuario Registrado en la BD"))
        self.lblClave.setText(_translate("dlgSesion", "Password:"))
        self.leClave.setToolTip(_translate("dlgSesion", "Clave de Acceso del Usuario"))
        self.lblNombre.setText(_translate("dlgSesion", "Nombre:"))
        self.lblRole.setText(_translate("dlgSesion", "Role:"))
        self.leNombre.setText(_translate("dlgSesion", "Unknow"))
        self.leRole.setText(_translate("dlgSesion", "UnKnow"))
        self.pbAceptar.setText(_translate("dlgSesion", "Aceptar"))
        self.pbCancelar.setText(_translate("dlgSesion", "Cancelar"))
        self.pbAceptar.setToolTip(_translate("dlgSesion", "Presione para Intertar el Acceso al Sistema"))
        self.pbCancelar.setToolTip(_translate("dlgSesion", "Salida del Inicio de Sesión"))

    # Función para procesar el Enter
    def fnProcesaEnter(self):   
        # Verifica si tiene el foco el Usuario
        if (self.leUsuario.hasFocus()): 
            # Manda el Foco al Password
            self.leClave.setFocus()
        else:
            # El Foco lo tiene el Password
            # Manda el Foco al botón de Aceptar
            self.pbAceptar.setFocus()    


    # Se ha presionado una tecla
    def keyPressEvent(self, event):
        # Verifica si tiene el foco el botón de Aceptar
        if (self.leUsuario.hasFocus()):
            return QtWidgets.QLineEdit.keyPressEvent(self.leUsuario, event)    

        elif (self.leClave.hasFocus()):
            return QtWidgets.QLineEdit.keyPressEvent(self.leClave, event)
        else:
            # Verificando que sea enter
            if (event.key() == QtCore.Qt.Key_Return):
                
                # Verifica que el texto del Botón sea Aceptar
                if (self.pbAceptar.text()=="Aceptar"):
                    # Llama función para validar datos
                    if (self.fnValidaDatos()):
                        # Intenta conexión al Sistema
                        self.fnSistemaConectar()
                else:
                    # Establezco acceso concedido
                    self.accesoConcedido=True

                    # Registro en la Bitácora
                    self.datBitacora.fnBitacoraRegistrar("Login")

                    #Cierro el diálogo de Sesión
                    self.dlgSesion.close()                                                        
                                    
    # Función para procesar el Click del Botón de Aceptar
    def fnProcesaClickAceptar(self):
        if (self.pbAceptar.text()=="Aceptar"):
            # Llama función para validar datos
            if (self.fnValidaDatos()):
                # Intenta conexión a BD
                self.fnSistemaConectar()
        else:
            # Establezco acceso concedido
            self.accesoConcedido=True

            # Registra ingreso en la Bitácora
            self.datBitacora.fnBitacoraRegistrar("Login")

            #Cierro el diálogo de Sesión
            self.dlgSesion.close()   
            

    # Función para validar los datos
    def fnValidaDatos(self):
        
        # Variable para el Mensaje
        sMensaje=""

        # Valida el Servidor
        if (len(self.leUsuario.text())==0):
            # Coloca el dato en el Mensaje
            sMensaje ="El Usuario\n"
            # Coloca el foco en el usuario
            self.leUsuario.setFocus()

        # Valida el Password
        if (len(self.leClave.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leClave.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "La Clave"

        # Verifica si debe desplegar el Mensaje de Error
        if (len(sMensaje)>0):
            # Actualiza el Mensaje
            sMensaje="Revise los siguientes datos:\n" + sMensaje
            # Despliega el MessageBox
            fg.fnMensajeInformacion(sMensaje,"El Usuario y Clave no pueden quedar vacíos")
            # Hay error en los datos
            return False
        else:
            # Los datos están correctos
            return True

    # Función para Conectar al Sistema
    def fnSistemaConectar(self):

        # Variable de Resultado
        resultado = False

        # Declaramos el objeto de la Entidad Usuarios
        oUsuario = eu.eUsuarios()

        # Declaramos el objeto del Modelo Usuarios
        datUsuario = mu.mUsuarios()

        # Ejecuta la Consulta y Obtiene el Objeto
        oUsuario = datUsuario.fnUsuarioGet(self.leUsuario.text(),self.leClave.text())

        # Verifica que haya obtenido algo
        if (oUsuario.getStrUsuarioIde()!=""):
            
            # Coloca los datos en las Variables globales correspondientes
            eg.eGlobales.UsuarioIde = oUsuario.getStrUsuarioIde()

            # Obtiene el Nombre del Usuario 
            eg.eGlobales.UsuarioNom = oUsuario.getStrUsuarioName()

            # Obtiene el Role del Usuario
            eg.eGlobales.UsuarioRol = oUsuario.getStrRoleName()

            # Coloca el Nombre y el Rol en la Pantalla
            self.leNombre.setText(eg.eGlobales.UsuarioNom)
            self.leRole.setText(eg.eGlobales.UsuarioRol)

            # Deshabilita el Botón de Cancelar
            self.pbCancelar.setEnabled(False)

            # Deshabilita el Usuario y Clave
            self.leUsuario.setEnabled(False)
            self.leClave.setEnabled(False)                

            #Cambia el Texto del Botón de Aceptar
            self.pbAceptar.setText("Ingresar")
        
            # Coloca el Resultado
            resultado = True

        else:
            # Mensaje de que no es correcto
            fg.fnMensajeInformacion("Error en Usuario-Clave","Verifique su Usuario y Clave")

            # Regresa el Foco al Usuario
            self.leUsuario.setFocus()


        # Retorna el Resultado
        return resultado   

    # Método ejecuta el diálogo
    def Ejecutar(self):
       
        # Crea el objeto de Aplicación
        app = QtWidgets.QApplication(sys.argv)

        
        # Intentamos conectar al Servidor y a la Base de Datos
        if (fbd.fnConexionServidor()):

            # Crea el diálogo
            dlgSesion = QtWidgets.QDialog()
            
            # Llama al objeto pasando como parámetro el Diálogo
            self.setupUi(dlgSesion)

            # Muestra el Diálogo
            dlgSesion.show()

            # Crea el Objeto de la Ventana Emergenet
            fv.mensajeEmergente("Iniciando Sesión ...")

            # Ejecuta el loop
            dlgSesion.exec_()

            # Pregunta si el acceso es concedido
            if (self.accesoConcedido):

                # Crea el Objeto de la Ventana Principal
                xPrincipal = QtWidgets.QMainWindow()

                # Crea el objeto desde la Clase Ui_mwPrincipal
                ui = vista.mwPrincipal.Ui_mwPrincipal()

                # Ejecuta el Método setup
                ui.setupUi(xPrincipal)

                # Muestra la ventana principal
                xPrincipal.showMaximized()

                # Crea el Objeto de la Ventana Emergenet
                fv.mensajeEmergente("Iniciando Aplicación ...")
                
                # Ejecuta la ventana principal
                sys.exit(app.exec_())

                
            else:
                # Cerrar el Servidor
                print("Cerrando la Conexión")
                fbd.fnConexionCerrar()

                # Finaliza
                sys.exit(-1)        
        
        else:

            # Finaliza
            sys.exit(-1)

    
   

# Función main
if __name__ == "__main__":

    # Crea un objeto de la Clase
    oDlgSesion = Ui_dlgSesion()

    # Ejecuta
    oDlgSesion.Ejecutar()
   

    