# ----------------------------------------------------------------------------------
# dlgUsuarios.py
# Diálogo para la Actualización de Usuarios
# ----------------------------------------------------------------------------------

# Librería de Sistema
import sys

# Libreria
from PyQt5 import QtCore, QtGui, QtWidgets

# Librerías Propietarias
import entidades.sistema.entUsuarios as eu
import modelo.sistema.modUsuarios    as mu
import modelo.sistema.modRolProcesos as mrp
import modelo.sistema.modProcesos    as mp
import funciones.funcGrales          as fg
import entidades.entGlobales         as eg
import funciones.funcBaseDatos       as fbd
import funciones.funcVentanas        as fv


# Define la clase
class dlgUsuarios(QtWidgets.QDialog):

    # Declaramos el objeto del Modelo Usuarios
    datUsuarios = mu.mUsuarios()

    # Declaramos el objeto del Modelo RolProcesos
    datRolProcesos = mrp.mRolProcesos()

    # Declaramos el objeto del Modelo Procesos
    datProcesos = mp.mProcesos()

    # Declaramos variable para Identificación la operación
    sOperacion=""

    # Variable para saber cuando se está cargando datos
    bCargando = False

    # Constructor de la Clase
    def __init__(self):
        
        # Llamo a super de la Clase
        super(dlgUsuarios, self).__init__()

        # Activa ventana de que se están cargando datos
        self.bCargando = True

        # Coloca el Icono
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("img/jsIco50x50.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Establezco el nombre del Objeto
        self.setObjectName("dlgUsuarios")        

        # Establece las dimensiones del Diálogo
        self.resize(770, 492)

        # Establece que es Modal
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setModal(True)
        
        # Crea un objeto de Fuente para usarlo en todos los objetos
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        
        # Crea el objeto Ícono
        icon = QtGui.QIcon()

        # El Encabezado
        self.gbUsuario = QtWidgets.QGroupBox(self)
        self.gbUsuario.setGeometry(QtCore.QRect(10, 10, 750, 60))
        self.gbUsuario.setObjectName("gbUsuario")

        self.lblIdentificacion = QtWidgets.QLabel(self.gbUsuario)
        self.lblIdentificacion.setGeometry(QtCore.QRect(20, 20, 135, 30))
        self.lblIdentificacion.setFont(font)
        self.lblIdentificacion.setObjectName("lblIdentificacion")

        self.leIdentificacion = QtWidgets.QLineEdit(self.gbUsuario)
        self.leIdentificacion.setGeometry(QtCore.QRect(170, 20, 190, 30))
        self.leIdentificacion.setObjectName("leIdentificacion")
        self.leIdentificacion.setFont(font)
        self.leIdentificacion.setMaxLength(10)

        self.lblUsuarios = QtWidgets.QLabel(self.gbUsuario)
        self.lblUsuarios.setGeometry(QtCore.QRect(390, 20, 135, 30))
        self.lblUsuarios.setFont(font)
        self.lblUsuarios.setObjectName("lblUsuarios")

        self.cboUsuarios = QtWidgets.QComboBox(self.gbUsuario)
        self.cboUsuarios.setGeometry(QtCore.QRect(540, 20, 190, 30))
        self.cboUsuarios.setObjectName("cboUsuarios")
        self.cboUsuarios.setFont(font)
        self.cboUsuarios.currentTextChanged.connect(self.fnUsuarioSeleccionado)

        # Detalle
        self.gbDetalle = QtWidgets.QGroupBox(self)
        self.gbDetalle.setGeometry(QtCore.QRect(10, 80, 750, 321))
        self.gbDetalle.setObjectName("gbDetalle")

        self.lblPassword = QtWidgets.QLabel(self.gbDetalle)
        self.lblPassword.setGeometry(QtCore.QRect(20, 30, 135, 30))
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")

        self.lePassword = QtWidgets.QLineEdit(self.gbDetalle)
        self.lePassword.setGeometry(QtCore.QRect(170, 30, 190, 30))
        self.lePassword.setObjectName("lePassword")
        self.lePassword.setFont(font)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setMaxLength(10)

        self.lblConfirmar = QtWidgets.QLabel(self.gbDetalle)
        self.lblConfirmar.setGeometry(QtCore.QRect(390, 30, 135, 30))
        self.lblConfirmar.setFont(font)
        self.lblConfirmar.setObjectName("lblConfirmar")

        self.leConfirmar = QtWidgets.QLineEdit(self.gbDetalle)
        self.leConfirmar.setGeometry(QtCore.QRect(540, 30, 190, 30))
        self.leConfirmar.setObjectName("leConfirmar")
        self.leConfirmar.setFont(font)
        self.leConfirmar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leConfirmar.setMaxLength(10)

        self.lblNombre = QtWidgets.QLabel(self.gbDetalle)
        self.lblNombre.setGeometry(QtCore.QRect(20, 70, 135, 30))
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")

        self.leNombre = QtWidgets.QLineEdit(self.gbDetalle)
        self.leNombre.setGeometry(QtCore.QRect(170, 70, 560, 30))
        self.leNombre.setObjectName("leNombre")
        self.leNombre.setFont(font)
        self.leNombre.setMaxLength(50)

        self.lblRol = QtWidgets.QLabel(self.gbDetalle)
        self.lblRol.setGeometry(QtCore.QRect(20, 110, 135, 30))
        self.lblRol.setFont(font)
        self.lblRol.setObjectName("lblRol")

        self.leRol = QtWidgets.QLineEdit(self.gbDetalle)
        self.leRol.setGeometry(QtCore.QRect(170, 110, 190, 30))
        self.leRol.setObjectName("leRol")
        self.leRol.setFont(font)
        self.leRol.setMaxLength(10)

        self.lblRoles = QtWidgets.QLabel(self.gbDetalle)
        self.lblRoles.setGeometry(QtCore.QRect(390, 110, 135, 30))
        self.lblRoles.setFont(font)
        self.lblRoles.setObjectName("lblRoles")

        self.cboRoles = QtWidgets.QComboBox(self.gbDetalle)
        self.cboRoles.setGeometry(QtCore.QRect(540, 110, 190, 30))
        self.cboRoles.setObjectName("cboRoles")
        self.cboRoles.setFont(font)
        self.cboRoles.currentTextChanged.connect(self.fnRolSeleccionado)

        self.gbProcesos = QtWidgets.QGroupBox(self.gbDetalle)
        self.gbProcesos.setGeometry(QtCore.QRect(20, 150, 711, 161))
        self.gbProcesos.setObjectName("gbProcesos")
        self.listProcesos = QtWidgets.QListWidget(self.gbProcesos)
        self.listProcesos.setGeometry(QtCore.QRect(10, 20, 691, 131))
        self.listProcesos.setObjectName("listProcesos")
        self.listProcesos.setFont(font)
        self.listProcesos.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        
        self.gbOperaciones = QtWidgets.QGroupBox(self)
        self.gbOperaciones.setGeometry(QtCore.QRect(10, 410, 391, 71))
        self.gbOperaciones.setObjectName("gbOperaciones")

        self.pbInsertar = QtWidgets.QPushButton(self.gbOperaciones)
        self.pbInsertar.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.pbInsertar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_insertar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbInsertar.setIcon(icon)
        self.pbInsertar.setIconSize(QtCore.QSize(32, 32))
        self.pbInsertar.setObjectName("pbInsertar")
        # Establece función para cuando se desea insertar
        self.pbInsertar.clicked.connect(self.fnUsuarioInsertar) 
        

        self.pbEditar = QtWidgets.QPushButton(self.gbOperaciones)
        self.pbEditar.setGeometry(QtCore.QRect(140, 20, 111, 41))
        self.pbEditar.setFont(font)        
        icon.addPixmap(QtGui.QPixmap("img/icon_editar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbEditar.setIcon(icon)
        self.pbEditar.setIconSize(QtCore.QSize(32, 32))
        self.pbEditar.setObjectName("pbEditar")
         # Establece función para cuando se desea Modificar
        self.pbEditar.clicked.connect(self.fnUsuarioModificar) 

        self.pbEliminar = QtWidgets.QPushButton(self.gbOperaciones)
        self.pbEliminar.setGeometry(QtCore.QRect(270, 20, 111, 41))
        self.pbEliminar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_eliminar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbEliminar.setIcon(icon)
        self.pbEliminar.setIconSize(QtCore.QSize(32, 32))
        self.pbEliminar.setObjectName("pbEliminar")
        # Establece función para cuando va a eliminar el usuario
        self.pbEliminar.clicked.connect(self.fnUsuarioEliminar) 
        
        # Transacción
        self.gbTransaccion = QtWidgets.QGroupBox(self)
        self.gbTransaccion.setGeometry(QtCore.QRect(420, 410, 341, 71))
        self.gbTransaccion.setObjectName("gbTransaccion")
        self.pbCancelar = QtWidgets.QPushButton(self.gbTransaccion)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 20, 151, 41))
        self.pbCancelar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")
        # Establece función para cancelar transacción
        self.pbCancelar.clicked.connect(self.fnTransaccionCancelar) 
        

        self.pbAceptar = QtWidgets.QPushButton(self.gbTransaccion)
        self.pbAceptar.setGeometry(QtCore.QRect(180, 20, 151, 41))
        self.pbAceptar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setObjectName("pbAceptar")
        # Establece función para cuando acepta transacción
        self.pbAceptar.clicked.connect(self.fnTransaccionAceptar) 
        
        
        # Carga los usuarios
        self.fnCargaUsuarios()

        # Carga los Roles
        self.fnCargaRoles()

        # Carga los Procesos
        self.fnCargaProcesos()

        # Des Habilita Captura
        self.fnDesHabilitarCaptura(True)

        # Retranslada ???
        self.retranslate()

        # Conecta a los Slots ??????
        QtCore.QMetaObject.connectSlotsByName(self)

        #Termina la carga
        self.bCargando=False
        

    def retranslate(self):   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dlgUsuarios", "Sistema - Usuarios"))
        
        # Encabezado
        self.gbUsuario.setTitle(_translate("dlgUsuarios", "Usuario"))
        self.lblIdentificacion.setText(_translate("dlgUsuarios", "Identificación:"))
        self.lblUsuarios.setText(_translate("dlgUsuarios", "Usuarios:"))

        # Detalle
        self.gbDetalle.setTitle(_translate("dlgUsuarios", "Detalle"))
        self.lblPassword.setText(_translate("dlgUsuarios", "Password:"))
        self.lblConfirmar.setText(_translate("dlgUsuarios", "Confirmar:"))
        self.lblNombre.setText(_translate("dlgUsuarios", "Nombre:"))
        self.lblRol.setText(_translate("dlgUsuarios", "Rol:"))
        self.lblRoles.setText(_translate("dlgUsuarios", "Roles:"))

        # Operaciones
        self.gbOperaciones.setTitle(_translate("dlgUsuarios", "Operaciones"))
        self.pbInsertar.setText(_translate("dlgUsuarios", "Ins"))
        self.pbEditar.setText(_translate("dlgUsuarios", "Upd"))
        self.pbEliminar.setText(_translate("dlgUsuarios", "Del"))

        # Transacciones
        self.gbTransaccion.setTitle(_translate("dlgUsuarios", "Transacción"))
        self.pbCancelar.setText(_translate("dlgUsuarios", "Cancelar"))
        self.pbAceptar.setText(_translate("dlgUsuarios", "Aceptar"))
        
    # Función que habilita deshabilita captura
    def fnDesHabilitarCaptura(self,deshabilita):
        self.gbUsuario.setEnabled(deshabilita)
        self.gbDetalle.setEnabled(not deshabilita)
        self.gbOperaciones.setEnabled(deshabilita)
        self.gbTransaccion.setEnabled(not deshabilita)
        #Verifica a donde enviar el foco
        if (deshabilita):
            # Foco a Identificacion
            self.leIdentificacion.setFocus()
        else:
            # Foco a Nombre
            self.lePassword.setFocus()        

    # Función para cargar la información de Empresa
    def fnCargaUsuarios(self):
        # Obtiene la lista de Usuarios
        listaUsuarios = self.datUsuarios.fnUsuarioListaGet()

        #Iniciliza el Combo de usuarios
        self.cboUsuarios.clear()

        # Ciclo para cada usuarios
        for oUsuario in listaUsuarios:
            self.cboUsuarios.addItem(oUsuario.getStrUsuarioIde())

        # Deja sin seleccionar
        self.cboUsuarios.setCurrentIndex(-1)

    # Función para cargar la información de roles
    def fnCargaRoles(self):
        # Obtiene la lista de Roles
        listaRoles = self.datRolProcesos.fnRolesListaGet()

        #Iniciliza el Combo de usuarios
        self.cboRoles.clear()

        # Ciclo para cada rol
        for sRol in listaRoles:
            self.cboRoles.addItem(sRol)

        # Deja sin seleccionar
        self.cboRoles.setCurrentIndex(-1)
        
    # Función para cargar los Procesos
    def fnCargaProcesos(self):
        
        # Obtiene la lista de Procesos
        listaProcesos = self.datProcesos.fnListaProcesosGet()

        # Ciclo para cada proceso
        for oProceso in listaProcesos:
            self.listProcesos.addItem(oProceso.getStrProcesoIde())        

    # Función para desplegar información cuando un usuario se selecciona
    def fnUsuarioSeleccionado(self,textoActivo):

        # Verifica que no está cargando
        if (not self.bCargando):
        
            # Coloco el usuario seleccionado en el texto
            self.leIdentificacion.setText(textoActivo)
            
            # Crea un Objeto de usuarios
            oUsuario = eu.eUsuarios()

            # Obtiene información de un usuario por Ide
            oUsuario = self.datUsuarios.fnUsuarioGetByIde(textoActivo)

            # Coloca los datos en la pantalla
            self.leNombre.setText(oUsuario.getStrUsuarioName())
            self.lePassword.setText(oUsuario.getStrUsuarioPass())
            self.leRol.setText(oUsuario.getStrRoleName())   
            self.fnActivaRol(oUsuario.getStrRoleName())         
            self.leConfirmar.setText(oUsuario.getStrUsuarioPass())

    # Función para Des Seleccionar Procesos
    def fnDesSeleccionarProcesos(self):        
        #Ciclo para des-seleccionar todos los procesos
        for indice in range(self.listProcesos.count()):
            # Desselecciona
            self.listProcesos.item(indice).setSelected(False)

    # Función para Seleccionar procesos cuando un Rol es activado
    def fnRolSeleccionado(self,textoActivo):

        # Verifica que no está cargando
        if (not self.bCargando):

            # Verifica si es inserción o modificacion
            if (self.sOperacion==eg.eGlobales.OPERACION_INSERTAR or 
                self.sOperacion==eg.eGlobales.OPERACION_MODIFICAR):
                # Coloca el texto en la captura del Rol
                self.leRol.setText(self.cboRoles.currentText())


            # DesSelecciona los Procesos
            self.fnDesSeleccionarProcesos()    
                            
            # Obtiene la lista de los Procesos por Rol
            listaProcesos = self.datRolProcesos.fnProcesosListaGetByRol(textoActivo)

            # Ciclo para cada uno de los procsos
            for sProceso in listaProcesos:

                # Ciclo para cada Proceso en la lista
                for indice in range(self.listProcesos.count()):

                    # Compara
                    if (self.listProcesos.item(indice).text()==sProceso):

                        # Si es igual lo selecciona
                        self.listProcesos.item(indice).setSelected(True)
                        
                        # Salgo del Ciclo
                        break
            
            # En caso de que sea supervisor, deshabilita seleccionar
            if (self.cboRoles.currentText()=="supervisor"):
                self.listProcesos.setEnabled(False)
            else:
                self.listProcesos.setEnabled(True)   
                
    # Función para activar un Rol
    def fnActivaRol(self,rol):

        # Ciclo para recorrer el combo box
        for indice in range(self.cboRoles.count()):

            # Compara si es el rol para activarlo
            if (self.cboRoles.itemText(indice)==rol):

                # Si es igual lo activa
                self.cboRoles.setCurrentIndex(indice)

                #Sale del Ciclo
                break            

                
    
    # Función para validar los datos
    def fnValidaDatos(self):
        
        # Variable para el Mensaje
        sMensaje=""

        # Elimina espacios en blanco a la izquiera y derecha
        self.lePassword.setText(self.lePassword.text().strip())
        
        # Valida el Password
        if (len(self.lePassword.text())==0):
             # Coloca el dato en el Mensaje
             sMensaje ="El Password \n"
             # Coloca el foco en el password
             self.lePassword.setFocus()

        # Elimina espacios en blanco a la izquiera y derecha
        self.leConfirmar.setText(self.leConfirmar.text().strip())

        # Valida la confirmación
        if (len(self.leConfirmar.text())==0):
            
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
            
                # Coloca el Foco
                self.leConfirmar.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "La Confirmación \n"

        # Valida que el password y el confirma sean iguales
        if (self.lePassword.text()!=self.leConfirmar.text()):

            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
            
                # Coloca el Foco
                self.lePassword.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Password y la Confirmación no coinciden \n"

        # Elimina espacios en blanco a la izquiera y derecha
        self.leNombre.setText(self.leNombre.text().strip())
        
        # Valida el Nombre
        if (len(self.leNombre.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leNombre.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Nombre \n"    

        # Elimina espacios en blanco a la izquierda y derecha
        self.leRol.setText(self.leRol.text().strip())

        # Convierte a minúsculas
        self.leRol.setText(self.leRol.text().lower())

        # Valida el Rol
        if (len(self.leRol.text())==0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leRol.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "El Rol \n"    

        # # Valida que haya seleccionado por lo menos un proceso
        if (len(self.listProcesos.selectedItems())<=0):
            # Verifica si debe colocar el Foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.listProcesos.setFocus()

            # Agrega el dato en el Mensaje
            sMensaje = sMensaje + "De seleccionar por lo menos un Proceso \n"    

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

    # Función para Eliminar usuarios
    def fnUsuarioEliminar(self):

        # Elimina espacios
        self.leIdentificacion.setText(self.leIdentificacion.text().strip())

        # Convierte a minúsculas
        self.leIdentificacion.setText(self.leIdentificacion.text().lower())

        # Valida que haya algo capturado 
        if (self.leIdentificacion.text()!=""):

            # Valida que no sea admin
            if (self.leIdentificacion.text()!="admin"):

                #Valida que no sea el usuario ingresado
                if (self.leIdentificacion.text()!=eg.eGlobales.UsuarioIde):

                    # Valida que exista
                    if (self.datUsuarios.fnUsuarioExiste(self.leIdentificacion.text())):

                        # Coloca la operación a realizar
                        self.sOperacion=eg.eGlobales.OPERACION_ELIMINAR

                        # Deshabilita groupbox usuario
                        self.gbUsuario.setEnabled(False)
                        
                        # DesHabilitamos el groupbox de Operaciones
                        self.gbOperaciones.setEnabled(False)
                        
                        # Habilita el groupbox de Transacciones
                        self.gbTransaccion.setEnabled(True)
                        
                        # Coloca el foco en aceptar
                        self.pbAceptar.setFocus()

                    else:
                        
                        # Mensaje
                        fg.fnMensajeInformacion("La identificación a eliminar no existe","Seleccione otro")        
                        
                        # Coloca el foco en la Identificacion
                        self.leIdentificacion.setFocus() 
                else:
                    # Mensaje
                    fg.fnMensajeInformacion("No puedes eliminar el usuario con el que has ingresado","Seleccione otro")    
            else:
                # Mensaje
                fg.fnMensajeInformacion("El Usuario admin no puede ser eliminado","Seleccione otro")
        else:
            
            # Mensaje
            fg.fnMensajeInformacion("Debe capturar la Identificación a Eliminar","No deje vacío o con espacios")   
            # Coloca el foco en la Identificacion
            self.leIdentificacion.setFocus() 
    
    # Función que activa un usuario en el cboUsuarios
    def fnSeleccionaUsuario(self, usuario):

        # Ciclo para recorrer el combo box
        for indice in range(self.cboUsuarios.count()):

            # Compara si es el usuario para activarlo
            if (self.cboUsuarios.itemText(indice)==usuario):

                # Si es igual lo activa
                self.cboUsuarios.setCurrentIndex(indice)

                #Sale del Ciclo
                break    

    # Función para Insertar usuarios
    def fnUsuarioInsertar(self):

        # Elimina espacios
        self.leIdentificacion.setText(self.leIdentificacion.text().strip())

        # Convierte a minúsculas
        self.leIdentificacion.setText(self.leIdentificacion.text().lower())
        

        # Valida que haya algo capturado 
        if (self.leIdentificacion.text()!=""):

            # Valida que no sea admin
            if (self.leIdentificacion.text()!="admin"):
                
                # Valida que No exista
                if (not self.datUsuarios.fnUsuarioExiste(self.leIdentificacion.text())):

                    # Coloca la operación a realizar
                    self.sOperacion=eg.eGlobales.OPERACION_INSERTAR

                    # Deshabilita groupbox usuario
                    self.gbUsuario.setEnabled(False)
                    
                    # DesHabilitamos el groupbox de Operaciones
                    self.gbOperaciones.setEnabled(False)
                    
                    # Habilita el groupbox de Detalle
                    self.gbDetalle.setEnabled(True)
                    
                    # Habilita el groupbox de Transacciones
                    self.gbTransaccion.setEnabled(True)
                    
                    # Inicializa datos
                    self.fnInicializar(False)

                    # Coloca el foco en password
                    self.lePassword.setFocus()

                else:
                    # Selecciona el Usuario para ser Desplegado
                    self.fnSeleccionaUsuario(self.leIdentificacion.text())

                    # Mensaje
                    fg.fnMensajeInformacion("La identificación a insertar YA existe","Capture otra")        
                                            
                    # Coloca el foco en la Identificacion
                    self.leIdentificacion.setFocus() 
                
            else:
                # Mensaje
                fg.fnMensajeInformacion("El Usuario admin no puede ser insertado","Seleccione otro")
        else:
            
            # Mensaje
            fg.fnMensajeInformacion("Debe capturar la Identificación a Insertar","No deje vacío o con espacios")   
            # Coloca el foco en la Identificacion
            self.leIdentificacion.setFocus() 

    # Función para Modificar usuarios
    def fnUsuarioModificar(self):

        # Elimina espacios
        self.leIdentificacion.setText(self.leIdentificacion.text().strip())

        # Convierte a minúsculas
        self.leIdentificacion.setText(self.leIdentificacion.text().lower())
        
        # Valida que haya algo capturado 
        if (self.leIdentificacion.text()!=""):
                
            # Valida que Si exista
            if (self.datUsuarios.fnUsuarioExiste(self.leIdentificacion.text())):

                # Verifica si es admin para deshabilitar combo de Roles
                if (self.leIdentificacion.text()=="admin"):
                    
                    # Deshabilito combo y lineedit de Roles
                    self.cboRoles.setEnabled(False)
                    self.leRol.setEnabled(False)

                # Selecciona el Usuario para ser Desplegado
                self.fnSeleccionaUsuario(self.leIdentificacion.text())

                # Coloca la operación a realizar
                self.sOperacion=eg.eGlobales.OPERACION_MODIFICAR

                # Deshabilita groupbox usuario
                self.gbUsuario.setEnabled(False)
                
                # DesHabilitamos el groupbox de Operaciones
                self.gbOperaciones.setEnabled(False)
                
                # Habilita el groupbox de Detalle
                self.gbDetalle.setEnabled(True)
                
                # Habilita el groupbox de Transacciones
                self.gbTransaccion.setEnabled(True)
                                
                # Coloca el foco en password
                self.lePassword.setFocus()

            else:
            
                # Mensaje
                fg.fnMensajeInformacion("La identificación a modificar No existe","Capture otra")        
                                        
                # Coloca el foco en la Identificacion
                self.leIdentificacion.setFocus() 
                
        else:
            
            # Mensaje
            fg.fnMensajeInformacion("Debe capturar la Identificación a Modificar","No deje vacío o con espacios")   
            # Coloca el foco en la Identificacion
            self.leIdentificacion.setFocus()         
    
    # Función para inicializar datos
    def fnInicializar(self,borrarIde):
        # Inicializa Datos
        if (borrarIde):
            self.leIdentificacion.clear()
        self.leNombre.clear()
        self.lePassword.clear()
        self.leConfirmar.clear()
        self.leRol.clear()
        self.bCargando=True
        self.fnCargaUsuarios()
        self.fnCargaRoles()
        self.cboRoles.setCurrentIndex(-1)
        self.cboUsuarios.setCurrentIndex(-1)
        self.fnDesSeleccionarProcesos()
        self.bCargando=False
        # Habilita los procesos
        self.listProcesos.setEnabled(True)   
        # Habilita el combo de Roles
        self.cboRoles.setEnabled(True)
        self.leRol.setEnabled(True)

    # Función para cuando se cancela transacción
    def fnTransaccionCancelar(self):
        
        # Inicializar Datos
        self.fnInicializar(True)

        # Deshabilita Captura
        self.fnDesHabilitarCaptura(True)        

    # Función para cuando se acepta transacción
    def fnTransaccionAceptar(self):        

        # Verifica que operación es
        if (self.sOperacion==eg.eGlobales.OPERACION_ELIMINAR):

            # Intenta eliminar el usuario
            if (self.datUsuarios.fnUsuarioDel(self.leIdentificacion.text())):

                # Realiza transacción
                if (fbd.fnCommit()):

                    # Verifica mensaje de exito
                    if (eg.eGlobales.MensajesExito):

                        # Despliega el Mensaje
                        fg.fnMensajeInformacion("El Usuario ha sido eliminado","Ya no podrá ingresar al Sistema")

                    else:
                        
                        # Despliega Mensaje Emergente
                        fv.mensajeEmergente("El Usuario ha sido eliminado")    
                else:
                    # No se logró realizar la transacción
                    fg.fnMensajeInformacion("No se logró Confirmar Transacción","Avise al administrador")
            else:
                # No se logró realizar la transacción
                fg.fnMensajeInformacion("No se logró Eliminar el Usuario","Avise al administrador")

        elif (self.sOperacion==eg.eGlobales.OPERACION_INSERTAR):
                        
            # Valida datos
            if (self.fnValidaDatos()):

                # Variable para controlar si hubo error en transaccion
                bTransaccion = True

                # Crea un objeto Usuario
                oUsuario = eu.eUsuarios()

                #Coloca en el objeto los datos de la pantalla
                oUsuario.setStrUsuarioIde(self.leIdentificacion.text())
                oUsuario.setStrUsuarioName(self.leNombre.text())
                oUsuario.setStrUsuarioPass(self.lePassword.text())
                oUsuario.setStrRoleName(self.leRol.text())
                
                # Intenta Insertar el Usuario
                if (self.datUsuarios.fnUsuarioInsert(oUsuario)):

                    # Verifica si el Rol no es supervisor
                    if (self.leRol.text()!="supervisor"):

                        # Se intenta eliminar el rol-Procesos de la tabla si hay
                        if (self.datRolProcesos.fnRolProcesosDel(self.leRol.text())):
                          
                            # Ciclo para recorrer los Procesos Seleccionados
                            for proceso in self.listProcesos.selectedItems():
                                
                                # Inserta el Rol-Proceso
                                if (not self.datRolProcesos.fnRolProcesoIns(self.leRol.text(),proceso.text())):
                                    # No pudo insertar el proceso
                                    bTransaccion=False
                                    break
                                                        
                        else:
                            # Mensaje
                            fg.fnMensajeInformacion("Ocurrió un Error al eliminar Rol-Procesos","Verifique con el Administrador")        
                            bTransaccion = False
                                            
                else:
                    # Mensaje
                    fg.fnMensajeInformacion("Ocurrió un Error al Insertar el Usuario","Verifique con el Administrador")
                    bTransaccion=False

                # Verifica si debe realizar transacción
                if (bTransaccion):

                    # Intenta realizar transacción
                    if (fbd.fnCommit()):

                        # Verifica mensajes de Exito
                        if (eg.eGlobales.MensajesExito):

                            #Despliega el Mensaje
                            fg.fnMensajeInformacion("El Usuario ha sido Insertado","ya tiene acceso al Sistema")
                                
                    else:

                        # Mensaje
                        fg.fnMensajeInformacion("Ocurrió un Error en Transacción","Verifique con el administrador")
                        fbd.fnRollback()
                else:
                    # Cancela transacción
                    fbd.fnRollback()
                


                # Inicializar Datos
                self.fnInicializar(True)
                
                # Deshabilita Captura
                self.fnDesHabilitarCaptura(True)

        # La Operación es modificar obligatoriamente; no hay que verificar
        else:
            # Valida datos
            if (self.fnValidaDatos()):

                # Variable para controlar si hubo error en transaccion
                bTransaccion = True

                # Crea un objeto Usuario
                oUsuario = eu.eUsuarios()

                #Coloca en el objeto los datos de la pantalla
                oUsuario.setStrUsuarioIde(self.leIdentificacion.text())
                oUsuario.setStrUsuarioName(self.leNombre.text())
                oUsuario.setStrUsuarioPass(self.lePassword.text())
                oUsuario.setStrRoleName(self.leRol.text())
                
                # Intenta Modificar el Usuario
                if (self.datUsuarios.fnUsuarioUpdate(oUsuario)):

                    # Verifica si el Rol no es supervisor
                    if (self.leRol.text()!="supervisor"):

                        # Se intenta eliminar el rol-Procesos de la tabla si hay
                        if (self.datRolProcesos.fnRolProcesosDel(self.leRol.text())):
                          
                            # Ciclo para recorrer los Procesos Seleccionados
                            for proceso in self.listProcesos.selectedItems():
                                
                                # Inserta el Rol-Proceso
                                if (not self.datRolProcesos.fnRolProcesoIns(self.leRol.text(),proceso.text())):
                                    # No pudo insertar el proceso
                                    bTransaccion=False
                                    break
                                                        
                        else:
                            # Mensaje
                            fg.fnMensajeInformacion("Ocurrió un Error al eliminar Rol-Procesos","Verifique con el Administrador")        
                            bTransaccion = False
                                            
                else:
                    # Mensaje
                    fg.fnMensajeInformacion("Ocurrió un Error al Modificar el Usuario","Verifique con el Administrador")
                    bTransaccion=False

                # Verifica si debe realizar transacción
                if (bTransaccion):

                    # Intenta realizar transacción
                    if (fbd.fnCommit()):

                        # Verifica mensajes de Exito
                        if (eg.eGlobales.MensajesExito):

                            #Despliega el Mensaje
                            fg.fnMensajeInformacion("El Usuario ha sido Modificado","Los nuevos datos han sido registrados")

                        # Verifica si es el usuario ingresado
                        if (self.leIdentificacion.text()==eg.eGlobales.UsuarioIde):
                            # Mensaje al usuario ingresado que ha modificado su cuenta
                            fg.fnMensajeInformacion("Has modificado tu Acceso","Los datos surtirán efecto al reingresar al Sistema")
                                
                    else:

                        # Mensaje
                        fg.fnMensajeInformacion("Ocurrió un Error en Transacción","Verifique con el administrador")
                        fbd.fnRollback()
                else:
                    # Cancela transacción
                    fbd.fnRollback()            

                # Inicializar Datos
                self.fnInicializar(True)
                
                # Deshabilita Captura
                self.fnDesHabilitarCaptura(True)
        
# Función main
if __name__ == '__main__':

    # Importa la librería sys
    import sys

    # Crea el Objeto de la Aplicación
    app = QtWidgets.QApplication(sys.argv)

     # Intentamos conectar al Servidor y a la Base de Datos
    if (fbd.fnConexionServidor()):  

        # Crea el objeto para el Dialogo de Usuarios
        dialog = dlgUsuarios()

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        sys.exit(dialog.exec_())

    else:
        # Cierra el diálogo
        sys.exit(-1)