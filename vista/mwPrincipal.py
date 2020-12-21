# ----------------------------------------------------------------------
# mwPrincipal.py
# Ventana Principal del Sistema POS que presenta el Menu de Navegación

# prueba de commit en github 2

# ----------------------------------------------------------------------

# Librería de Python
import sys

# Importamos librerías de PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Importa librerías propietarias
import entidades.entGlobales           as eg
import entidades.sistema.entParametros as ep
import funciones.funcBaseDatos         as fbd
import funciones.funcVentanas          as fv
import modelo.sistema.modRolProcesos   as mrp
import modelo.sistema.modParametros    as mp
import modelo.sistema.modEmpresa       as me
import modelo.modBitacora              as mb
import modelo.catalogos.modClientes    as mc
import modelo.catalogos.modProductos   as mprod
import modelo.catalogos.modProveedores as mprov
import vista.dlgMensaje                as vm
import funciones.funcArchivo           as fa

# Dialogos a desplegar
import vista.sistema.dlgParametros
import vista.sistema.dlgEmpresa
import vista.sistema.dlgUsuarios



# Definición de la Clase Principal
class Ui_mwPrincipal(object):

    # Declaro variable para registro de Bitácora
    datBitacora = mb.mBitacora()
   
    # Definición del Método setup
    def setupUi(self, mwPrincipal):

        # Se define un objeto fon a ser utilizado
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)

        # Se define un objeto icono a ser utilizado
        icon = QtGui.QIcon()

        # Configuración de la Ventana Principal
        mwPrincipal.setObjectName("mwPrincipal")        
        mwPrincipal.resize(1197, 600)        
        mwPrincipal.setFont(font)        
        icon.addPixmap(QtGui.QPixmap("img/jsIco50x50.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mwPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mwPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        mwPrincipal.setCentralWidget(self.centralwidget)
        
        # Logo de la Empresa Centrada en la Imagen
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLogoEmpresa = QtWidgets.QLabel(self.centralwidget)
        self.lblLogoEmpresa.setText("")
        
        # Defino un objeto para consultar Empresa
        datEmpresa = me.mEmpresa()

        # Ejecuto la consulta para obtener el Logo
        sLogo = datEmpresa.fnEmpresaLogoGet()
        
        # Coloco el logo obtenido
        self.lblLogoEmpresa.setPixmap(QtGui.QPixmap(sLogo))

        self.lblLogoEmpresa.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lblLogoEmpresa.setObjectName("lblLogoEmpresa")
        self.verticalLayout.addWidget(self.lblLogoEmpresa)

        # Nombre de la Empresa Centrada en la Imagen
        self.lblNombreEmpresa = QtWidgets.QLabel(self.centralwidget)        
        font.setPointSize(16)
        font.setBold(True)
        self.lblNombreEmpresa.setFont(font)
        self.lblNombreEmpresa.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblNombreEmpresa.setObjectName("lblNombreEmpresa")
        self.verticalLayout.addWidget(self.lblNombreEmpresa)

        # Deja la fuente como estaba
        font.setPointSize(14)
        font.setBold(False)        


        # Crear el Menu Bar a la Ventana Principal
        self.mbPrincipal = QtWidgets.QMenuBar(mwPrincipal)
        self.mbPrincipal.setGeometry(QtCore.QRect(0, 0, 1197, 29))
        self.mbPrincipal.setFont(font)
        self.mbPrincipal.setObjectName("mbPrincipal")

        # Crea todos los Menus de la barra Principal
        # Sistema
        self.menuSistema = QtWidgets.QMenu(self.mbPrincipal)
        self.menuSistema.setObjectName("menuSistema")

        # Catalogo
        self.menuCatalogos = QtWidgets.QMenu(self.mbPrincipal)
        self.menuCatalogos.setObjectName("menuCatalogos")

        # Inventario
        self.menuInventario = QtWidgets.QMenu(self.mbPrincipal)
        self.menuInventario.setObjectName("menuInventario")

        # Reportes
        self.menuReportes = QtWidgets.QMenu(self.mbPrincipal)
        self.menuReportes.setObjectName("menuReportes")

        # Base de Datos
        self.menuBaseDatos = QtWidgets.QMenu(self.mbPrincipal)
        self.menuBaseDatos.setObjectName("menuBaseDatos")

        # Ayuda
        self.menuAyuda = QtWidgets.QMenu(self.mbPrincipal)
        self.menuAyuda.setObjectName("menuAyuda")

        # Coloca en la ventana principal el Menu Bar
        mwPrincipal.setMenuBar(self.mbPrincipal)

        # Crea el Status Bar y lo configura
        self.sbPrincipal = QtWidgets.QStatusBar(mwPrincipal)
        self.sbPrincipal.setObjectName("sbPrincipal")
        

        # Le agrega los botones al status bar
        #Agrega el botón de Año de Operación
        self.pbAñoOperacion = QtWidgets.QPushButton("Año:0000")
        self.pbAñoOperacion.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_calendario32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAñoOperacion.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbAñoOperacion)

        #Agrega el botón de Usuario
        self.pbUsuario = QtWidgets.QPushButton("Usuario:User")
        self.pbUsuario.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_user32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbUsuario.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbUsuario)

        #Agrega el botón de Proveedores
        self.pbProveedores = QtWidgets.QPushButton("Prov:0000")
        self.pbProveedores.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_proveedores32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbProveedores.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbProveedores)

        #Agrega el botón de Productos
        self.pbProductos = QtWidgets.QPushButton("Prod:0000")
        self.pbProductos.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_productos32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbProductos.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbProductos)

        #Agrega el botón de Clientes
        self.pbClientes = QtWidgets.QPushButton("Clientes:0000")
        self.pbClientes.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_clientes32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClientes.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbClientes)

        #Agrega el botón de Compras
        self.pbCompras = QtWidgets.QPushButton("Comp:0000")
        self.pbCompras.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_compras32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCompras.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbCompras)

        #Agrega el botón de Movimientos
        self.pbMovimientos = QtWidgets.QPushButton("Movi:0000")
        self.pbMovimientos.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_movimientos32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbMovimientos.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbMovimientos)

        #Agrega el botón de Ventas
        self.pbVentas = QtWidgets.QPushButton("Vtas:0|0000")
        self.pbVentas.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_ventas32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVentas.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbVentas)

        #Agrega el botón de Utilidades
        self.pbUtilidades = QtWidgets.QPushButton("Util:0.00")
        self.pbUtilidades.setFont(font)
        icon.addPixmap(QtGui.QPixmap("img/icon_utilidades32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbUtilidades.setIcon(icon)
        self.sbPrincipal.addWidget(self.pbUtilidades)

        # Agrega el Status Bar a la Ventana Principal y la configura
        mwPrincipal.setStatusBar(self.sbPrincipal)
        self.tbPrincipal = QtWidgets.QToolBar(mwPrincipal)
        self.tbPrincipal.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.tbPrincipal.setIconSize(QtCore.QSize(64, 64))
        self.tbPrincipal.setObjectName("tbPrincipal")
        mwPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.tbPrincipal)
        
        # Crea las acciones para agregarselas a la toolBar
        # Usuarios
        self.actionUsuarios = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_usuarios64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUsuarios.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionUsuarios.setFont(font)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionUsuarios.triggered.connect(self.fnDespliegaDialogoUsuarios)


        self.actionEmpresa = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_empresa64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmpresa.setIcon(icon)
        self.actionEmpresa.setFont(font)
        self.actionEmpresa.setObjectName("actionEmpresa")
        self.actionEmpresa.triggered.connect(self.fnDespliegaDialogoEmpresa)

        # Salida
        self.actionSalida = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_salida64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalida.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionSalida.setFont(font)
        self.actionSalida.setObjectName("actionSalida")
        self.actionSalida.triggered.connect(self.fnSalidaSistema)

        # Parámetros
        self.actionParametros = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_parametros64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionParametros.setIcon(icon)
        self.actionParametros.setFont(font)
        self.actionParametros.setObjectName("actionParametros")
        self.actionParametros.triggered.connect(self.fnDespliegaDialogoParametros)

        # Proveedores
        self.actionProveedores = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_proveedores64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProveedores.setIcon(icon)
        self.actionProveedores.setFont(font)
        self.actionProveedores.setObjectName("actionProveedores")
        self.actionProveedores.triggered.connect(self.fnCatalogoProveedores)
        
        # Productos
        self.actionProductos = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_productos64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductos.setIcon(icon)
        self.actionProductos.setFont(font)
        self.actionProductos.setObjectName("actionProductos")

        # Clientes
        self.actionClientes = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_clientes64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClientes.setIcon(icon)
        self.actionClientes.setFont(font)
        self.actionClientes.setObjectName("actionClientes")
        

        # Compras
        self.actionCompras = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_compras64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompras.setIcon(icon)
        self.actionCompras.setFont(font)
        self.actionCompras.setObjectName("actionCompras")

        # Movimientos
        self.actionMovimientos = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_movimientos64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMovimientos.setIcon(icon)
        self.actionMovimientos.setFont(font)
        self.actionMovimientos.setObjectName("actionMovimientos")
        self.actionVentas = QtWidgets.QAction(mwPrincipal)

        # Ventas
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_ventas64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVentas.setIcon(icon)
        self.actionVentas.setFont(font)
        self.actionVentas.setObjectName("actionVentas")
        self.actionRptCompras = QtWidgets.QAction(mwPrincipal)

        # Reporte de compras
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_rptcompras64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRptCompras.setIcon(icon)
        self.actionRptCompras.setFont(font)
        self.actionRptCompras.setObjectName("actionRptCompras")

        # Reporte de Movimientos
        self.actionRptMovimientos = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_rptmovimientos64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRptMovimientos.setIcon(icon)
        self.actionRptMovimientos.setFont(font)
        self.actionRptMovimientos.setObjectName("actionRptMovimientos")

        # Reporte de Ventas
        self.actionRptVentas = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_rptventas64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRptVentas.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionRptVentas.setFont(font)
        self.actionRptVentas.setObjectName("actionRptVentas")

        # Reporte de Bitácora
        self.actionRptBitacora = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_rptbitacora64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRptBitacora.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionRptBitacora.setFont(font)
        self.actionRptBitacora.setObjectName("actionRptBitacora")

        # Respaldos
        self.actionRespaldos = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_respaldos64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRespaldos.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionRespaldos.setFont(font)
        self.actionRespaldos.setObjectName("actionRespaldos")

        # Manual
        self.actionManual = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_manual64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManual.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionManual.setFont(font)
        self.actionManual.setObjectName("actionManual")

        # Acerca de
        self.actionAcerca_de = QtWidgets.QAction(mwPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon_acercade64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcerca_de.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.actionAcerca_de.setFont(font)
        self.actionAcerca_de.setObjectName("actionAcerca_de")

        # Agrega las acciones al Menu Sistema
        self.menuSistema.addAction(self.actionUsuarios)
        self.menuSistema.addAction(self.actionParametros)
        self.menuSistema.addSeparator()
        self.menuSistema.addAction(self.actionEmpresa)
        self.menuSistema.addSeparator()
        self.menuSistema.addAction(self.actionSalida)

        # Agrega las acciones al Menu Catálogos
        self.menuCatalogos.addAction(self.actionProveedores)
        self.menuCatalogos.addAction(self.actionProductos)
        self.menuCatalogos.addAction(self.actionClientes)

        # Agrega las acciones al Menu Inventario
        self.menuInventario.addAction(self.actionCompras)
        self.menuInventario.addAction(self.actionMovimientos)
        self.menuInventario.addAction(self.actionVentas)

        # Agrega las acciones al Menu Reportes
        self.menuReportes.addAction(self.actionRptCompras)
        self.menuReportes.addAction(self.actionRptMovimientos)
        self.menuReportes.addAction(self.actionRptVentas)
        self.menuReportes.addSeparator()
        self.menuReportes.addAction(self.actionRptBitacora)

        # Agrega las acciones al Menu Base de Datos
        self.menuBaseDatos.addAction(self.actionRespaldos)

        # Agrega las acciones al Menu Ayuda
        self.menuAyuda.addAction(self.actionManual)
        self.menuAyuda.addAction(self.actionAcerca_de)

        # Agrega las acciones a la toolBar
        self.mbPrincipal.addAction(self.menuSistema.menuAction())
        self.mbPrincipal.addAction(self.menuCatalogos.menuAction())
        self.mbPrincipal.addAction(self.menuInventario.menuAction())
        self.mbPrincipal.addAction(self.menuReportes.menuAction())
        self.mbPrincipal.addAction(self.menuBaseDatos.menuAction())
        self.mbPrincipal.addAction(self.menuAyuda.menuAction())
        self.tbPrincipal.addAction(self.actionSalida)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionEmpresa)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionParametros)
        self.tbPrincipal.addAction(self.actionUsuarios)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionProveedores)
        self.tbPrincipal.addAction(self.actionProductos)
        self.tbPrincipal.addAction(self.actionClientes)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionCompras)
        self.tbPrincipal.addAction(self.actionMovimientos)
        self.tbPrincipal.addAction(self.actionVentas)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionRptCompras)
        self.tbPrincipal.addAction(self.actionRptMovimientos)
        self.tbPrincipal.addAction(self.actionRptVentas)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionRptBitacora)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionRespaldos)
        self.tbPrincipal.addSeparator()
        self.tbPrincipal.addAction(self.actionManual)
        self.tbPrincipal.addAction(self.actionAcerca_de)

        # Configura el Acceso por Role
        self.fnConfigurarAccesoPorRole()

        # Carga parametros del Sistema
        self.fnCargaParametrosSistema()

        # Re Traslada ?
        self.retranslateUi(mwPrincipal)
        QtCore.QMetaObject.connectSlotsByName(mwPrincipal)
        
    # Definición de Función retranslateUi
    def retranslateUi(self, mwPrincipal):
        _translate = QtCore.QCoreApplication.translate
        
        # Variable para el título de la ventana
        tituloAplicacion = eg.eGlobales.SISTEMA+" "+eg.eGlobales.VERSION+" "+"Sucursal:"+eg.eGlobales.Sucursal
        tituloAplicacion = tituloAplicacion + " Terminal:" + eg.eGlobales.Terminal

        # Establece el Menu Principal
        mwPrincipal.setWindowTitle(_translate("mwPrincipal", tituloAplicacion))
        self.menuSistema.setTitle(_translate("mwPrincipal", "Sistema"))
        self.menuCatalogos.setTitle(_translate("mwPrincipal", "Catálogos"))
        self.menuInventario.setTitle(_translate("mwPrincipal", "Inventario"))
        self.menuReportes.setTitle(_translate("mwPrincipal", "Reportes"))
        self.menuBaseDatos.setTitle(_translate("mwPrincipal", "BaseDatos"))
        self.menuAyuda.setTitle(_translate("mwPrincipal", "Ayuda"))
        self.tbPrincipal.setWindowTitle(_translate("mwPrincipal", "toolBar"))
        
        self.actionUsuarios.setText(_translate("mwPrincipal", "Usuarios"))
        self.actionUsuarios.setToolTip(_translate("mwPrincipal", "Acceso a Altas, Bajas y Cambios de Usuarios"))
        self.actionUsuarios.setShortcut(_translate("mwPrincipal", "Alt+3"))
        
        self.actionEmpresa.setText(_translate("mwPrincipal", "Empresa"))
        self.actionEmpresa.setToolTip(_translate("mwPrincipal", "Acceso a Datos de la Empresa"))
        self.actionEmpresa.setShortcut(_translate("mwPrincipal", "Alt+1"))
        
        self.actionSalida.setText(_translate("mwPrincipal", "Salida"))
        self.actionSalida.setToolTip(_translate("mwPrincipal", "Salida del Sistema"))
        self.actionSalida.setShortcut(_translate("mwPrincipal", "Alt+0"))
        
        self.actionParametros.setText(_translate("mwPrincipal", "Parámetros"))
        self.actionParametros.setToolTip(_translate("mwPrincipal", "Acceso a Parámetros del Sistema"))
        self.actionParametros.setShortcut(_translate("mwPrincipal", "Alt+2"))
        
        self.actionProveedores.setText(_translate("mwPrincipal", "Proveedores"))
        self.actionProveedores.setToolTip(_translate("mwPrincipal", "Altas, Bajas y Cambios de Proveedores"))
        self.actionProveedores.setShortcut(_translate("mwPrincipal", "Alt+4"))

        self.actionProductos.setText(_translate("mwPrincipal", "Productos"))
        self.actionProductos.setToolTip(_translate("mwPrincipal", "Altas, Bajas y Cambios de Productos"))
        self.actionProductos.setShortcut(_translate("mwPrincipal", "Alt+5"))

        self.actionClientes.setText(_translate("mwPrincipal", "Clientes"))
        self.actionClientes.setToolTip(_translate("mwPrincipal", "Altas, Bajas y Cambios de Clientes"))
        self.actionClientes.setShortcut(_translate("mwPrincipal", "Alt+6"))

        self.actionCompras.setText(_translate("mwPrincipal", "Compras"))
        self.actionCompras.setToolTip(_translate("mwPrincipal", "Entradas de Inventario por Compras"))
        self.actionCompras.setShortcut(_translate("mwPrincipal", "Alt+7"))

        self.actionMovimientos.setText(_translate("mwPrincipal", "Movimientos"))
        self.actionMovimientos.setToolTip(_translate("mwPrincipal", "Entradas y Salidas de Inventario"))
        self.actionMovimientos.setShortcut(_translate("mwPrincipal", "Alt+8"))

        self.actionVentas.setText(_translate("mwPrincipal", "Ventas"))
        self.actionVentas.setToolTip(_translate("mwPrincipal", "Salidas por Ventas"))
        self.actionVentas.setShortcut(_translate("mwPrincipal", "Alt+9"))

        self.actionRptCompras.setText(_translate("mwPrincipal", "Compras"))
        self.actionRptCompras.setToolTip(_translate("mwPrincipal", "Reportes de Compras"))
        self.actionRptCompras.setShortcut(_translate("mwPrincipal", "Alt+A"))

        self.actionRptMovimientos.setText(_translate("mwPrincipal", "Movimientos"))
        self.actionRptMovimientos.setToolTip(_translate("mwPrincipal", "Reportes de Entradas y Salidas de Inventario"))
        self.actionRptMovimientos.setShortcut(_translate("mwPrincipal", "Alt+B"))

        self.actionRptVentas.setText(_translate("mwPrincipal", "Ventas"))
        self.actionRptVentas.setToolTip(_translate("mwPrincipal", "Reportes de Ventas"))
        self.actionRptVentas.setShortcut(_translate("mwPrincipal", "Alt+C"))

        self.actionRptBitacora.setText(_translate("mwPrincipal", "Bitácora"))
        self.actionRptBitacora.setToolTip(_translate("mwPrincipal", "Reportes de Bitacora"))
        self.actionRptBitacora.setShortcut(_translate("mwPrincipal", "Alt+D"))

        self.actionRespaldos.setText(_translate("mwPrincipal", "Respaldos"))
        self.actionRespaldos.setToolTip(_translate("mwPrincipal", "Respaldar y Restaurar Base de Datos"))
        self.actionRespaldos.setShortcut(_translate("mwPrincipal", "Alt+E"))

        self.actionManual.setText(_translate("mwPrincipal", "Manual"))
        self.actionManual.setToolTip(_translate("mwPrincipal", "Manual de Usuario del Sistema"))
        self.actionManual.setShortcut(_translate("mwPrincipal", "Alt+F"))

        self.actionAcerca_de.setText(_translate("mwPrincipal", "Acerca de ..."))
        self.actionAcerca_de.setToolTip(_translate("mwPrincipal", "Acerca de JAOR Software"))
        self.actionAcerca_de.setShortcut(_translate("mwPrincipal", "Alt+G"))

        # El nombre de la Empresa Centrado
        self.lblNombreEmpresa.setText(_translate("mwPrincipal", "Abarrotes 'La SuperMini'"))

    # Método para configurar el acceso al Sistema por medio del Role
    def fnConfigurarAccesoPorRole(self):
                
        # Declaramos un objeto del Módulo de RolProcesos
        datRolProcesos = mrp.mRolProcesos()

        # Verificamos cada una de las opciones del Sistema de acuerdo al Role
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Usuarios")):
            # Deshabilita
            self.actionUsuarios.setEnabled(False)

        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Parametros")):
            # Deshabilita
            self.actionParametros.setEnabled(False)
            
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Empresa")):
            # Deshabilita
            self.actionEmpresa.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Proveedores")):
            # Deshabilita
            self.actionProveedores.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Productos")):
            # Deshabilita
            self.actionProductos.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Clientes")):
            # Deshabilita
            self.actionClientes.setEnabled(False)

        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Compras")):
            # Deshabilita
            self.actionCompras.setEnabled(False)

        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Movimientos")):
            # Deshabilita
            self.actionMovimientos.setEnabled(False)
            
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Ventas")):
            # Deshabilita
            self.actionVentas.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"RptCompras")):
            # Deshabilita
            self.actionRptCompras.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"RptMovtos")):
            # Deshabilita
            self.actionRptMovimientos.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"RptVentas")):
            # Deshabilita
            self.actionRptVentas.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"RptBitacora")):
            # Deshabilita
            self.actionRptBitacora.setEnabled(False)
        
        if (not datRolProcesos.fnBoolRolProcesoExiste(eg.eGlobales.UsuarioRol,"Respaldos")):
            # Deshabilita
            self.actionRptBitacora.setEnabled(False)

    # Función para salir del sistema
    def fnSalidaSistema(self):

        # Crea un objeto Mensaje
        oMensaje = vm.dlgMensaje("Confirmar Salida","¿ Desea abandonar la Apliación ?",True)

        # Muestra el Mensaje
        oMensaje.show()

        # Lo lanza
        oMensaje.exec_()

        # Verifica la respuesta
        if (eg.eGlobales.BotonPresionado == eg.eGlobales.BOTON_ACEPTAR):

            # Crea el Objeto de la Ventana Emergenet
            fv.mensajeCentrado("Saliendo de la Aplicación ...",1)

            # Registro en Bitácora
            self.datBitacora.fnBitacoraRegistrar("Salida")

            # Cierra la conexión al Servidor
            fbd.fnConexionCerrar()

            # Cierra el Log
            fa.fnLogCierra()

            #Sale de la aplicación
            sys.exit(0)

    # Función desplegar el Diálogo de Parámetros
    def fnDespliegaDialogoParametros(self):
         
        # Crea el objeto para el Dialogo de Parámetros
        dialog = vista.sistema.dlgParametros.dlgParametros()

        # Verifico si debo registrar en la bitácora
        if (eg.eGlobales.BitacoraActiva):
            
            # Registro en Bitácora
            self.datBitacora.fnBitacoraRegistrar("Parametros")

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()

        # Actualizo los parámetros
        self.fnCargaParametrosSistema()

    # Función desplegar el Diálogo de Empresa
    def fnDespliegaDialogoEmpresa(self):
         
        # Crea el objeto para el Dialogo de Empresa
        dialog = vista.sistema.dlgEmpresa.dlgEmpresa()

        # Verifico si debo registrar en la bitácora
        if (eg.eGlobales.BitacoraActiva):
           
            # Registro en Bitácora
            self.datBitacora.fnBitacoraRegistrar("Empresa")

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()

        # Defino un objeto para consultar Empresa
        datEmpresa = me.mEmpresa()

        # Actualizo el Logo
        sLogo = datEmpresa.fnEmpresaLogoGet()

        # Coloco el logo obtenido
        self.lblLogoEmpresa.setPixmap(QtGui.QPixmap(sLogo))

    # Función desplegar el Diálogo de Usuarios
    def fnDespliegaDialogoUsuarios(self):
         
        # Crea el objeto para el Dialogo de Usuarios
        dialog = vista.sistema.dlgUsuarios.dlgUsuarios()

        # Verifico si debo registrar en la bitácora
        if (eg.eGlobales.BitacoraActiva):
           
            # Registro en Bitácora
            self.datBitacora.fnBitacoraRegistrar("Usuarios")

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()
        
    # Carga Parámetros del Sistema
    def fnCargaParametrosSistema(self):
        
        # Crea un objeto de Parámetros
        oParametros = ep.eParametros()

        # Crea el objeto para obtener información de los parámetros
        datParametros = mp.mParametros()

        # Ejecuta la obtención de los Parámetros
        oParametros = datParametros.fnParametrosGet()

        # Coloca los parámetros en las variables globales
        eg.eGlobales.MensajesExito = (True if (oParametros.getIntMensajesExito()==1) else False)
        eg.eGlobales.VerificarExistencias = (True if (oParametros.getIntVerificarExistencias()==1) else False)
        eg.eGlobales.AgruparProductos = (True if (oParametros.getIntAgruparProductos()==1) else False)
        eg.eGlobales.BitacoraActiva = (True if (oParametros.getIntBitacoraActiva()==1) else False)
        eg.eGlobales.ImprimirTicket = (True if (oParametros.getIntImprimirTicket()==1) else False)
        eg.eGlobales.MensajeTicket = oParametros.getStrMensajeTicket()
        eg.eGlobales.MonedaNombre  = oParametros.getStrMonedaNombre()
        eg.eGlobales.MonedaSimbolo = oParametros.getStrMonedaSimbolo()



        # -------------------------------------------------------------------------------------------------------

        # Carga la barra de estado  ---------------------------------------------------
        self.fnCargaInfoBarraEstado()

    # Carga la información en la barra de Estado
    def fnCargaInfoBarraEstado(self):

        # Coloca el año
        self.pbAñoOperacion.setText("Año:"+eg.eGlobales.AñoOperacion)

        # Coloca el Usuario
        self.pbUsuario.setText("Usuario:"+eg.eGlobales.UsuarioIde)

        # Declaro variable para los Provedores
        datProveedores = mprov.mProveedores()
    
        # Coloca el Numero de Proveedores Registrados
        self.pbProveedores.setText("Proveedores:"+str(datProveedores.fnProveedoresRegistrados()))

        # Declaro variable para los Productos
        datProductos = mprod.mProductos()
    
        # Coloca el Numero de Productos Registrados
        self.pbProductos.setText("Productos:"+str(datProductos.fnProductosRegistrados()))

        # Declaro variable para los Clientes
        datClientes = mc.mClientes()
    
        # Coloca el Numero de Clientes Registrados
        self.pbClientes.setText("Clientes:"+str(datClientes.fnClientesRegistrados()))



 # -----------------------------------------------------------------------------------------------------------

    # Función para desplegar Catálogo de Proveedores  ---------------------------------------------------------
    def fnCatalogoProveedores(self):

        # Obtiene las dimensiones de la Ventana
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        
        # Forma de Proveedores
        self.subWndProveedores = QtWidgets.QMdiSubWindow(self.centralwidget)

        # Establecemos titulo de la SubVentana
        self.subWndProveedores.setWindowTitle("          -- Lista de Proveedores --")     

        # La barra superior
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.subWndProveedores)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.centralwidget.geometry().width(), 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
    

        # Redimensiona la SubVentana con el ancho de la Ventana y el alto del central Widget                
        #self.subWndProveedores.resize(screen.width(),self.centralwidget.geometry().height())
        self.subWndProveedores.resize(self.centralwidget.geometry().width(),self.centralwidget.geometry().height())
        #self.subWndProveedores.show()
        self.subWndProveedores.showMaximized()


                  # texto en  botones dentro de la ventana
        self.pushButton_4.setText("Insertar")
        self.pushButton_3.setText("Editar")
        self.pushButton_2.setText("Eliminar")
        self.pushButton.setText("Buscar")
        self.pushButton_5.setText("Imprimir")
        self.pushButton_6.setText("Cerrar")
        
        

# Función main
if __name__ == "__main__":
    # Importa la libreria
    import sys

    # Crea la aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Verifica acceso al Servidor
    if (fbd.fnConexionServidor()):

        # Crea la ventana principal
        mwPrincipal = QtWidgets.QMainWindow()

        # Creal el objeto de la Clase
        ui = Ui_mwPrincipal()

        # Llama a setupUi con la ventana principal
        ui.setupUi(mwPrincipal)


        # Muestra la ventana
        mwPrincipal.showMaximized()

        # Crea el Objeto de la Ventana Emergenet
        window = fv.mensajeCentrado("Iniciando Aplicación ...Espere.")
        
        #Ejecuta la Aplicación
        sys.exit(app.exec_())
