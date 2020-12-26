#   ------------------------------------------------------------------------------------------------------------
#   ventana funcional llamando a un archivo.ui
#    buscar lo siguiente en youtube.
#  Python Curso V2: 462 2/2 Cargar un Archivo de Interfaz Grafica de Usuario
#   ------------------------------------------------------------------------------------------------------------
    
import sys
from PyQt5.QtWidgets  import QApplication, QMainWindow, QPushButton, QMessageBox, QDialog

from PyQt5 import uic    # es para importar los archivos ui
    
import entidades.catalogos.entProveedores  as ep
import modelo.catalogos.modProveedores     as mp
import funciones.funcGrales                as fg
import entidades.entGlobales               as eg
import funciones.funcBaseDatos             as fbd
import funciones.funcVentanas              as fv
#import clases.claReportes                  as cr
#import clases.claExportar                  as ce

# Constantes
INT_COL_ID         = 0
INT_COL_NIF        = 1
INT_COL_NOMBRE     = 2
INT_COL_DIRECCION  = 3
INT_COL_POSTAL     = 4
INT_COL_POBLACION  = 5
INT_COL_PROVINCIA  = 6
INT_COL_PAIS       = 7
INT_COL_TELEFONO   = 8
INT_COL_MOVIL      = 9
INT_COL_EMAIL      = 10
INT_COL_WEB        = 11



