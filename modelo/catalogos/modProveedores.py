# -----------------------------------------------------------------
# Clase mProveedores
# Modelo para obtener información referente a los Proveedores
# -----------------------------------------------------------------

# Importa las librerias
import entidades.entGlobales               as eg
import entidades.catalogos.entProveedores  as ep
import funciones.funcBaseDatos             as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_PROVEEDOR_ID = 0
INT_COL_NIF          = 1
INT_COL_TIPOIF       = 2
INT_COL_NOMBRE       = 3
INT_COL_DIRECCION    = 4
INT_COL_CODIGOPOSTAL = 5
INT_COL_POBLACION    = 6
INT_COL_PROVINCIA    = 7
INT_COL_PAIS         = 8
INT_COL_TELEFONO     = 9
INT_COL_MOVIL        = 10
INT_COL_EMAIL        = 11
INT_COL_WEB          = 12

# Definición de la Clase
class mProveedores:

    # Función para obtener cuantos Proveedores hay registrados
    def fnProveedoresRegistrados(self):

        # Crea una variable para el resultado
        resultado = -1

        # Prepara el Query para Consulta
        sQuery =  " SELECT count(*) FROM proveedores "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                resultado = registro[0]
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Resultado
        return resultado

    # Función para obtener información de un Proveedor
    def fnProveedorGet(self,identificacion:int):

        # Crea un objeto de Proveedor para retornar
        oProveedor = ep.eProveedores()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM Proveedores "
        sQuery += " WHERE Proveedor_id  = '"+str(identificacion)+"'"        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oProveedor.setProveedor_id(registro[INT_COL_PROVEEDOR_ID])
                oProveedor.setNif(registro[INT_COL_NIF])
                oProveedor.setTipoIF(registro[INT_COL_TIPOIF])
                oProveedor.setNombre(registro[INT_COL_NOMBRE])
                oProveedor.setDireccion(registro[INT_COL_DIRECCION])
                oProveedor.setCodigoPostal(registro[INT_COL_CODIGOPOSTAL])
                oProveedor.setPoblacion(registro[INT_COL_POBLACION])
                oProveedor.setProvincia(registro[INT_COL_PROVINCIA])
                oProveedor.setPais(registro[INT_COL_PAIS])
                oProveedor.setTelefono(registro[INT_COL_TELEFONO])
                oProveedor.setMovil(registro[INT_COL_MOVIL])
                oProveedor.setEmail(registro[INT_COL_EMAIL])
                oProveedor.setWeb(registro[INT_COL_WEB])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return oProveedor
    
    # Función que verifica que el Proveedor exista
    def fnProveedorExiste(self,identificacion:int):

        # Crea variable de resultado
        bResultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM proveedores "
        sQuery += " WHERE proveedor_id  = '"+str(identificacion)+"'"
        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Cambia la variable de Resultado
                bResultado = True
                
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return bResultado

    
    # Función para modificar un Proveedor
    def fnProveedorUpdate(self,oProveedor:ep.eProveedores):

        # Prepara el Query para Actualizar
        sQuery =  " UPDATE Proveedores "
        sQuery += " SET    nif           = '"+oProveedor.getNif()+"',"
        sQuery += "        tipoIF        = '"+oProveedor.getTipoIF()+"',"
        sQuery += "        nombre        = '"+oProveedor.getNombre()+"',"
        sQuery += "        direccion     = '"+oProveedor.getDireccion()+"',"
        sQuery += "        codigopostal  = '"+oProveedor.getCodigoPostal()+"',"
        sQuery += "        poblacion     = '"+oProveedor.getPoblacion()+"',"
        sQuery += "        provincia     = '"+oProveedor.getProvincia()+"',"
        sQuery += "        pais          = '"+oProveedor.getPais()+"',"
        sQuery += "        telefono      = '"+oProveedor.getTelefono()+"',"
        sQuery += "        movil         = '"+oProveedor.getMovil()+"',"
        sQuery += "        email         = '"+oProveedor.getEmail()+"',"
        sQuery += "        web           = '"+oProveedor.getWeb()+"'"
        sQuery += " WHERE  proveedor_id = " +str(oProveedor.getProveedor_id())

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para insertar un Proveedor
    def fnProveedorInsert(self,oProveedor:ep.eProveedores):

        # Prepara el Query para Actualizar
        sQuery =  " INSERT INTO Proveedores "
        sQuery += " (nif, tipoIF, nombre, direccion, codigopostal, poblacion, provincia,"
        sQuery += "  pais, telefono, movil, email, web) VALUES"
        sQuery += " ('"+oProveedor.getNif()+"',"
        sQuery += "  '"+oProveedor.getTipoIF()+"',"
        sQuery += "  '"+oProveedor.getNombre()+"',"
        sQuery += "  '"+oProveedor.getDireccion()+"',"
        sQuery += "  '"+oProveedor.getCodigoPostal()+"',"
        sQuery += "  '"+oProveedor.getPoblacion()+"',"
        sQuery += "  '"+oProveedor.getProvincia()+"',"
        sQuery += "  '"+oProveedor.getPais()+"',"
        sQuery += "  '"+oProveedor.getTelefono()+"',"
        sQuery += "  '"+oProveedor.getMovil()+"',"
        sQuery += "  '"+oProveedor.getEmail()+"',"
        sQuery += "  '"+oProveedor.getWeb()+"')"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para eliminar un Proveedor
    def fnProveedorDel(self,identificacion:int):

        # Prepara el Query para Actualizar
        sQuery =  " DELETE FROM Proveedores "
        sQuery += " WHERE  proveedor_id   = '"+str(identificacion)+"'"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para obtener los Proveedores
    def fnProveedorLista(self):

        # Objeto lista a devolver
        lstProveedores = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM Proveedores "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                oProveedor = ep.eProveedores()

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                oProveedor.setProveedor_id(registro[INT_COL_PROVEEDOR_ID])
                oProveedor.setNif(registro[INT_COL_NIF])
                oProveedor.setTipoIF(registro[INT_COL_TIPOIF])
                oProveedor.setNombre(registro[INT_COL_NOMBRE])
                oProveedor.setDireccion(registro[INT_COL_DIRECCION])
                oProveedor.setCodigoPostal(registro[INT_COL_CODIGOPOSTAL])
                oProveedor.setPoblacion(registro[INT_COL_POBLACION])
                oProveedor.setProvincia(registro[INT_COL_PROVINCIA])
                oProveedor.setPais(registro[INT_COL_PAIS])
                oProveedor.setTelefono(registro[INT_COL_TELEFONO])
                oProveedor.setMovil(registro[INT_COL_MOVIL])
                oProveedor.setEmail(registro[INT_COL_EMAIL])
                oProveedor.setWeb(registro[INT_COL_WEB])

                # Agrega el Proceso a la Lista
                lstProveedores.append(oProveedor)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstProveedores
    

# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Conectando al Servidor
    print("Conectando al Servidor ...")
    fbd.fnConexionServidor()

    # Declarando un objeto del Modelo
    datProveedores = mProveedores()

    # Ejecutando la Consulta de un Proveedor
    print("Proveedores Registrados:",datProveedores.fnProveedoresRegistrados())
    
    # Consultando existencia del Proveedor 0
    print("Existe Proveedor 0:",datProveedores.fnProveedorExiste(0))
    input("Presione para continuar ....")

    #Declaro un objeto de Proveedores y obtengo el Proveedor 0
    oProveedor = datProveedores.fnProveedorGet(0)

    print("Consultando Proveedor 0")
    print("Id            :",oProveedor.getProveedor_id())
    print("Nif           :",oProveedor.getNif())
    print("tipoIF        :",oProveedor.getTipoIF())
    print("Nombre        :",oProveedor.getNombre())
    print("Dirección     :",oProveedor.getDireccion())
    print("Código Postal :",oProveedor.getCodigoPostal())
    print("Población     :",oProveedor.getPoblacion())
    print("Provincia     :",oProveedor.getProvincia())
    print("País          :",oProveedor.getPais())
    print("Teléfono      :",oProveedor.getTelefono())
    print("Móvil         :",oProveedor.getMovil())
    print("Email         :",oProveedor.getEmail())
    print("Web           :",oProveedor.getWeb())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para insertar
    oProveedor.setNif("oerj656565")
    oProveedor.setTipoIF("RFC")
    oProveedor.setNombre("Juan Perez")
    oProveedor.setDireccion("Conocida")
    oProveedor.setCodigoPostal("12345")
    oProveedor.setPoblacion("Chetumal")
    oProveedor.setProvincia("Quintana Roo")
    oProveedor.setPais("México")
    oProveedor.setTelefono("123-56-7890")
    oProveedor.setMovil("321-65-0987")
    oProveedor.setEmail("jaorsoftware@mail.com")
    oProveedor.setWeb("www.jaorsoftware.com")
    
    # Inserto el Registro
    datProveedores.fnProveedorInsert(oProveedor)
    idInsertado = fbd.fnLastInsertId()
    print("Registro Insertado:",idInsertado)
    input("Presione enter para Consultarlo ...")

    print("Consultando Proveedor Insertado :",idInsertado)
    oProveedor = datProveedores.fnProveedorGet(idInsertado)
    print("Id            :",oProveedor.getProveedor_id())
    print("Nif           :",oProveedor.getNif())
    print("tipoIF        :",oProveedor.getTipoIF())
    print("Nombre        :",oProveedor.getNombre())
    print("Dirección     :",oProveedor.getDireccion())
    print("Código Postal :",oProveedor.getCodigoPostal())
    print("Población     :",oProveedor.getPoblacion())
    print("Provincia     :",oProveedor.getProvincia())
    print("País          :",oProveedor.getPais())
    print("Teléfono      :",oProveedor.getTelefono())
    print("Móvil         :",oProveedor.getMovil())
    print("Email         :",oProveedor.getEmail())
    print("Web           :",oProveedor.getWeb())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para actualizar
    oProveedor.setProveedor_id(idInsertado)
    oProveedor.setNif("oerj124")
    oProveedor.setTipoIF("CIF")
    oProveedor.setNombre("Juan Perez Ext")
    oProveedor.setDireccion("Conocida Ext")
    oProveedor.setCodigoPostal("89098")
    oProveedor.setPoblacion("Chetumal Ext")
    oProveedor.setProvincia("Quintana Roo Ext")
    oProveedor.setPais("USA")
    oProveedor.setTelefono("904-456-7890")
    oProveedor.setMovil("999-00-0000")
    oProveedor.setEmail("jaorsoftware@gmail.com")
    oProveedor.setWeb("www.jaorsoftwareExt.com")

    # Modificamos
    datProveedores.fnProveedorUpdate(oProveedor)

    print("Consultando Proveedor Modificado:",idInsertado)
    oProveedor = datProveedores.fnProveedorGet(idInsertado)
    print("Id            :",oProveedor.getProveedor_id())
    print("Nif           :",oProveedor.getNif())
    print("tipoIF        :",oProveedor.getTipoIF())
    print("Nombre        :",oProveedor.getNombre())
    print("Dirección     :",oProveedor.getDireccion())
    print("Código Postal :",oProveedor.getCodigoPostal())
    print("Población     :",oProveedor.getPoblacion())
    print("Provincia     :",oProveedor.getProvincia())
    print("País          :",oProveedor.getPais())
    print("Teléfono      :",oProveedor.getTelefono())
    print("Móvil         :",oProveedor.getMovil())
    print("Email         :",oProveedor.getEmail())
    print("Web           :",oProveedor.getWeb())
    input("Presiona enter para continuar ...")

    # Borramos el Ciente 1
    datProveedores.fnProveedorDel(idInsertado)
    print("Proveedor Eliminado : ",idInsertado)    
    input("Presiona para continuar ...")

    # Consultando existencia del Proveedor 1
    print("Existe Proveedor :"+str(idInsertado),datProveedores.fnProveedorExiste(idInsertado))
    input("Presione para continuar ....")
    
    print("Lista de Proveedores ...")
    lstProveedores = datProveedores.fnProveedorLista()
    for Proveedor in lstProveedores:
        print("Id            :",Proveedor.getProveedor_id())
        print("Nif           :",Proveedor.getNif())
        print("tipoIF        :",Proveedor.getTipoIF())
        print("Nombre        :",Proveedor.getNombre())
        print("Dirección     :",Proveedor.getDireccion())
        print("Código Postal :",Proveedor.getCodigoPostal())
        print("Población     :",Proveedor.getPoblacion())
        print("Provincia     :",Proveedor.getProvincia())
        print("País          :",Proveedor.getPais())
        print("Teléfono      :",Proveedor.getTelefono())
        print("Móvil         :",Proveedor.getMovil())
        print("Email         :",Proveedor.getEmail())
        print("Web           :",Proveedor.getWeb())
    
    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
