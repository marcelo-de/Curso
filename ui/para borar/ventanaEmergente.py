# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaEmergente.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgVentanaEmergente(object):
    def setupUi(self, dlgVentanaEmergente):
        dlgVentanaEmergente.setObjectName("dlgVentanaEmergente")
        dlgVentanaEmergente.resize(464, 52)
        self.leMensaje = QtWidgets.QLineEdit(dlgVentanaEmergente)
        self.leMensaje.setEnabled(True)
        self.leMensaje.setGeometry(QtCore.QRect(2, 0, 461, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leMensaje.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.leMensaje.setFont(font)
        self.leMensaje.setFrame(True)
        self.leMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.leMensaje.setReadOnly(True)
        self.leMensaje.setObjectName("leMensaje")

        self.retranslateUi(dlgVentanaEmergente)
        QtCore.QMetaObject.connectSlotsByName(dlgVentanaEmergente)

    def retranslateUi(self, dlgVentanaEmergente):
        _translate = QtCore.QCoreApplication.translate
        dlgVentanaEmergente.setWindowTitle(_translate("dlgVentanaEmergente", "Dialog"))
        self.leMensaje.setText(_translate("dlgVentanaEmergente", "Mensaje"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgVentanaEmergente = QtWidgets.QDialog()
    ui = Ui_dlgVentanaEmergente()
    ui.setupUi(dlgVentanaEmergente)
    dlgVentanaEmergente.show()
    sys.exit(app.exec_())
