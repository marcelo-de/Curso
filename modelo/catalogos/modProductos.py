# -----------------------------------------------------------------
# Clase mProductos
# Modelo para obtener información referente a los Productos
# -----------------------------------------------------------------

# Importa las librerias
import entidades.entGlobales             as eg
import entidades.catalogos.entProductos  as ep
import funciones.funcBaseDatos           as fbd

# Constantes para las Columnas de la Tabla de Productos
INT_COL_PRODUCTO_IDE         = 0
INT_COL_PRODUCTO_CODIGO      = 1
INT_COL_TIPO_PRODUCTO        = 2
INT_COL_PRODUCTO_MARCA       = 3
INT_COL_PRODUCTO_NOMBRE      = 4
INT_COL_PRODUCTO_DESCRIPCION = 5
INT_COL_PRODUCTO_MEDIDA      = 6
INT_COL_PRODUCTO_INICIAL     = 7
INT_COL_PRODUCTO_ENTRADAS    = 8
INT_COL_PRODUCTO_SALIDAS     = 9
INT_COL_PRODUCTO_ACTUAL      = 10
INT_COL_PRODUCTO_COSTO       = 11
INT_COL_PRODUCTO_PRECIO      = 12
INT_COL_IMPUESTO_ID          = 13
INT_COL_PROVEEDOR_ID         = 14

