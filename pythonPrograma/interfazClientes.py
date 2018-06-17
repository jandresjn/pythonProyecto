# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientes.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from BaseDatos import BaseDatos
from Cliente import Cliente
import sqlite3

class Ui_clientesForm(object):


    def crearCliente(self):
        nuevoCliente=Cliente(None,self.lineEdit_Nombre.text(),self.lineEdit_Documento.text())
        nuevoCliente.crearCliente()
        idCliente=nuevoCliente.id

        filasTabla = self.tableWidget.rowCount()

        boton = QtWidgets.QPushButton()
        boton.setText('Borrar')
        boton.clicked.connect(self.borrarCliente)

        self.tableWidget.blockSignals(True)

        self.tableWidget.insertRow( filasTabla )
        self.tableWidget.setItem( filasTabla, 0, QtWidgets.QTableWidgetItem(str(idCliente)))
        self.tableWidget.setItem( filasTabla, 1, QtWidgets.QTableWidgetItem(self.lineEdit_Nombre.text()))
        self.tableWidget.setItem( filasTabla, 2, QtWidgets.QTableWidgetItem(self.lineEdit_Documento.text()))
        self.tableWidget.setCellWidget( filasTabla, 3, boton)

        self.tableWidget.blockSignals(False)
        self.lineEdit_Nombre.clear()
        self.lineEdit_Documento.clear()
        print("termina")

    def borrarCliente(self):
        print("borrarCliente")
        ArregloBotonClicked=QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(ArregloBotonClicked.pos())
        if index.isValid():
            id = self.tableWidget.item(index.row(),0).text()
            clienteActual=Cliente(id,None,None)
            clienteActual.borrarCliente()

            self.tableWidget.removeRow(index.row())

    def cargarDatos(self):
        print("cargarDatos")
        self.arregloBotones=[]
        tabla="clientes"
        camposSelect=["id","nombre","numero_documento"]
        self.tableWidget.setRowCount(0)
        rows=self.bd.cargarDatosValorCampo(tabla,camposSelect)

        for count in range(len(rows)):
            self.arregloBotones.append(QtWidgets.QPushButton(self.tableWidget))
            self.arregloBotones[count].setText('Borrar')

        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            a = QtWidgets.QTableWidgetItem(str(row[0]))
            a.setFlags(a.flags()  & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(inx, 0, a)
            self.tableWidget.setItem(inx, 1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(inx, 2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setCellWidget(inx, 3, self.arregloBotones[int(inx)])
            self.arregloBotones[inx].clicked.connect(self.borrarCliente)

    def setupUi(self, clientesForm):
        self.bd=BaseDatos()
        clientesForm.setObjectName("clientesForm")
        clientesForm.resize(500, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(clientesForm.sizePolicy().hasHeightForWidth())
        clientesForm.setSizePolicy(sizePolicy)
        clientesForm.setMinimumSize(QtCore.QSize(500, 0))
        clientesForm.setMaximumSize(QtCore.QSize(500, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(clientesForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(clientesForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_Nombre = QtWidgets.QLineEdit(clientesForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Nombre.sizePolicy().hasHeightForWidth())
        self.lineEdit_Nombre.setSizePolicy(sizePolicy)
        self.lineEdit_Nombre.setObjectName("lineEdit_Nombre")
        self.verticalLayout_2.addWidget(self.lineEdit_Nombre)
        self.label_3 = QtWidgets.QLabel(clientesForm)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_Documento = QtWidgets.QLineEdit(clientesForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Documento.sizePolicy().hasHeightForWidth())
        self.lineEdit_Documento.setSizePolicy(sizePolicy)
        self.lineEdit_Documento.setObjectName("lineEdit_Documento")
        self.verticalLayout_2.addWidget(self.lineEdit_Documento)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(clientesForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(clientesForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.tableWidget.blockSignals(True)
        self.cargarDatos()
        self.tableWidget.blockSignals(False)
        self.btnAdd.clicked.connect(self.crearCliente)

        self.retranslateUi(clientesForm)
        QtCore.QMetaObject.connectSlotsByName(clientesForm)

    def retranslateUi(self, clientesForm):
        _translate = QtCore.QCoreApplication.translate
        clientesForm.setWindowTitle(_translate("clientesForm", "Clientes"))
        self.label.setText(_translate("clientesForm", "Nombre"))
        self.label_3.setText(_translate("clientesForm", "Num de Documento"))
        self.btnAdd.setText(_translate("clientesForm", "Añadir"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("clientesForm", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("clientesForm", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("clientesForm", "N Documento"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("clientesForm", "Opciones"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clientesForm = QtWidgets.QWidget()
    ui = Ui_clientesForm()
    ui.setupUi(clientesForm)
    clientesForm.show()
    sys.exit(app.exec_())
