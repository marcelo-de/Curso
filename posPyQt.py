# ----------------------------------------------------------------------------------
# posPyQt5.py
# Programa Principal que inicia la aplicación
# ----------------------------------------------------------------------------------


# Importa las librerias propietarias
import vista.dlgSesion
import funciones.funcArchivo as fa

# Crear el Log
fa.fnLogCrea()

# Crea un objeto de la Clase
oDlgSesion = vista.dlgSesion.Ui_dlgSesion()

# Ejecuta
oDlgSesion.Ejecutar()