# Definición de la Clase
class mProductos:

    # Función para obtener cuantos Productos hay registrados
    def fnProductosRegistrados(self):

        # Crea una variable para el resultado
        resultado = -1

        # Prepara el Query para Consulta
        sQuery =  " SELECT count(*) FROM productos "

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

    # Función para obtener información de un Producto
    def fnProductoGet(self,identificacion:int):

        # Crea un objeto de Productos para retornar
        oProducto = ep.eProductos()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM Productos "
        sQuery += " WHERE intProductoIde  = '"+str(identificacion)+"'"        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oProducto.setIntProductoIde(registro[INT_COL_PRODUCTO_IDE])
                oProducto.setStrProductoCodigo(registro[INT_COL_PRODUCTO_CODIGO])
                oProducto.setTipoProducto(registro[INT_COL_TIPO_PRODUCTO])
                oProducto.setStrProductoMarca(registro[INT_COL_PRODUCTO_MARCA])
                oProducto.setStrProductoNombre(registro[INT_COL_PRODUCTO_NOMBRE])
                oProducto.setStrProductoDescripcion(registro[INT_COL_PRODUCTO_DESCRIPCION])
                oProducto.setStrProductoMedida(registro[INT_COL_PRODUCTO_MEDIDA])
                oProducto.setIntProductoInicial(registro[INT_COL_PRODUCTO_INICIAL])
                oProducto.setIntProductoEntradas(registro[INT_COL_PRODUCTO_ENTRADAS])
                oProducto.setIntProductoSalidas(registro[INT_COL_PRODUCTO_SALIDAS])
                oProducto.setIntProductoActual(registro[INT_COL_PRODUCTO_ACTUAL])
                oProducto.setDecProductoCosto(registro[INT_COL_PRODUCTO_COSTO])
                oProducto.setDecProductoPrecio(registro[INT_COL_PRODUCTO_PRECIO])
                oProducto.setImpuesto_id(registro[INT_COL_IMPUESTO_ID])
                oProducto.setProveedor_id(registro[INT_COL_PROVEEDOR_ID])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return oProducto
    
    # Función que verifica que el Producto exista
    def fnProductoExiste(self,identificacion:int):

        # Crea variable de resultado
        bResultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM Productos "
        sQuery += " WHERE intProductoIde  = "+str(identificacion)
        

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

    
    # Función para modificar un Producto
    def fnProductoUpdate(self,oProducto:ep.eProductos):

        # Prepara el Query para Actualizar
        sQuery =  " UPDATE Productos "
        sQuery += " SET    strProductoCodigo        = '"+oProducto.getStrProductoCodigo()+"',"
        sQuery += "        tipoProducto             = '"+oProducto.getTipoProducto()+"',"
        sQuery += "        strProductoMarca         = '"+oProducto.getStrProductoMarca()+"',"
        sQuery += "        strProductoNombre        = '"+oProducto.getStrProductoNombre()+"',"
        sQuery += "        strProductoDescripcion   = '"+oProducto.getStrProductoDescripcion()+"',"
        sQuery += "        strProductoMedida        = '"+oProducto.getStrProductoMedida()+"',"
        sQuery += "        intProductoInicial       =  "+str(oProducto.getIntProductoInicial())+","
        sQuery += "        intProductoEntradas      =  "+str(oProducto.getIntProductoEntradas())+","
        sQuery += "        intProductoSalidas       =  "+str(oProducto.getIntProductoSalidas())+","
        sQuery += "        intProductoActual        =  "+str(oProducto.getIntProductoActual())+","
        sQuery += "        decProductoCosto         =  "+str(oProducto.getDecProductoCosto())+","
        sQuery += "        decProductoPrecio        =  "+str(oProducto.getDecProductoPrecio())+","
        sQuery += "        impuesto_id              =  "+str(oProducto.getImpuesto_id())+","
        sQuery += "        proveedor_id             =  "+str(oProducto.getProveedor_id())        
        sQuery += " WHERE  intProductoIde           =  "+str(oProducto.getIntProductoIde())

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para insertar un Producto
    def fnProductoInsert(self,oProducto:ep.eProductos):

        # Prepara el Query para Actualizar
        sQuery =  " INSERT INTO Productos "
        sQuery += " (strProductoCodigo, tipoProducto, strProductoMarca, strProductoNombre,"
        sQuery += "  strProductoDescripcion, strProductoMedida, intProductoInicial, "
        sQuery += "  intProductoEntradas, intProductoSalidas, intProductoActual, decProductoCosto,"
        sQuery += "  decProductoPrecio, impuesto_id, proveedor_id) VALUES"
        sQuery += " ('"+oProducto.getStrProductoCodigo()+"',"
        sQuery += "  '"+oProducto.getTipoProducto()+"',"
        sQuery += "  '"+oProducto.getStrProductoMarca()+"',"
        sQuery += "  '"+oProducto.getStrProductoNombre()+"',"
        sQuery += "  '"+oProducto.getStrProductoDescripcion()+"',"
        sQuery += "  '"+oProducto.getStrProductoMedida()+"',"
        sQuery += "   "+str(oProducto.getIntProductoInicial())+","
        sQuery += "   "+str(oProducto.getIntProductoEntradas())+","
        sQuery += "   "+str(oProducto.getIntProductoSalidas())+","
        sQuery += "   "+str(oProducto.getIntProductoActual())+","
        sQuery += "   "+str(oProducto.getDecProductoCosto())+","
        sQuery += "   "+str(oProducto.getDecProductoPrecio())+","
        sQuery += "   "+str(oProducto.getImpuesto_id())+","
        sQuery += "   "+str(oProducto.getProveedor_id())+")"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)        
    
        
    # Función para eliminar un Producto
    def fnProductoDel(self,identificacion:int):

        # Prepara el Query para Actualizar
        sQuery =  " DELETE FROM Productos "
        sQuery += " WHERE  intProductoIde = "+str(identificacion)

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para obtener los Productos
    def fnProductoLista(self):

        # Objeto lista a devolver
        lstProductos = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM Productos "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                oProducto = ep.eProductos()

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                oProducto.setIntProductoIde(registro[INT_COL_PRODUCTO_IDE])
                oProducto.setStrProductoCodigo(registro[INT_COL_PRODUCTO_CODIGO])
                oProducto.setTipoProducto(registro[INT_COL_TIPO_PRODUCTO])
                oProducto.setStrProductoMarca(registro[INT_COL_PRODUCTO_MARCA])
                oProducto.setStrProductoNombre(registro[INT_COL_PRODUCTO_NOMBRE])
                oProducto.setStrProductoDescripcion(registro[INT_COL_PRODUCTO_DESCRIPCION])
                oProducto.setStrProductoMedida(registro[INT_COL_PRODUCTO_MEDIDA])
                oProducto.setIntProductoInicial(registro[INT_COL_PRODUCTO_INICIAL])
                oProducto.setIntProductoEntradas(registro[INT_COL_PRODUCTO_ENTRADAS])
                oProducto.setIntProductoSalidas(registro[INT_COL_PRODUCTO_SALIDAS])
                oProducto.setIntProductoActual(registro[INT_COL_PRODUCTO_ACTUAL])
                oProducto.setDecProductoCosto(registro[INT_COL_PRODUCTO_COSTO])
                oProducto.setDecProductoPrecio(registro[INT_COL_PRODUCTO_PRECIO])
                oProducto.setImpuesto_id(registro[INT_COL_IMPUESTO_ID])
                oProducto.setProveedor_id(registro[INT_COL_PROVEEDOR_ID])

                # Agrega el Proceso a la Lista
                lstProductos.append(oProducto)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstProductos

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
    datProductos = mProductos()

    # Ejecutando la Consulta de un Usuario
    print("Productos Registrados:",datProductos.fnProductosRegistrados())

    # Consultando existencia del Producto 0
    print("Existe Producto 0:",datProductos.fnProductoExiste(0))
    input("Presione para continuar ....")

    #Declaro un objeto de Producto y obtengo el Cliente 0
    oProducto = datProductos.fnProductoGet(0)

    print("Consultando Producto 0")
    print("Ide         :",oProducto.getIntProductoIde())
    print("Codigo      :",oProducto.getStrProductoCodigo())
    print("Tipo        :",oProducto.getTipoProducto())
    print("Marca       :",oProducto.getStrProductoMarca())
    print("Nombre      :",oProducto.getStrProductoNombre())
    print("Descripción :",oProducto.getStrProductoDescripcion())
    print("Medida      :",oProducto.getStrProductoMedida())
    print("Inicial     :",oProducto.getIntProductoInicial())
    print("Entradas    :",oProducto.getIntProductoEntradas())
    print("Salidas     :",oProducto.getIntProductoSalidas())
    print("Actual      :",oProducto.getIntProductoActual())
    print("Costo       :",oProducto.getDecProductoCosto())
    print("Precio      :",oProducto.getDecProductoPrecio())
    print("Impuesto    :",oProducto.getImpuesto_id())
    print("Proveedor   :",oProducto.getProveedor_id())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para insertar
    oProducto.setStrProductoCodigo("AB123345_23")
    oProducto.setTipoProducto("CERVEZAS")
    oProducto.setStrProductoMarca("CORONA")
    oProducto.setStrProductoNombre("Coronita 250")
    oProducto.setStrProductoDescripcion("Coronita 25o ml envase cristal")
    oProducto.setStrProductoMedida("Pza")
    oProducto.setIntProductoInicial(10)
    oProducto.setIntProductoEntradas(5)
    oProducto.setIntProductoSalidas(3)
    oProducto.setIntProductoActual(12)
    oProducto.setDecProductoCosto(8.30)
    oProducto.setDecProductoPrecio(12.30)
    oProducto.setImpuesto_id(2)
    oProducto.setProveedor_id(0)
    
    # Inserto el Registro
    datProductos.fnProductoInsert(oProducto)
    idInsertado = fbd.fnLastInsertId()
    print("Registro Insertado:",idInsertado)
    input("Presione enter para Consultarlo ...")

    print("Consultando Producto Insertado:",idInsertado)
    oProducto = datProductos.fnProductoGet(idInsertado)
    print("Ide         :",oProducto.getIntProductoIde())
    print("Codigo      :",oProducto.getStrProductoCodigo())
    print("Tipo        :",oProducto.getTipoProducto())
    print("Marca       :",oProducto.getStrProductoMarca())
    print("Nombre      :",oProducto.getStrProductoNombre())
    print("Descripción :",oProducto.getStrProductoDescripcion())
    print("Medida      :",oProducto.getStrProductoMedida())
    print("Inicial     :",oProducto.getIntProductoInicial())
    print("Entradas    :",oProducto.getIntProductoEntradas())
    print("Salidas     :",oProducto.getIntProductoSalidas())
    print("Actual      :",oProducto.getIntProductoActual())
    print("Costo       :",oProducto.getDecProductoCosto())
    print("Precio      :",oProducto.getDecProductoPrecio())
    print("Impuesto    :",oProducto.getImpuesto_id())
    print("Proveedor   :",oProducto.getProveedor_id())
    input("Presiona enter para continuar ...")

    # Modificamos algunos datos para actualizar
    oProducto.setStrProductoCodigo("AB123345_23")
    oProducto.setTipoProducto("CERVEZAS")
    oProducto.setStrProductoMarca("Superior")
    oProducto.setStrProductoNombre("Lager XX")
    oProducto.setStrProductoDescripcion("Lager XX Obscura 350 ml envase cristal")
    oProducto.setStrProductoMedida("Pza")
    oProducto.setIntProductoInicial(20)
    oProducto.setIntProductoEntradas(5)
    oProducto.setIntProductoSalidas(3)
    oProducto.setIntProductoActual(22)
    oProducto.setDecProductoCosto(7.30)
    oProducto.setDecProductoPrecio(15.30)
    oProducto.setImpuesto_id(1)
    oProducto.setProveedor_id(0)


    # Modificamos
    datProductos.fnProductoUpdate(oProducto)

    print("Consultando Producto Modificado:",idInsertado)
    oProducto = datProductos.fnProductoGet(idInsertado)
    print("Ide         :",oProducto.getIntProductoIde())
    print("Codigo      :",oProducto.getStrProductoCodigo())
    print("Tipo        :",oProducto.getTipoProducto())
    print("Marca       :",oProducto.getStrProductoMarca())
    print("Nombre      :",oProducto.getStrProductoNombre())
    print("Descripción :",oProducto.getStrProductoDescripcion())
    print("Medida      :",oProducto.getStrProductoMedida())
    print("Inicial     :",oProducto.getIntProductoInicial())
    print("Entradas    :",oProducto.getIntProductoEntradas())
    print("Salidas     :",oProducto.getIntProductoSalidas())
    print("Actual      :",oProducto.getIntProductoActual())
    print("Costo       :",oProducto.getDecProductoCosto())
    print("Precio      :",oProducto.getDecProductoPrecio())
    print("Impuesto    :",oProducto.getImpuesto_id())
    print("Proveedor   :",oProducto.getProveedor_id())
    input("Presiona enter para continuar ...")

    
    # Borramos el Producto Insertado
    datProductos.fnProductoDel(idInsertado)
    print("Producto Eliminado : ",idInsertado)    
    input("Presiona para continuar ...")

    # Consultando existencia del Producto Insertado
    print("Existe Producto :"+str(idInsertado),datProductos.fnProductoExiste(idInsertado))
    input("Presione para continuar ....")
    
    print("Lista de Productos ...")
    lstProductos = datProductos.fnProductoLista()
    for oProducto in lstProductos:
        print("Ide         :",oProducto.getIntProductoIde())
        print("Codigo      :",oProducto.getStrProductoCodigo())
        print("Tipo        :",oProducto.getTipoProducto())
        print("Marca       :",oProducto.getStrProductoMarca())
        print("Nombre      :",oProducto.getStrProductoNombre())
        print("Descripción :",oProducto.getStrProductoDescripcion())
        print("Medida      :",oProducto.getStrProductoMedida())
        print("Inicial     :",oProducto.getIntProductoInicial())
        print("Entradas    :",oProducto.getIntProductoEntradas())
        print("Salidas     :",oProducto.getIntProductoSalidas())
        print("Actual      :",oProducto.getIntProductoActual())
        print("Costo       :",oProducto.getDecProductoCosto())
        print("Precio      :",oProducto.getDecProductoPrecio())
        print("Impuesto    :",oProducto.getImpuesto_id())
        print("Proveedor   :",oProducto.getProveedor_id())    

    # # Confirmo transaccion
    fbd.fnCommit()
    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
