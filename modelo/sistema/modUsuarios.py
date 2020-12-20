# -----------------------------------------------------------------
# Clase mUsuarios
# Modelo para obtener información referente a los Usuarios
# -----------------------------------------------------------------

# Importa la libreria globales
#from   multipledispatch import dispatch
import entidades.entGlobales   as eg
import entidades.sistema.entUsuarios   as eu
import funciones.funcBaseDatos as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_USUARIO_IDE = 0
INT_COL_USUARIO_CVE = 1
INT_COL_USUARIO_NOM = 2
INT_COL_USUARIO_ROL = 3

# Definición de la Clase
class mUsuarios:

    # Función para obtener información de un usuario
    #@dispatch(str,str)
    def fnUsuarioGet(self,identificacion, clave):

        # Crea un objeto de Usuarios para retornar
        oUsuario = eu.eUsuarios()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM usuarios "
        sQuery += " WHERE strUsuarioIde  = '"+identificacion+"'"
        sQuery += " AND   strUsuarioPass = '"+clave+"'"

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oUsuario.setStrUsuarioIde(registro[INT_COL_USUARIO_IDE])
                oUsuario.setStrUsuarioName(registro[INT_COL_USUARIO_NOM])
                oUsuario.setStrUsuarioPass(registro[INT_COL_USUARIO_CVE])
                oUsuario.setStrRoleName(registro[INT_COL_USUARIO_ROL])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return oUsuario

    #@dispatch(str)
    #def fnUsuarioGet(self,identificacion):
    def fnUsuarioGetByIde(self,identificacion):

        # Crea un objeto de Usuarios para retornar
        oUsuario = eu.eUsuarios()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM usuarios "
        sQuery += " WHERE strUsuarioIde  = '"+identificacion+"'"
        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oUsuario.setStrUsuarioIde(registro[INT_COL_USUARIO_IDE])
                oUsuario.setStrUsuarioName(registro[INT_COL_USUARIO_NOM])
                oUsuario.setStrUsuarioPass(registro[INT_COL_USUARIO_CVE])
                oUsuario.setStrRoleName(registro[INT_COL_USUARIO_ROL])
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return oUsuario

    # Función que verifica que el usuario exista
    def fnUsuarioExiste(self,identificacion):

        # Crea variable de resultado
        bResultado = False

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM usuarios "
        sQuery += " WHERE strUsuarioIde  = '"+identificacion+"'"
        

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Cambia la variable de Resultado
                bResultado= True
                
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto Usuario
        return bResultado

    
    # Función para obtener modificar un usuario
    def fnUsuarioUpdate(self,oUsuario):

        # Prepara el Query para Actualizar
        sQuery =  " UPDATE usuarios "
        sQuery += " SET    strUsuarioPass  = '"+oUsuario.getStrUsuarioPass()+"',"
        sQuery += "        strUsuarioName  = '"+oUsuario.getStrUsuarioName()+"',"
        sQuery += "        strRoleName     = '"+oUsuario.getStrRoleName()+"'"
        sQuery += " WHERE  strUsuarioIde   = '"+oUsuario.getStrUsuarioIde()+"'"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para insertar un usuario
    def fnUsuarioInsert(self,oUsuario):

        # Prepara el Query para Actualizar
        sQuery =  " INSERT INTO usuarios "
        sQuery += " (strUsuarioIde,strUsuarioPass,strUsuarioName,strRoleName) VALUES"
        sQuery += " ('"+oUsuario.getStrUsuarioIde()+"',"
        sQuery += "  '"+oUsuario.getStrUsuarioPass()+"',"
        sQuery += "  '"+oUsuario.getStrUsuarioName()+"',"
        sQuery += "  '"+oUsuario.getStrRoleName()+"')"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para eliminar un usuario
    def fnUsuarioDel(self,sIde):

        # Prepara el Query para Actualizar
        sQuery =  " DELETE FROM usuarios "
        sQuery += " WHERE  strUsuarioIde   = '"+sIde+"'"

        # Intenta Ejecuta la Sentencia de
        return fbd.fnExecuteUpdateSql(sQuery,False)

    # Función para obtener los Usuarios
    def fnUsuarioListaGet(self):

        # Objeto lista a devolver
        lstUsuarios = []      

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM usuarios "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Ciclo para leer los registros
            while True:

                # Crea Objeto 
                oUsuario = eu.eUsuarios()

                 # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Verifica si ya no hay registos
                if (registro is None):
                    # Sale si no hay registros
                    break

                # Coloca los datos en el objeto
                oUsuario.setStrUsuarioIde(registro[INT_COL_USUARIO_IDE])
                oUsuario.setStrUsuarioPass(registro[INT_COL_USUARIO_CVE])
                oUsuario.setStrUsuarioName(registro[INT_COL_USUARIO_NOM])
                oUsuario.setStrRoleName(registro[INT_COL_USUARIO_ROL])

                # Agrega el Proceso a la Lista
                lstUsuarios.append(oUsuario)
                                        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna la lista de Procesos
        return lstUsuarios

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
    datUsuarios = mUsuarios()

    # Declarando un objeto de la entidad Usuarios
    oUsuario = eu.eUsuarios

    # Ejecutando la Consulta de un Usuario
    oUsuario = datUsuarios.fnUsuarioGet("jaor","software")
    #oUsuario = datUsuarios.fnUsuarioGet("jaor")

    # Desplegando los datos
    print("Ide  :",oUsuario.getStrUsuarioIde())
    print("Name :",oUsuario.getStrUsuarioName())
    print("Pass :",oUsuario.getStrUsuarioPass())
    print("Role :",oUsuario.getStrRoleName())
    input("Presiona una tecla para continuar ...")
    print("")

    #Intenga una modificación
    oUsuario.setStrUsuarioIde("jaor")
    oUsuario.setStrUsuarioPass("system")
    datUsuarios.fnUsuarioUpdate(oUsuario)

    # Obteniendo la lista de usuarios despues de insertar
    listaUsuarios = datUsuarios.fnUsuarioListaGet()

    print("Usuarios despues de Actualizar ...")
    #Ciclo para desplegar los usuarios
    for oUsuario in listaUsuarios:
        print(oUsuario.getStrUsuarioIde(),
              oUsuario.getStrUsuarioPass(),
              oUsuario.getStrUsuarioName(),
              oUsuario.getStrRoleName())
    input("Presiona para continuar ...")          
    print("")


    #Intenta una Inserción cambiando solo el Ide
    oUsuario.setStrUsuarioIde("juan")
    oUsuario.setStrUsuarioPass("nomelase")
    oUsuario.setStrUsuarioName("juan perez")
    oUsuario.setStrRoleName("user")
    
    # Verifica que haya habido una inserción
    if (not datUsuarios.fnUsuarioInsert(oUsuario)):
        #Realiza rollback
        fbd.fnRollback()
        sys.exit(-1)

    # Obteniendo la lista de usuarios despues de insertar
    listaUsuarios = datUsuarios.fnUsuarioListaGet()

    print("Usuarios despues de Insertar ...")
    #Ciclo para desplegar los usuarios
    for oUsuario in listaUsuarios:
        print(oUsuario.getStrUsuarioIde(),
              oUsuario.getStrUsuarioPass(),
              oUsuario.getStrUsuarioName(),
              oUsuario.getStrRoleName())
    input("Presiona para continuar ...")          

    
    # Elimina el usuario 
    datUsuarios.fnUsuarioDel("juan")    

    # Obteniendo la lista de usuarios despues de insertar
    listaUsuarios = datUsuarios.fnUsuarioListaGet()

    print("Usuarios despues de Eliminar ...")
    #Ciclo para desplegar los usuarios
    for oUsuario in listaUsuarios:
        print(oUsuario.getStrUsuarioIde(),
              oUsuario.getStrUsuarioPass(),
              oUsuario.getStrUsuarioName(),
              oUsuario.getStrRoleName())
    input("Presiona para continuar ...")          

    # Verificando si existe un usuario
    print("Existe el usuario admin:",datUsuarios.fnUsuarioExiste("admin"))

    # Realiza commit
    fbd.fnCommit()

    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
