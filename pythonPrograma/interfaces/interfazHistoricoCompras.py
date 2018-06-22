# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazHistoricoVentas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from paquetePrincipal.BaseDatos import BaseDatos
from paquetePrincipal.Cliente import Cliente
from paquetePrincipal.Proveedor import Proveedor
from paquetePrincipal.Venta import Venta
from paquetePrincipal.Producto import Producto
from interfaces.interfazHistoricoItemCompras import *
from datetime import datetime

class Ui_historicoCompras(object):
    def mostrar(self):
        ArregloBotonClicked=QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(ArregloBotonClicked.pos())
        if index.isValid():
            id = self.tableWidget.item(index.row(),0).text()
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_historicoItemCompras()
            self.ui.setupUi(self.window,id)
            self.window.show()



    def cargarDatosVentas(self):
        tablas="compras"
        self.arregloBotones=[]
        rows=self.bd.cargarTodo(tablas)
        self.tableWidget.setRowCount(0)

        for count in range(len(rows)):
            self.arregloBotones.append(QtWidgets.QPushButton(self.tableWidget))
            self.arregloBotones[count].setText('Mostrar')

        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            a = QtWidgets.QTableWidgetItem(str(row[0]))
            a.setFlags(a.flags()  & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(inx, 0, a)
            self.tableWidget.setItem(inx, 1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(inx, 2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(inx, 3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(inx, 4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(inx, 5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(inx, 6,QtWidgets.QTableWidgetItem(str(row[6])))


            self.tableWidget.setCellWidget(inx, 7, self.arregloBotones[int(inx)])
            self.arregloBotones[inx].clicked.connect(self.mostrar)


    def setupUi(self, historicoVentas,usuarioActual):
        self.bd=BaseDatos()
        historicoVentas.setObjectName("historicoVentas")
        historicoVentas.resize(894, 659)
        historicoVentas.setMinimumSize(QtCore.QSize(894, 659))
        historicoVentas.setMaximumSize(QtCore.QSize(894, 659))
        self.tableWidget = QtWidgets.QTableWidget(historicoVentas)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 821, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.cargarDatosVentas()
        self.retranslateUi(historicoVentas)
        QtCore.QMetaObject.connectSlotsByName(historicoVentas)

    def retranslateUi(self, historicoVentas):
        _translate = QtCore.QCoreApplication.translate
        historicoVentas.setWindowTitle(_translate("historicoVentas", "Historico Compras"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("historicoVentas", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("historicoVentas", "id cliente"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("historicoVentas", "id usuario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("historicoVentas", "fecha"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("historicoVentas", "total"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("historicoVentas", "total iva desc"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("historicoVentas", "medio de pago"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("historicoVentas", "Mostrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historicoVentas = QtWidgets.QWidget()
    ui = Ui_historicoVentas()
    ui.setupUi(historicoVentas)
    historicoVentas.show()
    sys.exit(app.exec_())