class Aplicacion(QDialog):    

    def __init__(self):
        super().__init__()
        self.inicializarGui()
        
    def inicializarGui(self):
        uic.loadUi('ui/dlgProv.ui', self)   # el achivo va con la extencion.
        
        self.tblProveedores.setColumnWidth(INT_COL_ID,150)
        self.tblProveedores.setColumnWidth(INT_COL_NIF,150)
        self.tblProveedores.setColumnWidth(INT_COL_NOMBRE,300)
        self.tblProveedores.setColumnWidth(INT_COL_DIRECCION,350)
        self.tblProveedores.setColumnWidth(INT_COL_POSTAL,150)
        self.tblProveedores.setColumnWidth(INT_COL_POBLACION,150)
        self.tblProveedores.setColumnWidth(INT_COL_PROVINCIA,150)
        self.tblProveedores.setColumnWidth(INT_COL_PAIS,150)
        self.tblProveedores.setColumnWidth(INT_COL_TELEFONO,150)
        self.tblProveedores.setColumnWidth(INT_COL_MOVIL,150)
        self.tblProveedores.setColumnWidth(INT_COL_EMAIL,250)
        self.tblProveedores.setColumnWidth(INT_COL_WEB,350)


            
            # AQUI EL CODIGO         
    # =============================       Cargar Proveedores a la Tabla    CURSO 56  MINUTO 11
    def fnCargarProveedores(self):

         # Obtiene lo que tenga filtrar
        filtro = self.leFiltrar.text()

        # Obtiene la Lista de Proveedores
        lstProveedores = self.datProveedores.fnProveedorLista(filtro)

        # Coloca el Numero de Renglones en la tabla  primero a 0
        self.tblProveedores.setRowCount(0)
        self.tblProveedores.setRowCount(len(lstProveedores))

        # Variable para el Renglon
        renglon = 0

        # Ciclo para colocar los Proveedores
        for Proveedor in lstProveedores:
            # Se colcoa en la tabla los datos
            # Obtengo el Item
            item = self.fnCreaItem(str(Proveedor.getProveedor_id()))
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            item.setBackground(QtGui.QColor(248, 240, 244))
            item.setForeground(QtGui.QColor(255, 0, 0))
            self.tblProveedores.setItem(renglon,
                                        INT_COL_ID,
                                        item)

            item = self.fnCreaItem(str(Proveedor.getNif()))
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

            self.tblProveedores.setItem(renglon,
                                        INT_COL_NIF,
                                        item)
       
            self.tblProveedores.setItem(renglon,
                                        INT_COL_NOMBRE,
                                        self.fnCreaItem(str(Proveedor.getNombre())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_DIRECCION,
                                        self.fnCreaItem(str(Proveedor.getDireccion())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_POSTAL,
                                        self.fnCreaItem(str(Proveedor.getCodigoPostal())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_POBLACION,
                                        self.fnCreaItem(str(Proveedor.getPoblacion())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_PROVINCIA,
                                        self.fnCreaItem(str(Proveedor.getProvincia())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_PAIS,
                                        self.fnCreaItem(str(Proveedor.getPais())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_TELEFONO,
                                        self.fnCreaItem(str(Proveedor.getTelefono())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_MOVIL,
                                        self.fnCreaItem(str(Proveedor.getMovil())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_EMAIL,
                                        self.fnCreaItem(str(Proveedor.getEmail())))

            self.tblProveedores.setItem(renglon,
                                        INT_COL_WEB,
                                        self.fnCreaItem(str(Proveedor.getWeb())))


            # Incrementa el Renglon
            renglon = renglon + 1

            # Función para crear un item en base a datos
    def fnCreaItem(self,elDato):
        
        #Creo el Item        
        item = QtWidgets.QTableWidgetItem()
        
        # Se le coloca el dato
        item.setText(elDato)
        
        # Retorno el Item
        return item
        
    # Función para controlar boton insertar proveedores    
    def pbInsertarProveedor_click(self):
        
        # Crea el objeto para el Dialogo de Parámetros
        dialog = vista.catalogos.dlgProveedoresAC.dlgProveedoresAC("")

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()

         # Carga los Proveedores #NOTA
        self.fnCargarProveedores()

         # Crea el Objeto de la Ventana Emergenet
        fv.mensajeEmergente("Actualizando Proveedores ...")    

    # Función para controlar boton Editar
    def pbEditarProveedor_click(self):    
        # Obtiene los indices
        indexes = self.tblProveedores.selectionModel().selectedRows()

        # Obtiene el numero de Renglones seleccionados
        renSeleccionados = len(indexes)

        # Verifica si es mayor que 0
        if (renSeleccionados > 0):    
            # Obtengo el Indice del Row Seleccionado                
            renSeleccionado = indexes[0].row() # El 0 es el único

            # Obtengo el item de la tabla
            item = self.tblProveedores.item(renSeleccionado,INT_COL_ID)

            # Obtengo el valor del NIF para eliminar
            idProveedor = item.text()        

            # Crea el objeto para el Dialogo de Parámetros
            dialog = vista.catalogos.dlgProveedoresAC.dlgProveedoresAC(idProveedor)

            # Muestra el Diálogo
            dialog.show()

            #Lanza la aplicación
            dialog.exec_()

            # Carga los Proveedores
            self.fnCargarProveedores()     

            # Crea el Objeto de la Ventana Emergenet
            fv.mensajeEmergente("Actualizando Proveedores ...")       
            

        else:
            # Despliega el MessageBox
            fg.fnMensajeInformacion("Módulo Proveedores","Debe seleccionar un Proveedor para Editar")    
        
    # Función para controlar la Eliminación del Proveedor    
    def pbEliminarProveedor_click(self):
        # Obtiene el numero de Renglones seleccionados
        indexes = self.tblProveedores.selectionModel().selectedRows()
        renSeleccionados = len(indexes)

        # Verifica si es mayor que 0
        if (renSeleccionados > 0):            

            # Solicita confirmación
            confirmacion = fg.fnMensajeConfirmacion("Módulo Proveedores","Por favor confirme la eliminación del Registro")    

            # verifica
            if (confirmacion == QtWidgets.QMessageBox.Ok):

                # Obtengo el Indice del Row Seleccionado                
                renSeleccionado = indexes[0].row() # El 0 es el único

                # Obtengo el item de la tabla
                item = self.tblProveedores.item(renSeleccionado,INT_COL_ID)

                # Obtengo el valor del NIF para eliminar
                idProveedor = int(item.text())
                
                # Ejecutando el borrado
                if (self.datProveedores.fnProveedorDel(idProveedor)):
                    
                    # Mensaje de que registro se ha eliminado
                    fg.fnMensajeInformacion("Modulo Proveedores","El Registro ha sido eliminado")    
                    
                    # Carga de Nuevo los Proveedores
                    self.fnCargarProveedores()

                    # Crea el Objeto de la Ventana Emergenet
                    fv.mensajeEmergente("Actualizando Proveedores ...")
                        
        else:
            # Despliega el MessageBox
            fg.fnMensajeInformacion("Módulo Proveedores","Debe seleccionar un Proveedor para Eliminar")    
        
    def pbFiltrar_click(self):
        # Cargao de Nueva Cuenta Proveedores
        self.fnCargarProveedores()

    def pbExportarProveedores_click(self):
        # Crea el objeto de Exportar
        oReporte = ce.claExportar("proveedores.xls",
                                 self.tblProveedores)

        # Abre el Archivo
        oReporte.abrir()

    def pbImprimirProveedores_click(self):
        # Crea el objeto de Exportar
        oReporte = cr.claReportes("rptProveedores.html",
                                  "Sistema de Punto de Venta",
                                  "Reporte de Proveedores",
                                   self.leFiltrar.text(),
                                   self.tblProveedores)

        # Despliega el Reporte
        oReporte.desplegar()  

    def pbCerrarProveedores_click(self):
        # Cierra la ventana
        self.subWndProveedores.close()
        

    def tblProveedores_click(self, row, col):        
        
        # Obtengo el item de la tabla
        item = self.tblProveedores.item(row,INT_COL_ID)

        # Obtengo el valor del NIF para eliminar
        idProveedor = item.text()        

        # Crea el objeto para el Dialogo de ProveedoresAC
        dialog = vista.catalogos.dlgProveedoresAC.dlgProveedoresAC(idProveedor)

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()  

        # Carga de Nuevo los Proveedores
        self.fnCargarProveedores()

        # Crea el Objeto de la Ventana Emergenet
        fv.mensajeEmergente("Actualizando Proveedores ...")                              




    


         # ===============================================================
        # Carga los Datos de la Empresa
        self.fnCargaProveedores()        







    def retranslate(self):   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dlgProveedores", "Sistema - Empresa"))
        self.gbEmpresa.setTitle(_translate("dlgProveedores", "Datos"))
        self.lblNombre.setText(_translate("dlgProveedores", "Nombre:"))
        self.lblDireccion.setText(_translate("dlgProveedores", "Dirección:"))
        self.lblTelefono.setText(_translate("dlgProveedores", "Teléfono:"))
        self.lblRfc.setText(_translate("dlgProveedores", "RFC:"))
        self.lblSerial.setText(_translate("dlgProveedores", "Serial:"))
        self.lblLogo.setText(_translate("dlgProveedores", "Logo:"))
        self.pbCancelar.setText(_translate("dlgProveedores", "Cancelar"))
        self.pbAceptar.setText(_translate("dlgProveedores", "Aceptar"))

    # Función para cargar la información de Empresa
    def fnCargaProveedores(self):
        
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
        oEmpresa = ep.eProveedores()

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
# if __name__ == '__main__':

#     # Importa la librería sys
#     import sys

#     # Crea el Objeto de la Aplicación
#     app = QtWidgets.QApplication(sys.argv)

#      # Intentamos conectar al Servidor y a la Base de Datos
#     if (fbd.fnConexionServidor()):  

#         # Crea el objeto para el Dialogo de Empresa
#         dialog = dlgProveedores()

#         # Muestra el Diálogo
#         dialog.show()

#         #Lanza la aplicación
#         sys.exit(dialog.exec_())

#     else:
#         # Cierra el diálogo
#         sys.exit(-1)






def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


