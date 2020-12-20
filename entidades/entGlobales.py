# -------------------------------------------------------------------
# Módulo entGlobales.py
# Constantes y Variables Globales al Sistema
# -------------------------------------------------------------------

# Importamos librería
from typing import TextIO

# Variables de MySql no se pudieran manejar a través de la clase
gConnMySql        = 0        # Conexión a la Base de Datos
gCursor           = 0        # El Cursor par hacer Consultas

# Declaro la Clase
class eGlobales:

    # -------------------------------------------------------------------
    # Constantes
    # -------------------------------------------------------------------
    SISTEMA         = "jaorPosPyQt"        # Nombre del Sistema
    INICIALIZACION  = "inicializacion.xml" # Archivo de Inicialización
    VERSION         = "Ver 1.0"
    BOTON_ACEPTAR   = 1
    BOTON_CANCELAR  = 0
    ARCHIVO_LOG     = "jaorPosLog"         # Nombre del Archivo Log

    # Operaciones
    OPERACION_INSERTAR  = "I"
    OPERACION_ELIMINAR  = "E"
    OPERACION_MODIFICAR = "M"
      
    # ------------------------------------------------------------------
    # Variables Globales
    # ------------------------------------------------------------------
    UsuarioIde      = "UnKnow" # Usuario del Sistema
    UsuarioNom      = "Unknow" # Nombre del Usuario
    UsuarioRol      = "Unknow" # Role del Usuario
    Sucursal        = "Unknow" # Sucursal
    Terminal        = "0"      # Terminal
    AñoOperacion    = "UnKnow"
    
    # Variables para los parámetros del Sistema
    MensajesExito        = True
    AgruparProductos     = False
    VerificarExistencias = False
    ImprimirTicket       = False
    BitacoraActiva       = False
    MensajeTicket        = "UnKnow"
    MonedaSimbolo        = "?"
    MonedaNombre         = "UnKnow"

    # Variable para el Archivo Log
    aLogArchivo: TextIO  = None
    bLogCreado           = False

    # En el dialogo de Ventana
    BotonPresionado = -1

    
# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

   
    # Verificando despliegue de Variables globales
    print("Variables y Constantes Globales ...")
    print("Sistema        :",eGlobales.SISTEMA)
    print("Inicialización :",eGlobales.INICIALIZACION)
    print("Botón Aceptar  :",eGlobales.BOTON_ACEPTAR)
    print("Botón Cancelar :",eGlobales.BOTON_CANCELAR)    
    print("Operación Ins  :",eGlobales.OPERACION_INSERTAR)    
    print("Operación Del  :",eGlobales.OPERACION_ELIMINAR)    
    print("Operación Upd  :",eGlobales.OPERACION_MODIFICAR)    
    print("Versión        :",eGlobales.VERSION)
    print("Archiv Log     :",eGlobales.ARCHIVO_LOG)
    print("UsuarioIde     :",eGlobales.UsuarioIde)
    print("UsuarioNom     :",eGlobales.UsuarioNom)
    print("UsuarioRol     :",eGlobales.UsuarioRol)
    print("Sucursal       :",eGlobales.Sucursal)
    print("Terminal       :",eGlobales.Terminal)
    print("AñoOperacion   :",eGlobales.AñoOperacion)
    print("Conexión       :",gConnMySql)
    print("Cursor         :",gCursor)    
    print("")

    #Imprimiendo parámetros del Sistema
    print("Parámetros del Sistema ...")
    print("Mensajes de Éxito        :",eGlobales.MensajesExito)
    print("Agrupar Productos        :",eGlobales.AgruparProductos)
    print("Verificar Existencias    :",eGlobales.VerificarExistencias)
    print("Bitácora Activa          :",eGlobales.BitacoraActiva)
    print("Mensaje del Ticket       :",eGlobales.MensajeTicket)
    print("Nombre de la Moneda      :",eGlobales.MonedaNombre)
    print("Símbolo de la Monena     :",eGlobales.MonedaSimbolo)

    # Otros
    print("Botón Presionado         :",eGlobales.BotonPresionado)
    print("aLogArchivo              :",eGlobales.aLogArchivo)
    print("bLogCreado               :",eGlobales.aLogArchivo)
