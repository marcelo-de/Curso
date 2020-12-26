# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaMensaje.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(528, 237)
        Dialog.setModal(True)
        self.lblTitulo = QtWidgets.QLabel(Dialog)
        self.lblTitulo.setGeometry(QtCore.QRect(10, 10, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.teMensaje = QtWidgets.QTextEdit(Dialog)
        self.teMensaje.setGeometry(QtCore.QRect(10, 50, 511, 121))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.teMensaje.setFont(font)
        self.teMensaje.setReadOnly(True)
        self.teMensaje.setObjectName("teMensaje")
        self.pbCancelar = QtWidgets.QPushButton(Dialog)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.pbCancelar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/icon_cancelar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setAutoDefault(False)
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbAceptar = QtWidgets.QPushButton(Dialog)
        self.pbAceptar.setGeometry(QtCore.QRect(350, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.pbAceptar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../img/icon_aceptar32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon1)
        self.pbAceptar.setIconSize(QtCore.QSize(32, 32))
        self.pbAceptar.setAutoDefault(False)
        self.pbAceptar.setObjectName("pbAceptar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pbAceptar, self.pbCancelar)
        Dialog.setTabOrder(self.pbCancelar, self.teMensaje)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mensaje"))
        self.lblTitulo.setText(_translate("Dialog", "Título"))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar"))
        self.pbAceptar.setText(_translate("Dialog", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
