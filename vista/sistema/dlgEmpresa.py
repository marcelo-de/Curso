# ----------------------------------------------------------------------------------
# dlgEmpresa.py
# Diálogo para la Actualización de los datos de la Empresa
# ----------------------------------------------------------------------------------

# Librería de Sistema
import sys

# Libreria
from PyQt5 import QtCore, QtGui, QtWidgets

# Librerías Propietarias
import entidades.sistema.entEmpresa  as ee
import modelo.sistema.modEmpresa     as me
import funciones.funcGrales          as fg
import entidades.entGlobales         as eg
import funciones.funcBaseDatos       as fbd
import funciones.funcVentanas        as fv


# Define la clase
class dlgEmpresa(QtWidgets.QDialog):

    # Declaramos el objeto del Modelo Empresa
    datEmpresa = me.mEmpresa()

    # Variable para la ruta del Logo
    sLogo=""

    # Construtor de la Clase
    def __init__(self):
        
        # Llamo a super de la Clase
        super(dlgEmpresa, self).__init__()

        # Coloca el Icono
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("img/jsIco50x50.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Establezco el nombre del Objeto
        self.setObjectName("dlgEmpresa")        

        # Establece las dimensiones del Diálogo
        self.resize(400, 420)

        # Establece que es Modal
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setModal(True)

        # Establece el groupBox
        self.gbEmpresa = QtWidgets.QGroupBox(self)
        self.gbEmpresa.setGeometry(QtCore.QRect(10, 10, 380, 340))
        self.gbEmpresa.setObjectName("gbEmpresa")

        # Crea un objeto de Fuente para usarlo en todos los objetos
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)

        # Objetos en el diálogo
        # =========================================================
        self.lblNombre = QtWidgets.QLabel(self.gbEmpresa)
        self.lblNombre.setGeometry(QtCore.QRect(20, 30, 120, 30))
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")

        self.lblDireccion = QtWidgets.QLabel(self.gbEmpresa)
        self.lblDireccion.setGeometry(QtCore.QRect(20, 70, 120, 30))
        self.lblDireccion.setFont(font)
        self.lblDireccion.setObjectName("lblDireccion")

        self.lblTelefono = QtWidgets.QLabel(self.gbEmpresa)
        self.lblTelefono.setGeometry(QtCore.QRect(20, 110, 120, 30))
        self.lblTelefono.setFont(font)
        self.lblTelefono.setObjectName("lblTelefono")

        self.lblRfc = QtWidgets.QLabel(self.gbEmpresa)
        self.lblRfc.setGeometry(QtCore.QRect(20, 150, 120, 30))
        self.lblRfc.setFont(font)
        self.lblRfc.setObjectName("lblRfc")

        self.lblSerial = QtWidgets.QLabel(self.gbEmpresa)
        self.lblSerial.setGeometry(QtCore.QRect(20, 190, 120, 30))
        self.lblSerial.setFont(font)
        self.lblSerial.setObjectName("lblSerial")

        self.lblLogo = QtWidgets.QLabel(self.gbEmpresa)
        self.lblLogo.setGeometry(QtCore.QRect(20, 230, 120, 30))
        self.lblLogo.setFont(font)
        self.lblLogo.setObjectName("lblLogo")

        self.pbLogo = QtWidgets.QPushButton(self.gbEmpresa)
        self.pbLogo.setGeometry(QtCore.QRect(160, 240, 75, 80))
        self.pbLogo.setText("")
        self.pbLogo.setIconSize(QtCore.QSize(64, 64))
        self.pbLogo.setAutoDefault(False)
        self.pbLogo.setObjectName("pbLogo")
        self.pbLogo.clicked.connect(self.fnSeleccionaLogo) 

        self.leNombre = QtWidgets.QLineEdit(self.gbEmpresa)
        self.leNombre.setGeometry(QtCore.QRect(160, 30, 210, 30))
        self.leNombre.setFont(font)
        self.leNombre.setMaxLength(40)
        self.leNombre.setObjectName("leNombre")
        
        self.leDireccion = QtWidgets.QLineEdit(self.gbEmpresa)
        self.leDireccion.setGeometry(QtCore.QRect(160, 70, 210, 30))        
        self.leDireccion.setFont(font)
        self.leDireccion.setMaxLength(40)
        self.leDireccion.setObjectName("leDireccion")

        self.leTelefono = QtWidgets.QLineEdit(self.gbEmpresa)
        self.leTelefono.setGeometry(QtCore.QRect(160, 110, 210, 30))
        self.leTelefono.setFont(font)
        self.leTelefono.setMaxLength(40)
        self.leTelefono.setObjectName("leTelefono")
        
        self.leRFC = QtWidgets.QLineEdit(self.gbEmpresa)
        self.leRFC.setGeometry(QtCore.QRect(160, 150, 210, 30))
        self.leRFC.setFont(font)
        self.leRFC.setMaxLength(13)
        self.leRFC.setObjectName("leRFC")

        self.leSerial = QtWidgets.QLineEdit(self.gbEmpresa)
        self.leSerial.setGeometry(QtCore.QRect(160, 190, 210, 30))
        self.leSerial.setFont(font)
        self.leSerial.setMaxLength(10)
        self.leSerial.setObjectName("leSerial")

        # Establece el botón para cancelar
        self.pbCancelar = QtWidgets.QPushButton(self)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 370, 150, 40))
        self.pbCancelar.setFont(font)
        
        # Crea el Icono para cargar la imagen
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Establece el Ícono y su tamaño
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbCancelar.setAutoDefault(False)
        
        # Controla el Evento Click del Botón Cancelar para Cerrar
        self.pbCancelar.clicked.connect(self.close) 

        # Crea el botón de Aceptar
        self.pbAceptar = QtWidgets.QPushButton(self)
        self.pbAceptar.setGeometry(QtCore.QRect(240, 370, 150, 40))
        self.pbAceptar.setFont(font)

        # Crea el Ícono y lo establece para el botón de aceptar
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setObjectName("pbAceptar")
        
        # Controla el Evento Click
        self.pbAceptar.clicked.connect(self.fnProcesaClickAceptar) 
        self.pbAceptar.setAutoDefault(True)

        # Retranslada ???
        self.retranslate()

        # Conecta a los Slots ??????
        QtCore.QMetaObject.connectSlotsByName(self)

        # Establece el orden de captura
        dlgEmpresa.setTabOrder(self.leNombre, self.leDireccion)
        dlgEmpresa.setTabOrder(self.leDireccion, self.leTelefono)
        dlgEmpresa.setTabOrder(self.leTelefono, self.leRFC)
        dlgEmpresa.setTabOrder(self.leRFC, self.leSerial)
        dlgEmpresa.setTabOrder(self.leSerial, self.pbLogo)
        dlgEmpresa.setTabOrder(self.pbLogo, self.pbAceptar)
        dlgEmpresa.setTabOrder(self.pbAceptar, self.pbCancelar)
                
        # Carga los Datos de la Empresa
        self.fnCargaEmpresa()        
       

    def retranslate(self):   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dlgEmpresa", "Sistema - Empresa"))
        self.gbEmpresa.setTitle(_translate("dlgEmpresa", "Datos"))
        self.lblNombre.setText(_translate("dlgEmpresa", "Nombre:"))
        self.lblDireccion.setText(_translate("dlgEmpresa", "Dirección:"))
        self.lblTelefono.setText(_translate("dlgEmpresa", "Teléfono:"))
        self.lblRfc.setText(_translate("dlgEmpresa", "RFC:"))
        self.lblSerial.setText(_translate("dlgEmpresa", "Serial:"))
        self.lblLogo.setText(_translate("dlgEmpresa", "Logo:"))
        self.pbCancelar.setText(_translate("dlgEmpresa", "Cancelar"))
        self.pbAceptar.setText(_translate("dlgEmpresa", "Aceptar"))

    # Función para cargar la información de Empresa
    def fnCargaEmpresa(self):
        
        # Ejecuta la Consulta y Obtiene el Objeto
        oEmpresa = self.datEmpresa.fnEmpresaGet()

        # Verifica que haya obtenido algo
        if (oEmpresa.getStrEmpresaNombre!=""):

            # Coloca el Mensaje del Ticket
            self.leNombre.setText(oEmpresa.getStrEmpresaNombre())
            self.leDireccion.setText(oEmpresa.getStrEmpresaDireccion())
            self.leTelefono.setText(oEmpresa.getStrEmpresaTelefono())
            self.leRFC.setText(oEmpresa.getStrEmpresaRfc())
            self.leSerial.setText(oEmpresa.getStrEmpresaSerial())

            # Obtiene la ruta del Logo
            self.sLogo = oEmpresa.getStrEmpresaLogo()

            # Crea un icono 
            icon = QtGui.QIcon()

            # Carga la imagen en el Icono
            icon.addPixmap(QtGui.QPixmap(self.sLogo), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            # Coloca el Icon en el Botón
            self.pbLogo.setIcon(icon)


        else:
            # Despliega el Mensaje
            fg.fnMensajeInformacion("Ocurrió un Error al Obtener los Datos de la Empresa","Verifique la Conexión al Servidor")

     # Función para procesar el Click del Botón de Aceptar
    def fnProcesaClickAceptar(self):

        # Llama función para validar datos
        if (self.fnValidaDatos()):

            # Intenta actualización de la Base de Datos
            self.fnActualizarEmpresa()

    # Función para validar los datos
    def fnValidaDatos(self):
        
        # Variable para el Mensaje
        sMensaje=""

        # Valida el Nombre de la Moneda
        if (len(self.leNombre.text())==0):
            # Coloca el dato en el Mensaje
            sMensaje ="El Nombre \n"
            # Coloca el foco en el usuario
            self.leNombre.setFocus()

        # Valida la direccion
        if (len(self.leDireccion.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leDireccion.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "La Dirección \n"

        # Valida el Telefono
        if (len(self.leTelefono.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leTelefono.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Teléfono \n"    

        # Valida el RFC
        if (len(self.leRFC.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leRfc.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El RFC \n"    

        # Valida el Serial
        if (len(self.leTelefono.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leTelefono.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Teléfono \n"    

        # Verifica si debe desplegar el Mensaje de Error
        if (len(sMensaje)>0):
            # Actualiza el Mensaje
            sMensaje="Revise los siguientes datos:\n" + sMensaje
            # Despliega el MessageBox
            fg.fnMensajeInformacion(sMensaje,"Los Datos no pueden quedar vacíos")
            # Hay error en los datos
            return False
        else:
            # Los datos están correctos
            return True   
    
    # Función para Actualizar los datos de Empresa en la tabla
    def fnActualizarEmpresa(self):        

        # Crea un objeto de Empresa
        oEmpresa = ee.eEmpresa()

        # Coloca los datos desde la pantalla al objeto
        oEmpresa.setStrEmpresaNombre(self.leNombre.text())
        oEmpresa.setStrEmpresaDireccion(self.leDireccion.text())
        oEmpresa.setStrEmpresaTelefono(self.leTelefono.text())
        oEmpresa.setStrEmpresaRfc(self.leRFC.text())
        oEmpresa.setStrEmpresaSerial(self.leSerial.text())
        oEmpresa.setStrEmpresaLogo(self.sLogo)
        
        # Llama a la función que actualiza los parámetros
        if (self.datEmpresa.fnEmpresaSet(oEmpresa)):
            
            # Verificamos si desplegamos mensaje de Exito
            if (eg.eGlobales.MensajesExito):
                # Despliega mensaje de éxito
                fg.fnMensajeInformacion("Se ha actualizado la tabla de Empresa","Los cambios surgen efecto de Inmediato")
            else:
                # Despliega mensaje emergente de exito
                fv.mensajeEmergente("Se han actualizado los datos...")
            # Cierra la ventana
            self.close()

    # Mostrar el Diálogo de Archivos
    def fnSeleccionaLogo(self):

        # Llama el dialogo de Archivos usando img por default
        archivoSeleccionado = QtWidgets.QFileDialog.getOpenFileName(self, 
                                                                   'Seleccione el Logo', 
                                                                   'img')#,
                                                                   #"PNG files (*.png);;JPG files (*.jpg);;"
                                                                   #"ICO files (*.ico);;BMP (*.bmp)")
        
        # Verifica que tenga algo
        if (len(archivoSeleccionado[0])>0):

            # Crea un icono 
            icon = QtGui.QIcon()

            # Carga la imagen en el Icono
            icon.addPixmap(QtGui.QPixmap(archivoSeleccionado[0]), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            # Verifica que No lo pudo cargar
            if (icon.isNull()):
                # Despliega un Mensaje
                fg.fnMensajeInformacion("Ocurrió un Error al cargar el Archivo:"+archivoSeleccionado[0],"Verifique que sea un archivo de imagen")
            else:
                # Establece el icono en el botón
                self.pbLogo.setIcon(icon)
                
                # Establece la nueva ruta para el archivo del logo
                self.sLogo=archivoSeleccionado[0]            

# Función main
if __name__ == '__main__':

    # Importa la librería sys
    import sys

    # Crea el Objeto de la Aplicación
    app = QtWidgets.QApplication(sys.argv)

     # Intentamos conectar al Servidor y a la Base de Datos
    if (fbd.fnConexionServidor()):  

        # Crea el objeto para el Dialogo de Empresa
        dialog = dlgEmpresa()

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        sys.exit(dialog.exec_())

    else:
        # Cierra el diálogo
        sys.exit(-1)