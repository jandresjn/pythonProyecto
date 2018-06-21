# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from interfaces.usuariosInterfaz import *
from interfaces.interfazProductos import *
from interfaces.interfazClientes import *
from interfaces.interfazVentas import *

class Ui_MainWindow(object):

    def openWindow(self,new_Window,MainWindow):
        self.window = QtWidgets.QWidget()
        new_Window.setupUi(self.window,self.usuarioActual)
        # MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow,usuarioActual):
        self.usuarioActual=usuarioActual
        print(self.usuarioActual.nombreUsuario)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 270)
        MainWindow.setMinimumSize(QtCore.QSize(359, 270))
        MainWindow.setMaximumSize(QtCore.QSize(359, 270))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        if (self.usuarioActual.id==1):
            self.boton_usuarios = QtWidgets.QPushButton(self.centralwidget)
            self.boton_usuarios.setObjectName("boton_usuarios")
            self.verticalLayout.addWidget(self.boton_usuarios)
            # Se agrega la función de abrir ventana cuando se presiona el botón de usuarios...
            self.usuariosInterfaz= Ui_Form()
            self.boton_usuarios.clicked.connect(lambda: self.openWindow(self.usuariosInterfaz,MainWindow))

        self.boton_productos = QtWidgets.QPushButton(self.centralwidget)
        self.boton_productos.setObjectName("boton_productos")
        self.verticalLayout.addWidget(self.boton_productos)
        # Se agrega la función de abrir ventana cuando se presiona el botón de usuarios...
        self.productosInterfaz = Ui_productosForm()
        self.boton_productos.clicked.connect(lambda: self.openWindow(self.productosInterfaz,MainWindow))
        self.boton_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_clientes.setObjectName("boton_clientes")
        self.verticalLayout.addWidget(self.boton_clientes)
        # Se agrega la función de abrir ventana cuando se presiona el botón de usuarios...
        self.clientesInterfaz= Ui_clientesForm()
        self.boton_clientes.clicked.connect(lambda: self.openWindow(self.clientesInterfaz,MainWindow))
        # self.boton_servicios = QtWidgets.QPushButton(self.centralwidget)
        # self.boton_servicios.setObjectName("boton_servicios")
        # self.verticalLayout.addWidget(self.boton_servicios)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        # Se agrega la función de abrir ventana cuando se presiona el botón de usuarios...
        # self.serviciosInterfaz= Ui_serviciosForm()
        # self.boton_servicios.clicked.connect(lambda: self.openWindow(self.serviciosInterfaz,MainWindow))

        # Se agrega botón Ventas y función abrir ventana...
        self.boton_ventas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_ventas.setObjectName("boton_ventas")
        self.verticalLayout.addWidget(self.boton_ventas)
        self.ventasInterfaz= Ui_ventasObject()
        self.boton_ventas.clicked.connect(lambda: self.openWindow(self.ventasInterfaz,MainWindow))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow ", "Menú Principal"))
        if (self.usuarioActual.id==1):
            self.boton_usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.boton_productos.setText(_translate("MainWindow", "Productos"))
        self.boton_clientes.setText(_translate("MainWindow", "Clientes"))
        # self.boton_servicios.setText(_translate("MainWindow", "Servicios"))
        self.boton_ventas.setText(_translate("MainWindow", "Ventas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
