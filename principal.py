# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from usuariosInterfaz import *
class Ui_MainWindow(object):

    def openWindow(self,new_Window,MainWindow):
        self.window = QtWidgets.QWidget()
        new_Window.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(175, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.boton_usuarios = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.boton_usuarios.setObjectName("boton_usuarios")
        self.verticalLayout.addWidget(self.boton_usuarios)
        # Se agrega la función de abrir ventana cuando se presiona el botón de usuarios...
        self.usuariosInterfaz= Ui_Form()
        self.boton_usuarios.clicked.connect(lambda: self.openWindow(self.usuariosInterfaz,MainWindow))

        self.boton_productos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.boton_productos.setObjectName("boton_productos")
        self.verticalLayout.addWidget(self.boton_productos)
        self.boton_clientes = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.boton_clientes.setObjectName("boton_clientes")
        self.verticalLayout.addWidget(self.boton_clientes)
        self.boton_servicios = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.boton_servicios.setObjectName("boton_servicios")
        self.verticalLayout.addWidget(self.boton_servicios)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 175, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú Principal"))
        self.boton_usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.boton_productos.setText(_translate("MainWindow", "Productos"))
        self.boton_clientes.setText(_translate("MainWindow", "Clientes"))
        self.boton_servicios.setText(_translate("MainWindow", "Servicios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
