# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazHistoricoItemVentas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from paquetePrincipal.BaseDatos import BaseDatos
from paquetePrincipal.Cliente import Cliente
from paquetePrincipal.Venta import Venta
from paquetePrincipal.Producto import Producto
from datetime import datetime

class Ui_historicoItemVentas(object):
    def hallarNombre(self,idNombre):
        tabla="productos"
        camposSelect=["descripcion"]
        camposWhere=["id"]
        tipoCamposWhere=[-1]
        valorCamposWhere=[idNombre]
        nombre=self.bd.buscarValorCamposGeneral(tabla,camposSelect,camposWhere,tipoCamposWhere,valorCamposWhere)
        return nombre
    def cargarTodo(self,idVenta):
        tabla="items_venta"
        campo="id_venta"
        valorCampo=idVenta
        rows=self.bd.cargarTodoId(tabla,campo,valorCampo)
        self.listWidget.clear()
        self.listWidget.addItem("(NOMBRE)   (id, id venta, precio, cantidad, iva, id producto, total)")
        for row in rows :
            print(row[5])
            nombre=self.hallarNombre(row[5])
            self.listWidget.addItem(str(nombre)+" "+str(row))

    def setupUi(self, historicoItemVentas,idVenta):
        self.bd=BaseDatos()
        historicoItemVentas.setObjectName("historicoItemVentas")
        historicoItemVentas.resize(659*0.7, 659*0.7)
        historicoItemVentas.setMinimumSize(QtCore.QSize(659*0.7, 659*0.7))
        historicoItemVentas.setMaximumSize(QtCore.QSize(659*0.7, 659*0.7))
        self.listWidget = QtWidgets.QListWidget(historicoItemVentas)
        self.listWidget.setGeometry(QtCore.QRect(40, 30, 591*0.7, 591*0.7))
        self.listWidget.setObjectName("listWidget")

        self.cargarTodo(idVenta)
        self.retranslateUi(historicoItemVentas)
        QtCore.QMetaObject.connectSlotsByName(historicoItemVentas)

    def retranslateUi(self, historicoItemVentas):
        _translate = QtCore.QCoreApplication.translate
        historicoItemVentas.setWindowTitle(_translate("historicoItemVentas", "Historico Ventas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historicoItemVentas = QtWidgets.QWidget()
    ui = Ui_historicoItemVentas()
    ui.setupUi(historicoItemVentas)
    historicoItemVentas.show()
    sys.exit(app.exec_())
