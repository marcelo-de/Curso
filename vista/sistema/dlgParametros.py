# ----------------------------------------------------------------------------------
# dlgParametros.py
# Diálogo para la actualización de Parámetros
# ----------------------------------------------------------------------------------

# Librería de Sistema
import sys

# Libreria
from PyQt5 import QtCore, QtGui, QtWidgets

# Librerías Propietarias
import entidades.sistema.entParametros  as ep 
import modelo.sistema.modParametros     as mp
import funciones.funcGrales             as fg
import entidades.entGlobales            as eg
import funciones.funcBaseDatos          as fbd


# Define la clase
class dlgParametros(QtWidgets.QDialog):

    # Declaramos el objeto del Modelo Parámetros
    datParametros = mp.mParametros()

    # Construtor de la Clase
    def __init__(self):
        
        # Llamo a super de la Clase
        super(dlgParametros, self).__init__()

         # Coloca el Icono
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("img/jsIco50x50.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

            
        # Establezco el nombre del Objeto
        self.setObjectName("dlgParametros")
       

        # Establece las dimensiones del Diálogo
        self.resize(423, 534)

        # Establece que es Modal
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setModal(True)

        # Establece el groupBox
        self.gbParametros = QtWidgets.QGroupBox(self)
        self.gbParametros.setGeometry(QtCore.QRect(10, 10, 401, 451))
        self.gbParametros.setObjectName("gbParametros")

        # Crea un objeto de Fuente para usarlo en todos los objetos
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)

        # Establece el check de Mensajes de Éxito
        self.chkMensajesExito = QtWidgets.QCheckBox(self.gbParametros)
        self.chkMensajesExito.setGeometry(QtCore.QRect(30, 20, 341, 31))        
        self.chkMensajesExito.setFont(font)
        self.chkMensajesExito.setObjectName("chkMensajesExito")

        # Establece el check de Verificar Existencias
        self.chkVerificarExistencias = QtWidgets.QCheckBox(self.gbParametros)
        self.chkVerificarExistencias.setGeometry(QtCore.QRect(30, 60, 341, 31))
        self.chkVerificarExistencias.setFont(font)
        self.chkVerificarExistencias.setObjectName("chkVerificarExistencias")

        # Establece el check para Agrupar Productos
        self.chkAgruparProductos = QtWidgets.QCheckBox(self.gbParametros)
        self.chkAgruparProductos.setGeometry(QtCore.QRect(30, 100, 341, 31))
        self.chkAgruparProductos.setFont(font)
        self.chkAgruparProductos.setObjectName("chkAgruparProductos")

        # Establece el check para Activar Bitácora
        self.chkActivarBitacora = QtWidgets.QCheckBox(self.gbParametros)
        self.chkActivarBitacora.setGeometry(QtCore.QRect(30, 140, 341, 31))
        self.chkActivarBitacora.setFont(font)
        self.chkActivarBitacora.setObjectName("chkActivarBitacora")

        # Establece el check para Imprimir el Ticket
        self.chkImprimirTicket = QtWidgets.QCheckBox(self.gbParametros)
        self.chkImprimirTicket.setGeometry(QtCore.QRect(30, 180, 341, 31))
        self.chkImprimirTicket.setFont(font)
        self.chkImprimirTicket.setObjectName("chkImprimirTicket")

        # Establece la etiqueta para el nombre de la Moneda
        self.lblNombreMoneda = QtWidgets.QLabel(self.gbParametros)
        self.lblNombreMoneda.setGeometry(QtCore.QRect(30, 230, 341, 31))
        self.lblNombreMoneda.setFont(font)
        self.lblNombreMoneda.setObjectName("lblNombreMoneda")

        # Establece el lineedit para el nombre de la Moneda
        self.leNombreMoneda = QtWidgets.QLineEdit(self.gbParametros)
        self.leNombreMoneda.setGeometry(QtCore.QRect(30, 260, 341, 31))
        self.leNombreMoneda.setMaxLength(10)
        self.leNombreMoneda.setFont(font)
        self.leNombreMoneda.setObjectName("leNombreMoneda")

        # Establece la etiqueta para el Símbolo de la Moneda
        self.lblSimboloMoneda = QtWidgets.QLabel(self.gbParametros)
        self.lblSimboloMoneda.setGeometry(QtCore.QRect(30, 300, 341, 31))
        self.lblSimboloMoneda.setFont(font)
        self.lblSimboloMoneda.setObjectName("lblSimboloMoneda")

        # Establece el lineedit para el Símbolo de la Moneda
        self.leSimboloMoneda = QtWidgets.QLineEdit(self.gbParametros)
        self.leSimboloMoneda.setGeometry(QtCore.QRect(30, 330, 341, 31))
        self.leSimboloMoneda.setMaxLength(1)
        self.leSimboloMoneda.setFont(font)
        self.leSimboloMoneda.setObjectName("leSimboloMoneda")

        # Establece la etiqueta para el Texto Final
        self.lblTextoFinal = QtWidgets.QLabel(self.gbParametros)
        self.lblTextoFinal.setGeometry(QtCore.QRect(30, 370, 341, 31))
        self.lblTextoFinal.setFont(font)
        self.lblTextoFinal.setObjectName("lblTextoFinal")
        
        # Establece el LineEdit para el Texto Final
        self.leTextoFinal = QtWidgets.QLineEdit(self.gbParametros)
        self.leTextoFinal.setGeometry(QtCore.QRect(30, 400, 341, 31))
        self.leTextoFinal.setMaxLength(40)
        self.leTextoFinal.setFont(font)
        self.leTextoFinal.setObjectName("leTextoFinal")

        # Establece el botón para cancelar
        self.pbCancelar = QtWidgets.QPushButton(self)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 470, 151, 41))
        self.pbCancelar.setFont(font)
        
        # Crea el Icono para cargar la imagen
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Establece el Ícono y su tamaño
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")

        # Controla el Evento Click del Botón Cancelar para Cerrar
        self.pbCancelar.clicked.connect(self.close) 

        # Crea el botón de Aceptar
        self.pbAceptar = QtWidgets.QPushButton(self)
        self.pbAceptar.setGeometry(QtCore.QRect(260, 470, 151, 41))
        self.pbAceptar.setFont(font)

        # Crea el Ícono y lo establece para el botón de aceptar
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setObjectName("pbAceptar")
        
        # Controla el Evento Click
        self.pbAceptar.clicked.connect(self.fnProcesaClickAceptar) 

        # Retranslada ???
        self.retranslate()

        # Conecta a los Slots ??????
        QtCore.QMetaObject.connectSlotsByName(self)

        # Establece el orden de captura
        self.setTabOrder(self.chkMensajesExito, self.chkVerificarExistencias)
        self.setTabOrder(self.chkVerificarExistencias, self.chkAgruparProductos)
        self.setTabOrder(self.chkAgruparProductos, self.chkActivarBitacora)
        self.setTabOrder(self.chkActivarBitacora, self.chkImprimirTicket)
        self.setTabOrder(self.chkImprimirTicket, self.leNombreMoneda)
        self.setTabOrder(self.leNombreMoneda, self.leSimboloMoneda)
        self.setTabOrder(self.leSimboloMoneda, self.leTextoFinal)
        self.setTabOrder(self.leTextoFinal, self.pbAceptar)
        self.setTabOrder(self.pbAceptar, self.pbCancelar)
                
        # Carga los parámetros
        self.fnCargaParametros()

        # Asigno el foco al Nombre de la Moneda
        self.leNombreMoneda.setFocus()

       

    def retranslate(self):   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dlgParametros", "Sistema - Parámetros"))
        self.gbParametros.setTitle(_translate("dlgParametros", "Seleccione y Capture"))
        self.chkMensajesExito.setText(_translate("dlgParametros", "Desplegar Mensajes de Éxito"))
        self.chkVerificarExistencias.setText(_translate("dlgParametros", "Verificar Existencia en Venta"))
        self.chkAgruparProductos.setText(_translate("dlgParametros", "Agrupar Productos en Venta"))
        self.chkActivarBitacora.setText(_translate("dlgParametros", "Activar Bitácora"))
        self.chkImprimirTicket.setText(_translate("dlgParametros", "Imprimir Ticket"))
        self.lblNombreMoneda.setText(_translate("dlgParametros", "Nombre de la Moneda:"))
        self.leNombreMoneda.setText(_translate("dlgParametros", "UnKnow"))
        self.leSimboloMoneda.setText(_translate("dlgParametros", "?"))
        self.lblSimboloMoneda.setText(_translate("dlgParametros", "Símbolo de la Moneda:"))
        self.leTextoFinal.setText(_translate("dlgParametros", "! Gracias por su Compra !"))
        self.lblTextoFinal.setText(_translate("dlgParametros", "Texto Final del Ticket"))
        self.pbCancelar.setText(_translate("dlgParametros", "Cancelar"))
        self.pbAceptar.setText(_translate("dlgParametros", "Aceptar"))

    # Función para cargar la información de parámetros
    def fnCargaParametros(self):
        
        # Ejecuta la Consulta y Obtiene el Objeto
        oParametros = self.datParametros.fnParametrosGet()

        # Verifica que haya obtenido algo
        if (oParametros.getIntMensajesExito()>=0):

            # Coloca los datos en la pantalla
            if (oParametros.getIntMensajesExito()==1):
                self.chkMensajesExito.setChecked(True)
            else:
                self.chkMensajesExito.setChecked(False)    

            if (oParametros.getIntAgruparProductos()==1):
                self.chkAgruparProductos.setChecked(True)
            else:
                self.chkActivarBitacora.setChecked(False)    

            if (oParametros.getIntBitacoraActiva()==1):
                self.chkActivarBitacora.setChecked(True)
            else:
                self.chkActivarBitacora.setChecked(False)    

            if (oParametros.getIntImprimirTicket()==1):
                self.chkImprimirTicket.setChecked(True)
            else:
                self.chkImprimirTicket.setChecked(False)    

            if (oParametros.getIntVerificarExistencias()==1):
                self.chkVerificarExistencias.setChecked(True)
            else:
                self.chkVerificarExistencias.setChecked(False)        

            # Coloca el Mensaje del Ticket
            self.leTextoFinal.setText(oParametros.getStrMensajeTicket())

            # Coloca el Nombre de la Moneda
            self.leNombreMoneda.setText(oParametros.getStrMonedaNombre())

            # Coloca el Símbolo de la Moneda
            self.leSimboloMoneda.setText(oParametros.getStrMonedaSimbolo())

        else:
            # Despliega el Mensaje
            fg.fnMensajeInformacion("Ocurrió un Error al Obtener los Datos de los Parámetros","Verifique la Conexión al Servidor")

     # Función para procesar el Click del Botón de Aceptar
    def fnProcesaClickAceptar(self):

        # Llama función para validar datos
        if (self.fnValidaDatos()):

            # Intenta actualización de la Base de Datos
            self.fnActualizarParametros()

    # Función para validar los datos
    def fnValidaDatos(self):
        
        # Variable para el Mensaje
        sMensaje=""

        # Valida el Nombre de la Moneda
        if (len(self.leNombreMoneda.text())==0):
            # Coloca el dato en el Mensaje
            sMensaje ="El Nombre de la Moneda\n"
            # Coloca el foco en el usuario
            self.leNombreMoneda.setFocus()

        # Valida el Símbolo de la Moneda
        if (len(self.leSimboloMoneda.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leSimboloMoneda.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Símbolo de la Moneda"

        # Valida el Texto del Ticket
        if (len(self.leTextoFinal.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leTextoFinal.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Texto del Final del Ticket"    

        # Verifica si debe desplegar el Mensaje de Error
        if (len(sMensaje)>0):
            # Actualiza el Mensaje
            sMensaje="Revise los siguientes datos:\n" + sMensaje
            # Despliega el MessageBox
            fg.fnMensajeInformacion(sMensaje,"La Moneda, el Símbolo y Texto no pueden quedar vacíos")
            # Hay error en los datos
            return False
        else:
            # Los datos están correctos
            return True   
    
    # Función para Actualizar los Parámetros en la tabla
    def fnActualizarParametros(self):        

        # Crea un objeto de Parametros
        oParametros = ep.eParametros()

        # Coloca los datos en el objeto tomados desde la ventana
        oParametros.setIntMensajesExito(1 if self.chkMensajesExito.isChecked() else 0)
        oParametros.setIntBitacoraActiva(1 if self.chkActivarBitacora.isChecked() else 0)
        oParametros.setIntAgruparProductos(1 if self.chkAgruparProductos.isChecked() else 0)
        oParametros.setIntImprimirTicket(1 if self.chkImprimirTicket.isChecked() else 0)
        oParametros.setIntVerificarExistencias(1 if self.chkVerificarExistencias.isChecked() else 0)
        oParametros.setStrMensajeTicket(self.leTextoFinal.text())
        oParametros.setStrMonedaNombre(self.leNombreMoneda.text())
        oParametros.setStrMonedaSimbolo(self.leSimboloMoneda.text())

        # Llama a la función que actualiza los parámetros
        if (self.datParametros.fnParametrosSet(oParametros)):
            # Despliega mensaje de éxito
            fg.fnMensajeInformacion("Se ha actualizado la tabla de Parámetros","Los cambios surgen efecto de Inmediato")
            # Cierra la ventana
            self.close()



# Función main
if __name__ == '__main__':

    # Importa la librería sys
    import sys

    # Crea el Objeto de la Aplicación
    app = QtWidgets.QApplication(sys.argv)

     # Intentamos conectar al Servidor y a la Base de Datos
    if (fbd.fnConexionServidor()):  

        # Crea el objeto para el Dialogo de Parámetros
        dialog = dlgParametros()

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        sys.exit(dialog.exec_())

    else:
        # Cierra el diálogo
        sys.exit(-1)