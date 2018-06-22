# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from interfaces.usuariosInterfaz import *
from interfaces.interfazProductosNew import *
from interfaces.interfazClientes import *
from interfaces.interfazProveedores import *
from interfaces.interfazVentas import *
from interfaces.interfazCompras import *
from interfaces.interfazHistoricoVentas import *
from interfaces.interfazHistoricoCompras import *

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
        self.productosInterfaz = Ui_interfazProductosNew()
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
        self.boton_proveedores = QtWidgets.QPushButton(self.centralwidget)
        self.boton_proveedores.setObjectName("boton_proveedores")
        self.verticalLayout.addWidget(self.boton_proveedores)
        self.proveedorInterfaz= Ui_ProveedoresForm()
        self.boton_proveedores.clicked.connect(lambda: self.openWindow(self.proveedorInterfaz,MainWindow))

        self.boton_compras = QtWidgets.QPushButton(self.centralwidget)
        self.boton_compras.setObjectName("boton_compras")
        self.verticalLayout.addWidget(self.boton_compras)
        self.comprasInterfaz= Ui_comprasObject()
        self.boton_compras.clicked.connect(lambda: self.openWindow(self.comprasInterfaz,MainWindow))

        self.boton_historicoCompras = QtWidgets.QPushButton(self.centralwidget)
        self.boton_historicoCompras.setObjectName("boton_historicoCompras")
        self.verticalLayout.addWidget(self.boton_historicoCompras)
        self.hComprasInterfaz=Ui_historicoCompras()
        self.boton_historicoCompras.clicked.connect(lambda: self.openWindow(self.hComprasInterfaz,MainWindow))

        self.boton_ventas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_ventas.setObjectName("boton_ventas")
        self.verticalLayout.addWidget(self.boton_ventas)
        self.ventasInterfaz= Ui_ventasObject()
        self.boton_ventas.clicked.connect(lambda: self.openWindow(self.ventasInterfaz,MainWindow))

        self.boton_historicoVentas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_historicoVentas.setObjectName("boton_HistoricoVentas")
        self.verticalLayout.addWidget(self.boton_historicoVentas)
        self.hVentasInterfaz=Ui_historicoVentas()
        self.boton_historicoVentas.clicked.connect(lambda: self.openWindow(self.hVentasInterfaz,MainWindow))

        # Se agrega botón Ventas y función abrir ventana...

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
        self.boton_historicoVentas.setText(_translate("MainWindow", "Histórico Ventas"))
        self.boton_compras.setText(_translate("MainWindow", "Compras"))
        self.boton_historicoCompras.setText(_translate("MainWindow", "Histórico Compras"))
        self.boton_proveedores.setText(_translate("MainWindow", "Proveedores"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
