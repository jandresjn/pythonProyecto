# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazProductosNew.ui'
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
import sqlite3
class Ui_interfazProductosNew(object):
    def borrarProducto(self):
        print("borrarProducto")
        ArregloBotonClicked=QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(ArregloBotonClicked.pos())
        if index.isValid():
            id = self.tableWidget.item(index.row(),0).text()
            nuevoProducto=Producto(id=id)
            nuevoProducto.borrarProducto()
            # conn = sqlite3.connect("basedatos.db")
            # cursor = conn.cursor()
            # sql = "UPDATE usuarios SET activo=0 WHERE _rowid_=?"
            # cursor.execute(sql, [ (id) ] )
            # conn.commit()
            self.tableWidget.removeRow(index.row())

    def getCategorias(self):
        rows=self.bd.cargarTodo("categorias")
        for index in range(len(rows)):
            self.categorias.append(str(rows[index][1]))
            self.categoriasId.append(int(rows[index][0]))
        print("categorias")
        print(self.categorias)
        self.comboBox_categoria.addItems(self.categorias)

    def identificaCategoria2(self,id):
        # idx=self.comboBox_categoria.currentIndex()
        print("xxxxxxxxxxxxxxxxxxxx")
        print(self.categorias)
        print(id)
        categoria=self.categorias[id-1]
        return categoria

    def identificaCategoria(self):
        idx=self.comboBox_categoria.currentIndex()
        categoria=self.categoriasId[idx]
        return categoria
    def resetear(self):
        self.lineEdit_Codigo.clear()
        self.lineEdit_descripcion.clear()
        self.lineEdit_Precio.clear()

    def crearProducto(self):
        try:
            idCategoria=self.identificaCategoria()
            cod=None
            desc=None
            precioAct=None
            if self.lineEdit_Codigo.text() != "" or self.lineEdit_Codigo.text() != "" or self.lineEdit_Codigo.text() != "":
                cod=self.lineEdit_Codigo.text()
                desc=self.lineEdit_descripcion.text()
                precioAct=float(self.lineEdit_Precio.text())
            nuevoProducto=Producto(codigo=cod,precio=precioAct,descripcion=desc,inventario=self.spinBox_invInit.value(),id_categoria=idCategoria)
            nuevoProducto.crearProducto()
            idProducto=nuevoProducto.id

            filasTabla = self.tableWidget.rowCount()

            boton = QtWidgets.QPushButton()
            boton.setText('Borrar')
            boton.clicked.connect(self.borrarProducto)

            self.tableWidget.blockSignals(True)

            self.tableWidget.insertRow( filasTabla )
            self.tableWidget.setItem( filasTabla, 0, QtWidgets.QTableWidgetItem(str(idProducto)))
            self.tableWidget.setItem( filasTabla, 1, QtWidgets.QTableWidgetItem(self.lineEdit_Codigo.text()))
            self.tableWidget.setItem( filasTabla, 2, QtWidgets.QTableWidgetItem(self.lineEdit_descripcion.text()))
            self.tableWidget.setItem( filasTabla, 3, QtWidgets.QTableWidgetItem(self.lineEdit_Precio.text()))
            self.tableWidget.setItem( filasTabla, 4, QtWidgets.QTableWidgetItem(str(nuevoProducto.inventario)))
            self.tableWidget.setItem( filasTabla, 5, QtWidgets.QTableWidgetItem(self.comboBox_categoria.currentText()))

            self.tableWidget.setCellWidget( filasTabla, 6, boton)

            self.tableWidget.blockSignals(False)
            self.resetear()
            print("termina")
            self.label_4.setText("")

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            self.label_4.setText("Error: Use sólo números")
            return False
        except sqlite3.IntegrityError:
            print(" Ref Producto Repedito o Nulo")
            self.label_4.setText("Error: Usuario Repedito o Nulo")
            return False

    def cargarDatosProductos(self):
        tablas="productos"
        self.arregloBotones=[]
        # rows=self.bd.cargarTodo(tablas)
        self.tableWidget.setRowCount(0)

        camposSelect=["id","codigo","descripcion","precio","inventario","id_categoria"]
        rows=self.bd.cargarDatosValorCampo(tablas,camposSelect)

        for count in range(len(rows)):
            self.arregloBotones.append(QtWidgets.QPushButton(self.tableWidget))
            self.arregloBotones[count].setText('Borrar')

        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            a = QtWidgets.QTableWidgetItem(str(row[0]))
            a.setFlags(a.flags()  & ~Qt.ItemIsEditable)
            catego=self.identificaCategoria2(row[5])
            self.tableWidget.setItem(inx, 0, a)
            self.tableWidget.setItem(inx, 1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(inx, 2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(inx, 3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(inx, 4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(inx, 5,QtWidgets.QTableWidgetItem(str(catego)))



            self.tableWidget.setCellWidget(inx, 6, self.arregloBotones[int(inx)])
            self.arregloBotones[inx].clicked.connect(self.borrarProducto)

    def setupUi(self, interfazProductosNew,usuarioActual):
        self.categorias=[]
        self.categoriasId=[]
        self.bd=BaseDatos()
        interfazProductosNew.setObjectName("interfazProductosNew")
        interfazProductosNew.resize(709, 604)
        interfazProductosNew.setMinimumSize(QtCore.QSize(709, 604))
        interfazProductosNew.setMaximumSize(QtCore.QSize(709, 604))
        self.lineEdit_Codigo = QtWidgets.QLineEdit(interfazProductosNew)
        self.lineEdit_Codigo.setGeometry(QtCore.QRect(100, 30, 118, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo.setObjectName("lineEdit_Codigo")
        self.label_codigo = QtWidgets.QLabel(interfazProductosNew)
        self.label_codigo.setGeometry(QtCore.QRect(40, 40, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_codigo.sizePolicy().hasHeightForWidth())
        self.label_codigo.setSizePolicy(sizePolicy)
        self.label_codigo.setObjectName("label_codigo")
        self.label_precio = QtWidgets.QLabel(interfazProductosNew)
        self.label_precio.setGeometry(QtCore.QRect(290, 30, 51, 21))
        self.label_precio.setObjectName("label_precio")
        self.lineEdit_descripcion = QtWidgets.QLineEdit(interfazProductosNew)
        self.lineEdit_descripcion.setGeometry(QtCore.QRect(110, 90, 118, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_descripcion.sizePolicy().hasHeightForWidth())
        self.lineEdit_descripcion.setSizePolicy(sizePolicy)
        self.lineEdit_descripcion.setObjectName("lineEdit_descripcion")
        self.btnAdd = QtWidgets.QPushButton(interfazProductosNew)
        self.btnAdd.setGeometry(QtCore.QRect(550, 60, 85, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setObjectName("btnAdd")
        self.laberl_descripcion = QtWidgets.QLabel(interfazProductosNew)
        self.laberl_descripcion.setGeometry(QtCore.QRect(30, 100, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laberl_descripcion.sizePolicy().hasHeightForWidth())
        self.laberl_descripcion.setSizePolicy(sizePolicy)
        self.laberl_descripcion.setObjectName("laberl_descripcion")
        self.label_4 = QtWidgets.QLabel(interfazProductosNew)
        self.label_4.setGeometry(QtCore.QRect(290, 150, 211, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_Precio = QtWidgets.QLineEdit(interfazProductosNew)
        self.lineEdit_Precio.setGeometry(QtCore.QRect(350, 30, 118, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Precio.sizePolicy().hasHeightForWidth())
        self.lineEdit_Precio.setSizePolicy(sizePolicy)
        self.lineEdit_Precio.setObjectName("lineEdit_Precio")
        self.tableWidget = QtWidgets.QTableWidget(interfazProductosNew)
        self.tableWidget.setGeometry(QtCore.QRect(60, 220, 601, 323))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.laberl_invInit = QtWidgets.QLabel(interfazProductosNew)
        self.laberl_invInit.setGeometry(QtCore.QRect(30, 140, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laberl_invInit.sizePolicy().hasHeightForWidth())
        self.laberl_invInit.setSizePolicy(sizePolicy)
        self.laberl_invInit.setObjectName("laberl_invInit")
        self.laberl_idCategoria = QtWidgets.QLabel(interfazProductosNew)
        self.laberl_idCategoria.setGeometry(QtCore.QRect(290, 90, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laberl_idCategoria.sizePolicy().hasHeightForWidth())
        self.laberl_idCategoria.setSizePolicy(sizePolicy)
        self.laberl_idCategoria.setObjectName("laberl_idCategoria")
        self.comboBox_categoria = QtWidgets.QComboBox(interfazProductosNew)
        self.comboBox_categoria.setGeometry(QtCore.QRect(350, 90, 121, 22))
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.spinBox_invInit = QtWidgets.QSpinBox(interfazProductosNew)
        self.spinBox_invInit.setGeometry(QtCore.QRect(120, 140, 46, 24))
        self.spinBox_invInit.setProperty("value", 1)
        self.spinBox_invInit.setObjectName("spinBox_invInit")
        self.spinBox_invInit.setMinimum(1)
        self.getCategorias()
        self.cargarDatosProductos()
        self.btnAdd.clicked.connect(self.crearProducto)
        self.retranslateUi(interfazProductosNew)
        QtCore.QMetaObject.connectSlotsByName(interfazProductosNew)

    def retranslateUi(self, interfazProductosNew):
        _translate = QtCore.QCoreApplication.translate
        interfazProductosNew.setWindowTitle(_translate("interfazProductosNew", "Productos"))
        self.label_codigo.setText(_translate("interfazProductosNew", "Código"))
        self.label_precio.setText(_translate("interfazProductosNew", "Precio"))
        self.btnAdd.setText(_translate("interfazProductosNew", "Añadir"))
        self.laberl_descripcion.setText(_translate("interfazProductosNew", "Descripcion"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("interfazProductosNew", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("interfazProductosNew", "Código"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("interfazProductosNew", "Descripcion"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("interfazProductosNew", "Precio"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("interfazProductosNew", "Inventario"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("interfazProductosNew", "Categoria"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("interfazProductosNew", "Opciones"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.laberl_invInit.setText(_translate("interfazProductosNew", "Inv inicial"))
        self.laberl_idCategoria.setText(_translate("interfazProductosNew", "Categoria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfazProductosNew = QtWidgets.QWidget()
    ui = Ui_interfazProductosNew()
    ui.setupUi(interfazProductosNew)
    interfazProductosNew.show()
    sys.exit(app.exec_())
