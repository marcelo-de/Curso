# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgParametrosSistema.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgParametros(object):
    def setupUi(self, dlgParametros):
        dlgParametros.setObjectName("dlgParametros")
        dlgParametros.setWindowModality(QtCore.Qt.WindowModal)
        dlgParametros.resize(423, 534)
        dlgParametros.setModal(True)
        self.gbParametros = QtWidgets.QGroupBox(dlgParametros)
        self.gbParametros.setGeometry(QtCore.QRect(10, 10, 401, 451))
        self.gbParametros.setObjectName("gbParametros")
        self.chkMensajesExito = QtWidgets.QCheckBox(self.gbParametros)
        self.chkMensajesExito.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.chkMensajesExito.setFont(font)
        self.chkMensajesExito.setObjectName("chkMensajesExito")
        self.chkVerificarExistencias = QtWidgets.QCheckBox(self.gbParametros)
        self.chkVerificarExistencias.setGeometry(QtCore.QRect(30, 60, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.chkVerificarExistencias.setFont(font)
        self.chkVerificarExistencias.setObjectName("chkVerificarExistencias")
        self.chkAgruparProductos = QtWidgets.QCheckBox(self.gbParametros)
        self.chkAgruparProductos.setGeometry(QtCore.QRect(30, 100, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.chkAgruparProductos.setFont(font)
        self.chkAgruparProductos.setObjectName("chkAgruparProductos")
        self.chkActivarBitacora = QtWidgets.QCheckBox(self.gbParametros)
        self.chkActivarBitacora.setGeometry(QtCore.QRect(30, 140, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.chkActivarBitacora.setFont(font)
        self.chkActivarBitacora.setObjectName("chkActivarBitacora")
        self.chkImprimirTicket = QtWidgets.QCheckBox(self.gbParametros)
        self.chkImprimirTicket.setGeometry(QtCore.QRect(30, 180, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.chkImprimirTicket.setFont(font)
        self.chkImprimirTicket.setObjectName("chkImprimirTicket")
        self.lblNombreMoneda = QtWidgets.QLabel(self.gbParametros)
        self.lblNombreMoneda.setGeometry(QtCore.QRect(30, 230, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lblNombreMoneda.setFont(font)
        self.lblNombreMoneda.setObjectName("lblNombreMoneda")
        self.leNombreMoneda = QtWidgets.QLineEdit(self.gbParametros)
        self.leNombreMoneda.setGeometry(QtCore.QRect(30, 260, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.leNombreMoneda.setFont(font)
        self.leNombreMoneda.setObjectName("leNombreMoneda")
        self.leSimboloMoneda = QtWidgets.QLineEdit(self.gbParametros)
        self.leSimboloMoneda.setGeometry(QtCore.QRect(30, 330, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.leSimboloMoneda.setFont(font)
        self.leSimboloMoneda.setObjectName("leSimboloMoneda")
        self.lblSimboloMoneda = QtWidgets.QLabel(self.gbParametros)
        self.lblSimboloMoneda.setGeometry(QtCore.QRect(30, 300, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lblSimboloMoneda.setFont(font)
        self.lblSimboloMoneda.setObjectName("lblSimboloMoneda")
        self.leTextoFinal = QtWidgets.QLineEdit(self.gbParametros)
        self.leTextoFinal.setGeometry(QtCore.QRect(30, 400, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.leTextoFinal.setFont(font)
        self.leTextoFinal.setObjectName("leTextoFinal")
        self.lblTextoFinal = QtWidgets.QLabel(self.gbParametros)
        self.lblTextoFinal.setGeometry(QtCore.QRect(30, 370, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lblTextoFinal.setFont(font)
        self.lblTextoFinal.setObjectName("lblTextoFinal")
        self.pbCancelar = QtWidgets.QPushButton(dlgParametros)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 470, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.pbCancelar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbAceptar = QtWidgets.QPushButton(dlgParametros)
        self.pbAceptar.setGeometry(QtCore.QRect(260, 470, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.pbAceptar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon1)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setObjectName("pbAceptar")

        self.retranslateUi(dlgParametros)
        QtCore.QMetaObject.connectSlotsByName(dlgParametros)
        dlgParametros.setTabOrder(self.chkMensajesExito, self.chkVerificarExistencias)
        dlgParametros.setTabOrder(self.chkVerificarExistencias, self.chkAgruparProductos)
        dlgParametros.setTabOrder(self.chkAgruparProductos, self.chkActivarBitacora)
        dlgParametros.setTabOrder(self.chkActivarBitacora, self.chkImprimirTicket)
        dlgParametros.setTabOrder(self.chkImprimirTicket, self.leNombreMoneda)
        dlgParametros.setTabOrder(self.leNombreMoneda, self.leSimboloMoneda)
        dlgParametros.setTabOrder(self.leSimboloMoneda, self.leTextoFinal)
        dlgParametros.setTabOrder(self.leTextoFinal, self.pbAceptar)
        dlgParametros.setTabOrder(self.pbAceptar, self.pbCancelar)

    def retranslateUi(self, dlgParametros):
        _translate = QtCore.QCoreApplication.translate
        dlgParametros.setWindowTitle(_translate("dlgParametros", "Parámetros del Sistema"))
        self.gbParametros.setTitle(_translate("dlgParametros", "GroupBox"))
        self.chkMensajesExito.setText(_translate("dlgParametros", "Desplegar Mensajes de Éxito"))
        self.chkVerificarExistencias.setText(_translate("dlgParametros", "Verificar Existencia en Venta"))
        self.chkAgruparProductos.setText(_translate("dlgParametros", "Agrupar Productos en Venta"))
        self.chkActivarBitacora.setText(_translate("dlgParametros", "Activar Bitácora"))
        self.chkImprimirTicket.setText(_translate("dlgParametros", "Imprimir Ticket"))
        self.lblNombreMoneda.setText(_translate("dlgParametros", "Nombre de la Moneda:"))
        self.leNombreMoneda.setText(_translate("dlgParametros", "UnKnow"))
        self.leSimboloMoneda.setText(_translate("dlgParametros", "?"))
        self.lblSimboloMoneda.setText(_translate("dlgParametros", "Símbolo de la Moneda:"))
        self.leTextoFinal.setText(_translate("dlgParametros", "! Gracias por su Compra !"))
        self.lblTextoFinal.setText(_translate("dlgParametros", "Texto Final del Ticket"))
        self.pbCancelar.setText(_translate("dlgParametros", "Cancelar"))
        self.pbAceptar.setText(_translate("dlgParametros", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgParametros = QtWidgets.QDialog()
    ui = Ui_dlgParametros()
    ui.setupUi(dlgParametros)
    dlgParametros.show()
    sys.exit(app.exec_())
