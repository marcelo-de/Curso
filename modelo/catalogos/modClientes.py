# -----------------------------------------------------------------
# Clase mClientes
# Modelo para obtener información referente a los Clientes
# -----------------------------------------------------------------

# Importa las librerias
import entidades.entGlobales            as eg
import entidades.catalogos.entClientes  as ec
import funciones.funcBaseDatos          as fbd

# Constantes para las Columnas de la Tabla de Clientes
INT_COL_CLIENTE_ID   = 0
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
class mClientes:

    # Función para obtener cuantos Clientes hay registrados
    def fnClientesRegistrados(self):

        # Crea una variable para el resultado
        resultado = -1

        # Prepara el Query para Consulta
        sQuery =  " SELECT count(*) FROM clientes "

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

    # Función para obtener información de un Cliente
    def fnClienteGet(self,identificacion:int):

        # Crea un objeto de Usuarios para retornar
        oCliente = ec.eClientes()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM clientes "
        sQuery += " WHERE cliente_id  = '"+str(identificacion)+"'"        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oCliente.setCliente_id(registro[INT_COL_CLIENTE_ID])
                oCliente.setNif(registro[INT_COL_NIF])
                oCliente.setTipoIF(registro[INT_COL_TIPOIF])
                oCliente.setNombre(registro[INT_COL_NOMBRE])
                oCliente.setDireccion(registro[INT_COL_DIRECCION])
                oCliente.setCodigoPostal(registro[INT_COL_CODIGOPOSTAL])
                oCliente.setPoblacion(registro[INT_COL_POBLACION])
                oCliente.setProvincia(registro[INT_COL_PROVINCIA])
                oCliente.setPais(registro[INT_COL_PAIS])
                oCliente.setTelefono(registro[INT_COL_TELEFONO])
                oCliente.setMovil(registro[INT_COL_MOVIL])
                oCliente.setEmail(registro[INT_COL_EMAIL])
                oCliente.setWeb(registro[INT_COL_WEB])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return oCliente
    
    # Función que verifica que el cliente exista
    def fnClienteExiste(self,identificacion:int):

        # Crea variable de resultado
        bResultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM clientes "
        sQuery += " WHERE cliente_id  = '"+str(identificacion)+"'"
        

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

    
    # Función para modificar un Cliente
    def fnClienteUpdate(self,oCliente:ec.eClientes):

        # Prepara el Query para Actualizar
        sQuery =  " UPDATE clientes "
        sQuery += " SET    nif           = '"+oCliente.getNif()+"',"
        sQuery += "        tipoIF        = '"+oCliente.getTipoIF()+"',"
        sQuery += "        nombre        = '"+oCliente.getNombre()+"',"
        sQuery += "        direccion     = '"+oCliente.getDireccion()+"',"
        sQuery += "        codigopostal  = '"+oCliente.getCodigoPostal()+"',"
        sQuery += "        poblacion     = '"+oCliente.getPoblacion()+"',"
        sQuery += "        provincia      = '"+oCliente.getProvincia()+"',"
        sQuery += "        pais          = '"+oCliente.getPais()+"',"
        sQuery += "        telefono      = '"+oCliente.getTelefono()+"',"
        sQuery += "        movil         = '"+oCliente.getMovil()+"',"
        sQuery += "        email         = '"+oCliente.getEmail()+"',"
        sQuery += "        web           = '"+oCliente.getWeb()+"'"
        sQuery += " WHERE  cliente_id = " +str(oCliente.getCliente_id())

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para insertar un cliente
    def fnClienteInsert(self,oCliente:ec.eClientes):

        # Prepara el Query para Actualizar
        sQuery =  " INSERT INTO clientes "
        sQuery += " (nif, tipoIF, nombre, direccion, codigopostal, poblacion, provincia,"
        sQuery += "  pais, telefono, movil, email, web) VALUES"
        sQuery += " ('"+oCliente.getNif()+"',"
        sQuery += "  '"+oCliente.getTipoIF()+"',"
        sQuery += "  '"+oCliente.getNombre()+"',"
        sQuery += "  '"+oCliente.getDireccion()+"',"
        sQuery += "  '"+oCliente.getCodigoPostal()+"',"
        sQuery += "  '"+oCliente.getPoblacion()+"',"
        sQuery += "  '"+oCliente.getProvincia()+"',"
        sQuery += "  '"+oCliente.getPais()+"',"
        sQuery += "  '"+oCliente.getTelefono()+"',"
        sQuery += "  '"+oCliente.getMovil()+"',"
        sQuery += "  '"+oCliente.getEmail()+"',"
        sQuery += "  '"+oCliente.getWeb()+"')"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para eliminar un Cliente
    def fnClienteDel(self,identificacion:int):

        # Prepara el Query para Actualizar
        sQuery =  " DELETE FROM clientes "
        sQuery += " WHERE  cliente_id   = '"+str(identificacion)+"'"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para obtener los Clientes
    def fnClienteLista(self):

        # Objeto lista a devolver
        lstClientes = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM clientes "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                oCliente = ec.eClientes()

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                oCliente.setCliente_id(registro[INT_COL_CLIENTE_ID])
                oCliente.setNif(registro[INT_COL_NIF])
                oCliente.setTipoIF(registro[INT_COL_TIPOIF])
                oCliente.setNombre(registro[INT_COL_NOMBRE])
                oCliente.setDireccion(registro[INT_COL_DIRECCION])
                oCliente.setCodigoPostal(registro[INT_COL_CODIGOPOSTAL])
                oCliente.setPoblacion(registro[INT_COL_POBLACION])
                oCliente.setProvincia(registro[INT_COL_PROVINCIA])
                oCliente.setPais(registro[INT_COL_PAIS])
                oCliente.setTelefono(registro[INT_COL_TELEFONO])
                oCliente.setMovil(registro[INT_COL_MOVIL])
                oCliente.setEmail(registro[INT_COL_EMAIL])
                oCliente.setWeb(registro[INT_COL_WEB])

                # Agrega el Proceso a la Lista
                lstClientes.append(oCliente)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstClientes

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
    datClientes = mClientes()

    # Ejecutando la Consulta de un Usuario
    print("Clientes Registrados:",datClientes.fnClientesRegistrados())

    # Consultando existencia del Cliente 0
    print("Existe Cliente 0:",datClientes.fnClienteExiste(0))
    input("Presione para continuar ....")

    #Declaro un objeto de Clientes y obtengo el Cliente 0
    oCliente = datClientes.fnClienteGet(0)

    print("Consultando Cliente 0")
    print("Id            :",oCliente.getCliente_id())
    print("Nif           :",oCliente.getNif())
    print("tipoIF        :",oCliente.getTipoIF())
    print("Nombre        :",oCliente.getNombre())
    print("Dirección     :",oCliente.getDireccion())
    print("Código Postal :",oCliente.getCodigoPostal())
    print("Población     :",oCliente.getPoblacion())
    print("Provincia     :",oCliente.getProvincia())
    print("País          :",oCliente.getPais())
    print("Teléfono      :",oCliente.getTelefono())
    print("Móvil         :",oCliente.getMovil())
    print("Email         :",oCliente.getEmail())
    print("Web           :",oCliente.getWeb())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para insertar
    oCliente.setNif("oerj656565")
    oCliente.setTipoIF("RFC")
    oCliente.setNombre("Juan Perez")
    oCliente.setDireccion("Conocida")
    oCliente.setCodigoPostal("12345")
    oCliente.setPoblacion("Chetumal")
    oCliente.setProvincia("Quintana Roo")
    oCliente.setPais("México")
    oCliente.setTelefono("123-56-7890")
    oCliente.setMovil("321-65-0987")
    oCliente.setEmail("jaorsoftware@mail.com")
    oCliente.setWeb("www.jaorsoftware.com")
    
    # Inserto el Registro
    datClientes.fnClienteInsert(oCliente)
    idInsertado = fbd.fnLastInsertId()
    print("Registro Insertado:",idInsertado)
    input("Presione enter para Consultarlo ...")

    print("Consultando Cliente :",idInsertado)
    oCliente = datClientes.fnClienteGet(idInsertado)
    print("Id            :",oCliente.getCliente_id())
    print("Nif           :",oCliente.getNif())
    print("tipoIF        :",oCliente.getTipoIF())
    print("Nombre        :",oCliente.getNombre())
    print("Dirección     :",oCliente.getDireccion())
    print("Código Postal :",oCliente.getCodigoPostal())
    print("Población     :",oCliente.getPoblacion())
    print("Provincia     :",oCliente.getProvincia())
    print("País          :",oCliente.getPais())
    print("Teléfono      :",oCliente.getTelefono())
    print("Móvil         :",oCliente.getMovil())
    print("Email         :",oCliente.getEmail())
    print("Web           :",oCliente.getWeb())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para actualizar
    oCliente.setCliente_id(idInsertado)
    oCliente.setNif("oerj124")
    oCliente.setTipoIF("CIF")
    oCliente.setNombre("Juan Perez Ext")
    oCliente.setDireccion("Conocida Ext")
    oCliente.setCodigoPostal("89098")
    oCliente.setPoblacion("Chetumal Ext")
    oCliente.setProvincia("Quintana Roo Ext")
    oCliente.setPais("USA")
    oCliente.setTelefono("904-456-7890")
    oCliente.setMovil("999-00-0000")
    oCliente.setEmail("jaorsoftware@gmail.com")
    oCliente.setWeb("www.jaorsoftwareExt.com")

    # Modificamos
    datClientes.fnClienteUpdate(oCliente)

    print("Consultando Cliente:",idInsertado)
    oCliente = datClientes.fnClienteGet(idInsertado)
    print("Id            :",oCliente.getCliente_id())
    print("Nif           :",oCliente.getNif())
    print("tipoIF        :",oCliente.getTipoIF())
    print("Nombre        :",oCliente.getNombre())
    print("Dirección     :",oCliente.getDireccion())
    print("Código Postal :",oCliente.getCodigoPostal())
    print("Población     :",oCliente.getPoblacion())
    print("Provincia     :",oCliente.getProvincia())
    print("País          :",oCliente.getPais())
    print("Teléfono      :",oCliente.getTelefono())
    print("Móvil         :",oCliente.getMovil())
    print("Email         :",oCliente.getEmail())
    print("Web           :",oCliente.getWeb())
    input("Presiona enter para continuar ...")

    # Borramos el Ciente 1
    datClientes.fnClienteDel(idInsertado)
    print("Cliente Eliminado : ",idInsertado)    
    input("Presiona para continuar ...")

    # Consultando existencia del Cliente 1
    print("Existe Cliente :"+str(idInsertado),datClientes.fnClienteExiste(idInsertado))
    input("Presione para continuar ....")
    
    print("Lista de Clientes ...")
    lstClientes = datClientes.fnClienteLista()
    for Cliente in lstClientes:
        print("Id            :",Cliente.getCliente_id())
        print("Nif           :",Cliente.getNif())
        print("tipoIF        :",Cliente.getTipoIF())
        print("Nombre        :",Cliente.getNombre())
        print("Dirección     :",Cliente.getDireccion())
        print("Código Postal :",Cliente.getCodigoPostal())
        print("Población     :",Cliente.getPoblacion())
        print("Provincia     :",Cliente.getProvincia())
        print("País          :",Cliente.getPais())
        print("Teléfono      :",Cliente.getTelefono())
        print("Móvil         :",Cliente.getMovil())
        print("Email         :",Cliente.getEmail())
        print("Web           :",Cliente.getWeb())
        

    # # Confirmo transaccion
    fbd.fnCommit()
    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
