from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class myListWidget(QtWidgets.QListWidget):
    
   def Clicked(self,item):
      QtWidgets.QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		
def main():
   app = QtWidgets.QApplication(sys.argv)
   listWidget = myListWidget()
   #listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
   listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

   #Resize width and height
   listWidget.resize(300,120)
	
   listWidget.addItem("Item 1")
   listWidget.addItem("Item 2")
   listWidget.addItem("Item 3")
   listWidget.addItem("Item 4")
	
   listWidget.setWindowTitle('PyQT QListwidget Demo')
   listWidget.itemClicked.connect(listWidget.Clicked)
   
   listWidget.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()