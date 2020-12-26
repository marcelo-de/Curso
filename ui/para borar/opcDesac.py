# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opcDesac.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSistema = QtWidgets.QMenu(self.menubar)
        self.menuSistema.setObjectName("menuSistema")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpcion_1 = QtWidgets.QAction(MainWindow)
        self.actionOpcion_1.setEnabled(False)
        self.actionOpcion_1.setObjectName("actionOpcion_1")
        self.actionOpcion_2 = QtWidgets.QAction(MainWindow)
        self.actionOpcion_2.setObjectName("actionOpcion_2")
        self.menuSistema.addAction(self.actionOpcion_1)
        self.menuSistema.addAction(self.actionOpcion_2)
        self.menubar.addAction(self.menuSistema.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSistema.setTitle(_translate("MainWindow", "Sistema"))
        self.actionOpcion_1.setText(_translate("MainWindow", "Opcion 1"))
        self.actionOpcion_2.setText(_translate("MainWindow", "Opcion 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
