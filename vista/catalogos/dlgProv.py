#   ------------------------------------------------------------------------------------------------------------
#   ventana funcional llamando a un archivo.ui
#    buscar lo siguiente en youtube.
#  Python Curso V2: 462 2/2 Cargar un Archivo de Interfaz Grafica de Usuario
#   ------------------------------------------------------------------------------------------------------------
    
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets  import *
#from PyQt5.QtWidgets  import QApplication, QMainWindow, QPushButton, QMessageBox, QDialog, QTableWidget, QTableWidgetItem
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
INT_COL_PROVEEDOR_ID   = 0
INT_COL_NIF            = 1
INT_COL_NOMBRE         = 2
INT_COL_DIRECCION      = 3
INT_COL_POSTAL         = 4
INT_COL_POBLACION      = 5
INT_COL_PROVINCIA      = 6
INT_COL_PAIS           = 7
INT_COL_TELEFONO       = 8
INT_COL_MOVIL          = 9
INT_COL_EMAIL          = 10
INT_COL_WEB            = 11

# Declaramos la clase Proveedores


class dlgProveedor(QDialog):    

    def __init__(self):
        super().__init__()
        self.inicializarGui()

        
        
    def inicializarGui(self):
        uic.loadUi('ui/dlgProv.ui', self)   # el achivo va con la extencion.ui

        self.setWindowTitle("Lista de Proveedores") 

        # Aqui damos el ancho a las columnas de tablewidgets 
        self.tblProveedores.setColumnWidth(INT_COL_PROVEEDOR_ID,50)
        self.tblProveedores.setColumnWidth(INT_COL_NIF,100)
        self.tblProveedores.setColumnWidth(INT_COL_NOMBRE,150)
        self.tblProveedores.setColumnWidth(INT_COL_DIRECCION,150)
        self.tblProveedores.setColumnWidth(INT_COL_POSTAL,100)
        self.tblProveedores.setColumnWidth(INT_COL_POBLACION,100)
        self.tblProveedores.setColumnWidth(INT_COL_PROVINCIA,100)
        self.tblProveedores.setColumnWidth(INT_COL_PAIS,100)
        self.tblProveedores.setColumnWidth(INT_COL_TELEFONO,100)
        self.tblProveedores.setColumnWidth(INT_COL_MOVIL,100)
        self.tblProveedores.setColumnWidth(INT_COL_EMAIL,150)
        self.tblProveedores.setColumnWidth(INT_COL_WEB,150)

        self.pbCerrarProveedores.clicked.connect(self.pbCerrarProveedores_click) 
        #self.pbInsertarProveedor.clicked.connect(self.pbInsertarProveedor_click)

        #print("Intentando cargar line 68")


        self.fnCargarProveedores()    
            # AQUI EL CODIGO         
    # ===================================  C A R G A R  P R O V E E D O R E S    a la Tabla   => CURSO 56  MINUTO 9
    def fnCargarProveedores(self):

        datProveedores = mp.mProveedores()


        #print("Lista de Proveedores ...")

        lstProveedores = datProveedores.fnProveedorLista()


        # for Proveedor in lstProveedores:
        #     print("Id            :",Proveedor.getProveedor_id())
        #     print("Nif           :",Proveedor.getNif())
        #     print("tipoIF        :",Proveedor.getTipoIF())
        #     print("Nombre        :",Proveedor.getNombre())
        #     print("Dirección     :",Proveedor.getDireccion())
        #     print("Código Postal :",Proveedor.getCodigoPostal())
        #     print("Población     :",Proveedor.getPoblacion())
        #     print("Provincia     :",Proveedor.getProvincia())
        #     print("País          :",Proveedor.getPais())
        #     print("Teléfono      :",Proveedor.getTelefono())
        #     print("Móvil         :",Proveedor.getMovil())
        #     print("Email         :",Proveedor.getEmail())
        #     print("Web           :",Proveedor.getWeb())


        
        # Borra los renglones y los pone en 0
        self.tblProveedores.setRowCount(0)

        #Coloca el Numero de Renglones que tiene la tabla 
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
                                        INT_COL_PROVEEDOR_ID,
                                        item)
            # print("Id            :",Proveedor.getProveedor_id())
            # print("Id            :",item)


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
        #print("dentro de la funcion crear item line 181")
        #Creo el Item        
        item = QtWidgets.QTableWidgetItem()
        
        # Se le coloca el dato
        item.setText(elDato)
        
        # Retorno el Item
        return item
        
    # =======================================  FIN C A R G A R  P R O V E E D O R E S ===========   
        #print("creo el item line 195")



    # Función para controlar boton insertar proveedores    
    def pbInsertarProveedor_click(self):

       
        
        # Crea el objeto para el Dialogo de Parámetros
        dialog = vista.catalogos.dlgProvAC.dlgProvAC("")

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
            dialog = vista.catalogos.dlgProvAC.dlgProvAC(idProveedor)

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
        print("Se cliqueo el boton cerrar")
        # Cierra la ventana
        self.close()
        
        

    def tblProveedores_click(self, row, col):        
        
        # Obtengo el item de la tabla
        item = self.tblProveedores.item(row,INT_COL_ID)

        # Obtengo el valor del NIF para eliminar
        idProveedor = item.text()        

        # Crea el objeto para el Dialogo de ProvAC
        dialog = vista.catalogos.dlgProvAC.dlgProvAC(idProveedor)

        # Muestra el Diálogo
        dialog.show()

        #Lanza la aplicación
        dialog.exec_()  

        # Carga de Nuevo los Proveedores
        self.fnCargarProveedores()

        # Crea el Objeto de la Ventana Emergenet
        fv.mensajeEmergente("Actualizando Proveedores ...")                              



def main():
    app = QApplication(sys.argv)
    ventana = dlgProveedor()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


