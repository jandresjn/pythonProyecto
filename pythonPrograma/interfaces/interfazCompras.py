# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazVentas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from paquetePrincipal.BaseDatos import BaseDatos
from paquetePrincipal.Proveedor import Proveedor
from paquetePrincipal.Compra import Compra
from paquetePrincipal.Producto import Producto
from datetime import datetime

import sqlite3
class Ui_comprasObject(object):
    def confirmarVenta(self):
        mpago=self.identificaMedioPago()
        self.ventaActual.medioPago=mpago
        if self.cantidadItems > 0:
            self.ventaActual.guardarVenta()
            self.resetearVenta()


    def calcularTotalesVenta(self):
        self.ventaActual.total=0
        self.ventaActual.iva_total=0
        self.ventaActual.iva_total_desc=0
        for index in range(len(self.ventaActual.items_venta)):
            print("TOTAL ITEM: "+str(self.ventaActual.items_venta[index].totalSinIva))
            print("TOTAL VENTA: "+ str(self.ventaActual.total))
            self.ventaActual.total=self.ventaActual.total+self.ventaActual.items_venta[index].totalSinIva
            self.ventaActual.iva_total= self.ventaActual.iva_total+float(self.ventaActual.items_venta[index].totalConIva)
            descuento=self.identificaDescuento()
            self.ventaActual.iva_total_desc=self.ventaActual.iva_total_desc+float(self.ventaActual.items_venta[index].totalSinIva*(1+self.ventaActual.items_venta[index].iva))*(1-descuento)
        print("TOTAL: "+str(self.ventaActual.total))
        print("TOTAL IVA: "+str(self.ventaActual.iva_total))
        print("TOTAL IVA DESC: "+str(self.ventaActual.iva_total_desc))
        self.lineEdit_mostrarTotalConDesc.setText(str(self.ventaActual.iva_total_desc))

    def agregarItem(self):
        self.ventaActual.items_venta.append(self.itemVenta)
        if (len(self.ventaActual.items_venta)) != 0 and ((len(self.ventaActual.items_venta)-1)==self.cantidadItems) and self.ventaActual.items_venta[-1] is not None:
            self.ventaActual.items_venta[self.cantidadItems].iva=float(self.spinBox_IVA.value())/100
            print(self.ventaActual.items_venta[self.cantidadItems].iva)
            self.ventaActual.items_venta[self.cantidadItems].cantidad=int(self.spinBox_cantidadItem.value())
            self.ventaActual.items_venta[self.cantidadItems].calcularTotales()
            filasTabla = self.tableWidget_itemVentas.rowCount()
            boton = QtWidgets.QPushButton()
            boton.setText('Borrar')
            boton.clicked.connect(self.borrarItem)

            self.tableWidget_itemVentas.blockSignals(True)

            self.tableWidget_itemVentas.insertRow( filasTabla )
            self.tableWidget_itemVentas.setItem( filasTabla, 0, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].codigo)))
            self.tableWidget_itemVentas.setItem( filasTabla, 1, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].descripcion)))
            self.tableWidget_itemVentas.setItem( filasTabla, 2, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].categoria)))
            self.tableWidget_itemVentas.setItem( filasTabla, 3, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].precio)))
            self.tableWidget_itemVentas.setItem( filasTabla, 4, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].cantidad)))
            self.tableWidget_itemVentas.setItem( filasTabla, 5, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].iva)))
            self.tableWidget_itemVentas.setItem( filasTabla, 6, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].totalSinIva)))
            self.tableWidget_itemVentas.setItem( filasTabla, 7, QtWidgets.QTableWidgetItem(str(self.ventaActual.items_venta[self.cantidadItems].totalConIva)))


            self.tableWidget_itemVentas.setCellWidget( filasTabla, 8, boton)

            self.tableWidget_itemVentas.blockSignals(False)
            self.calcularTotalesVenta()
            self.cantidadItems+=1
        else:
            self.label_errorCodigo.setText("NO SE PUEDE AÑADIR")


    def buscarInfoCodigo(self):
        tabla="productos"
        campos=["codigo","activo"]
        tipoCampos=[-1,1]
        if self.lineEdit_codigo_Item.text() != "":
            id_producto=self.bd.buscarValorCampo(tabla,campos,tipoCampos,[self.lineEdit_codigo_Item.text()])
            if id_producto is not None:
                self.itemVenta=Producto(id=id_producto,codigo=self.lineEdit_codigo_Item.text())
                self.itemVenta.actualizarInfoProducto()
                # self.ventaActual.items_venta.append(Producto(id=id_producto,codigo=self.lineEdit_codigo_Item.text()))
                # self.ventaActual.items_venta[self.cantidadItems].actualizarInfoProducto()
                self.lineEdit_mostrarDescripcionItem.setText(str(self.itemVenta.descripcion))
                self.lineEdit_mostrarPrecioUnitario.setText(str(self.itemVenta.precio))
                self.lineEdit_mostrarInventarioDisp.setText(str(self.itemVenta.inventario))
                self.lineEdit_mostrarCategoria.setText(str(self.itemVenta.categoria))
                if self.itemVenta.inventario != 0:
                    self.spinBox_cantidadItem.setMaximum(self.itemVenta.inventario)
                self.label_errorCodigo.setText("ITEM ENCONTRADO")

            else:
                # self.clearInfoProductoBase():
                self.label_errorCodigo.setText("ITEM NO ENCONTRADO")


    def clearInfoProductoBase(self):
        self.lineEdit_mostrarDescripcionItem.clear()
        self.lineEdit_mostrarPrecioUnitario.clear()
        self.lineEdit_mostrarInventarioDisp.clear()
        self.lineEdit_mostrarCategoria.clear()
    def buscarItem(self):
        tabla="productos"
        campos=["codigo","descripcion","id_categoria"]
        c3=self.identificaCategoria()
        # print("c3")
        # print(c3)
        valorCampos=[]
        valorCampos=[self.lineEdit_codigo_buscar.text(),self.lineEdit_descripcion_buscar.text(),str(c3)]
        print(valorCampos)
        if (valorCampos[0] or valorCampos[1]) or valorCampos[2]  != "" :
            if valorCampos[0] == "":
                valorCampos[0]="  "
            if valorCampos[1] == "":
                valorCampos[1]="0"

            rows=self.bd.buscarDatosLike(tabla,campos,valorCampos)
            self.listWidget_buscarItems.clear()
            self.listWidget_buscarItems.addItem("(id, codigo, descripcion, precio, inv, categoria)")
            for row in rows :
                self.listWidget_buscarItems.addItem(str(row))

    def vincularCliente(self):
        existeCliente=self.clienteActual.buscarProveedorDoc(self.lineEdit_clienteActivo.text())
        if existeCliente:
            self.ventaActual.id_cliente=self.clienteActual.id
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            self.label_errorClienteActivo.setPalette(palette)
            self.label_errorClienteActivo.setText("VINCULACIÓN EXITOSA!")
            self.habilitarBotonesPrincipales()
            self.lineEdit_clienteActivo.setEnabled(False)
            self.pushButton_vincularCliente.setEnabled(False)
            self.label_mostrar_nombreClienteActivo.setText(self.clienteActual.nombreUsuario)
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            self.label_errorClienteActivo.setPalette(palette)
            self.label_errorClienteActivo.setText("DOC NO ENCONTRADO")
    def resetearVenta(self):
        self.deshabilitarBotonesPrincipales()
        self.ventaActual.id=None
        self.ventaActual.items_venta=[]
        self.ventaActual.id_cliente=None
        self.lineEdit_clienteActivo.clear()
        self.label_mostrar_nombreClienteActivo.clear()
        self.lineEdit_codigo_Item.clear()
        self.label_errorClienteActivo.clear()
        # self.tableWidget_itemVentas.clear()
        self.borrarTabla()
        self.cantidadItems=0
        self.ventaActual.clearAll()

        self.clearInfoProductoBase()
        self.lineEdit_mostrarTotalConDesc.clear()

    def deshabilitarBotonesPrincipales(self):
        self.pushButton_agregarItemVenta.setEnabled(False)
        self.pushButton_confirmarVenta.setEnabled(False)
        self.lineEdit_clienteActivo.setEnabled(True)
        self.pushButton_vincularCliente.setEnabled(True)
        self.lineEdit_codigo_Item.setEnabled(False)
        self.label_codigo_item.setEnabled(False)

    def borrarItem(self):
        print("borrarUsuario")
        ArregloBotonClicked=QtWidgets.qApp.focusWidget()
        index = self.tableWidget_itemVentas.indexAt(ArregloBotonClicked.pos())
        if index.isValid():

            print("-----------")
            print(index.row())
            del self.ventaActual.items_venta[index.row()]
            print("---------")
            for i in range(len(self.ventaActual.items_venta)):
                print(str(self.ventaActual.items_venta[i].descripcion))
            self.tableWidget_itemVentas.removeRow(index.row())
            self.cantidadItems-=1
            self.calcularTotalesVenta()


    def borrarTabla(self):
        print("Row Count: ")
        print(self.tableWidget_itemVentas.rowCount())
        # tableWidget_itemVentas.
        for i in range(self.tableWidget_itemVentas.rowCount()):
            self.tableWidget_itemVentas.removeRow(0)
            print(i)

    def getDescuentos(self):
        rows=self.bd.cargarTodo("descuentos")
        for index in range(len(rows)):
            self.descuentos_desc.append(str(rows[index][1]))
            self.descuentos_valor.append(float(rows[index][2]))
        print("descuentos")
        print(self.descuentos_desc)
        self.comboBox_itemDescuento.addItems(self.descuentos_desc)

    def identificaDescuento(self):
        idx=self.comboBox_itemDescuento.currentIndex()
        descuento=self.descuentos_valor[idx]
        return descuento

    def getCategorias(self):
        rows=self.bd.cargarTodo("categorias")
        for index in range(len(rows)):
            self.categorias.append(str(rows[index][1]))
            self.categoriasId.append(int(rows[index][0]))
        print("categorias")
        print(self.categorias)
        self.comboBox_categoria_buscar.addItems(self.categorias)

    def getmediosPago(self):
        rows=self.bd.cargarTodo("sistema_pagos")
        for index in range(len(rows)):
            self.medioPagos.append(str(rows[index][2]))
            self.medioPagos_cod.append(str(rows[index][1]))
        print("categorias")
        print(self.medioPagos)
        self.comboBox_item_medioPago.addItems(self.medioPagos)

    def identificaMedioPago(self):
        idx=self.comboBox_item_medioPago.currentIndex()
        medioPago=self.medioPagos_cod[idx]
        return medioPago

    def identificaCategoria(self):
        idx=self.comboBox_categoria_buscar.currentIndex()
        categoria=self.categoriasId[idx]
        return categoria



    def habilitarBotonesPrincipales(self):
        self.pushButton_agregarItemVenta.setEnabled(True)
        self.pushButton_confirmarVenta.setEnabled(True)
        self.lineEdit_codigo_Item.setEnabled(True)
        self.label_codigo_item.setEnabled(True)
    def setupUi(self, ventasObject,usuarioActual):
        self.categorias=[]
        self.categoriasId=[]
        self.descuentos_desc=[]
        self.descuentos_valor=[]
        self.medioPagos=[]
        self.medioPagos_cod=[]
        self.cantidadItems=0
        self.bd=BaseDatos()
        self.clienteActual=Proveedor()
        self.ventaActual=Compra(id_usuario=usuarioActual.id)
        now = datetime.now()
        self.ventaActual.fecha=str(now.year)+"/"+str(now.month)+"/"+str(now.day)
        print(self.ventaActual.fecha)

        ventasObject.setObjectName("ventasObject")
        ventasObject.resize(800, 600)
        ventasObject.setMinimumSize(QtCore.QSize(800, 600))
        ventasObject.setMaximumSize(QtCore.QSize(800, 600))
        ventasObject.setAcceptDrops(True)
        self.pushButton_vincularCliente = QtWidgets.QPushButton(ventasObject)
        self.pushButton_vincularCliente.setGeometry(QtCore.QRect(650, 90, 121, 31))
        self.pushButton_vincularCliente.setObjectName("pushButton_vincularCliente")
        self.label_ClienteActivo = QtWidgets.QLabel(ventasObject)
        self.label_ClienteActivo.setGeometry(QtCore.QRect(660, 0, 91, 31))
        self.label_ClienteActivo.setObjectName("label_ClienteActivo")

        self.label_usuarioActivo = QtWidgets.QLabel(ventasObject)
        self.label_usuarioActivo.setGeometry(QtCore.QRect(10, 10,181, 21))
        self.label_usuarioActivo.setObjectName("label_ClienteActivo")
        self.label_usuarioActivo.setText("Usuario: "+str(usuarioActual.nombreUsuario))

        self.label_id_clienteActivo = QtWidgets.QLabel(ventasObject)
        self.label_id_clienteActivo.setGeometry(QtCore.QRect(610, 30, 21, 21))
        self.label_id_clienteActivo.setObjectName("label_id_clienteActivo")
        self.label_nombre_clienteActivo = QtWidgets.QLabel(ventasObject)
        self.label_nombre_clienteActivo.setGeometry(QtCore.QRect(580, 70, 57, 14))
        self.label_nombre_clienteActivo.setObjectName("label_nombre_clienteActivo")
        self.lineEdit_clienteActivo = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_clienteActivo.setGeometry(QtCore.QRect(640, 30, 151, 26))
        self.lineEdit_clienteActivo.setObjectName("lineEdit_clienteActivo")
        self.label_errorClienteActivo = QtWidgets.QLabel(ventasObject)
        self.label_errorClienteActivo.setGeometry(QtCore.QRect(580, 130, 201, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 112, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_errorClienteActivo.setPalette(palette)
        self.label_errorClienteActivo.setObjectName("label_errorClienteActivo")
        self.label_mostrar_nombreClienteActivo = QtWidgets.QLabel(ventasObject)
        self.label_mostrar_nombreClienteActivo.setGeometry(QtCore.QRect(640, 70, 151, 16))
        self.label_mostrar_nombreClienteActivo.setText("")
        self.label_mostrar_nombreClienteActivo.setObjectName("label_mostrar_nombreClienteActivo")
        self.label_buscadorItems = QtWidgets.QLabel(ventasObject)
        self.label_buscadorItems.setGeometry(QtCore.QRect(220, 10, 131, 16))
        self.label_buscadorItems.setObjectName("label_buscadorItems")
        self.listWidget_buscarItems = QtWidgets.QListWidget(ventasObject)
        self.listWidget_buscarItems.setGeometry(QtCore.QRect(70, 90, 451, 91))
        self.listWidget_buscarItems.setObjectName("listWidget_buscarItems")
        item = QtWidgets.QListWidgetItem()
        # self.listWidget_buscarItems.addItem(item)
        self.tableWidget_itemVentas = QtWidgets.QTableWidget(ventasObject)
        self.tableWidget_itemVentas.setGeometry(QtCore.QRect(50, 350, 711, 171))
        self.tableWidget_itemVentas.setObjectName("tableWidget_itemVentas")
        self.tableWidget_itemVentas.setColumnCount(9)
        self.tableWidget_itemVentas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_itemVentas.setHorizontalHeaderItem(8, item)
        self.pushButton_confirmarVenta = QtWidgets.QPushButton(ventasObject)
        self.pushButton_confirmarVenta.setGeometry(QtCore.QRect(650, 550, 121, 31))
        self.pushButton_confirmarVenta.setObjectName("pushButton_confirmarVenta")
        self.pushButton_cancelarVenta = QtWidgets.QPushButton(ventasObject)
        self.pushButton_cancelarVenta.setGeometry(QtCore.QRect(510, 550, 121, 31))
        self.pushButton_cancelarVenta.setObjectName("pushButton_cancelarVenta")


        self.label_infoProducto = QtWidgets.QLabel(ventasObject)
        self.label_infoProducto.setGeometry(QtCore.QRect(50, 190, 211, 16))
        self.label_infoProducto.setObjectName("label_infoProducto")
        self.pushButton_agregarItemVenta = QtWidgets.QPushButton(ventasObject)
        self.pushButton_agregarItemVenta.setGeometry(QtCore.QRect(580, 280, 191, 51))
        self.pushButton_agregarItemVenta.setObjectName("pushButton_agregarItemVenta")
        self.label_codigo_item = QtWidgets.QLabel(ventasObject)
        self.label_codigo_item.setGeometry(QtCore.QRect(50, 220, 51, 21))
        self.label_codigo_item.setObjectName("label_codigo_item")
        self.lineEdit_codigo_Item = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_codigo_Item.setGeometry(QtCore.QRect(40, 240, 81, 26))
        self.lineEdit_codigo_Item.setObjectName("lineEdit_codigo_Item")
        self.label_descripcion = QtWidgets.QLabel(ventasObject)
        self.label_descripcion.setGeometry(QtCore.QRect(60, 280, 91, 16))
        self.label_descripcion.setObjectName("label_descripcion")


        self.label_codigo_buscar = QtWidgets.QLabel(ventasObject)
        self.label_codigo_buscar.setGeometry(QtCore.QRect(80, 40, 81, 16))
        self.label_codigo_buscar.setObjectName("label_codigo_buscar")
        self.label_descripcion_buscar = QtWidgets.QLabel(ventasObject)
        self.label_descripcion_buscar.setGeometry(QtCore.QRect(200, 40, 57, 14))
        self.label_descripcion_buscar.setObjectName("label_descripcion_buscar")
        self.spinBox_cantidadItem = QtWidgets.QSpinBox(ventasObject)
        self.spinBox_cantidadItem.setGeometry(QtCore.QRect(490, 300, 41, 24))
        self.spinBox_cantidadItem.setProperty("value", 1)
        self.spinBox_cantidadItem.setObjectName("spinBox_cantidadItem")
        self.spinBox_cantidadItem.setMinimum(1)
        self.comboBox_categoria_buscar = QtWidgets.QComboBox(ventasObject)
        self.comboBox_categoria_buscar.setGeometry(QtCore.QRect(300, 60, 141, 22))
        self.comboBox_categoria_buscar.setObjectName("comboBox_categoria_buscar")
        # self.comboBox_categoria_buscar.addItem("")
        # self.comboBox_categoria_buscar.addItem("")
        self.label_categoria_buscar = QtWidgets.QLabel(ventasObject)
        self.label_categoria_buscar.setGeometry(QtCore.QRect(320, 40, 57, 14))
        self.label_categoria_buscar.setObjectName("label_categoria_buscar")
        self.label_inventarioDisp = QtWidgets.QLabel(ventasObject)
        self.label_inventarioDisp.setGeometry(QtCore.QRect(160, 280, 91, 16))
        self.label_inventarioDisp.setObjectName("label_inventarioDisp")
        self.label_categoria_item = QtWidgets.QLabel(ventasObject)
        self.label_categoria_item.setGeometry(QtCore.QRect(260, 280, 91, 16))
        self.label_categoria_item.setObjectName("label_categoria_item")
        self.comboBox_itemDescuento = QtWidgets.QComboBox(ventasObject)
        self.comboBox_itemDescuento.setGeometry(QtCore.QRect(570, 240, 141, 22))
        self.comboBox_itemDescuento.setObjectName("comboBox_itemDescuento")
        # self.comboBox_itemDescuento.addItem("")
        # self.comboBox_itemDescuento.addItem("")
        self.label_cantidadItem = QtWidgets.QLabel(ventasObject)
        self.label_cantidadItem.setGeometry(QtCore.QRect(480, 280, 91, 16))
        self.label_cantidadItem.setObjectName("label_cantidadItem")
        self.label_descuento = QtWidgets.QLabel(ventasObject)
        self.label_descuento.setGeometry(QtCore.QRect(600, 220, 91, 16))
        self.label_descuento.setObjectName("label_descuento")
        self.lineEdit_mostrarDescripcionItem = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_mostrarDescripcionItem.setGeometry(QtCore.QRect(40, 300, 113, 26))
        self.lineEdit_mostrarDescripcionItem.setText("")
        self.lineEdit_mostrarDescripcionItem.setReadOnly(True)
        self.lineEdit_mostrarDescripcionItem.setClearButtonEnabled(False)
        self.lineEdit_mostrarDescripcionItem.setObjectName("lineEdit_mostrarDescripcionItem")
        self.lineEdit_mostrarInventarioDisp = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_mostrarInventarioDisp.setGeometry(QtCore.QRect(180, 300, 31, 26))
        self.lineEdit_mostrarInventarioDisp.setText("")
        self.lineEdit_mostrarInventarioDisp.setReadOnly(True)
        self.lineEdit_mostrarInventarioDisp.setClearButtonEnabled(False)
        self.lineEdit_mostrarInventarioDisp.setObjectName("lineEdit_mostrarInventarioDisp")
        self.lineEdit_mostrarCategoria = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_mostrarCategoria.setGeometry(QtCore.QRect(240, 300, 113, 26))
        self.lineEdit_mostrarCategoria.setText("")
        self.lineEdit_mostrarCategoria.setReadOnly(True)
        self.lineEdit_mostrarCategoria.setClearButtonEnabled(False)
        self.lineEdit_mostrarCategoria.setObjectName("lineEdit_mostrarCategoria")
        self.label_precio = QtWidgets.QLabel(ventasObject)
        self.label_precio.setGeometry(QtCore.QRect(170, 220, 91, 16))
        self.label_precio.setObjectName("label_precio")
        self.lineEdit_mostrarPrecioUnitario = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_mostrarPrecioUnitario.setGeometry(QtCore.QRect(160, 240, 113, 26))
        self.lineEdit_mostrarPrecioUnitario.setText("")
        self.lineEdit_mostrarPrecioUnitario.setReadOnly(True)
        self.lineEdit_mostrarPrecioUnitario.setClearButtonEnabled(False)
        self.lineEdit_mostrarPrecioUnitario.setObjectName("lineEdit_mostrarPrecioUnitario")
        self.label_infoProducto_2 = QtWidgets.QLabel(ventasObject)
        self.label_infoProducto_2.setGeometry(QtCore.QRect(360, 190, 341, 21))
        self.label_infoProducto_2.setObjectName("label_infoProducto_2")
        self.label_medioPago = QtWidgets.QLabel(ventasObject)
        self.label_medioPago.setGeometry(QtCore.QRect(400, 220, 91, 16))
        self.label_medioPago.setObjectName("label_medioPago")
        self.comboBox_item_medioPago = QtWidgets.QComboBox(ventasObject)
        self.comboBox_item_medioPago.setGeometry(QtCore.QRect(380, 240, 141, 22))
        self.comboBox_item_medioPago.setObjectName("comboBox_item_medioPago")
        # self.comboBox_item_medioPago.addItem("")
        # self.comboBox_item_medioPago.addItem("")
        self.lineEdit_codigo_buscar = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_codigo_buscar.setGeometry(QtCore.QRect(60, 60, 113, 26))
        self.lineEdit_codigo_buscar.setObjectName("lineEdit_codigo_buscar")
        self.lineEdit_descripcion_buscar = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_descripcion_buscar.setGeometry(QtCore.QRect(180, 60, 113, 26))
        self.lineEdit_descripcion_buscar.setObjectName("lineEdit_descripcion_buscar")
        self.label_errorCodigo = QtWidgets.QLabel(ventasObject)
        self.label_errorCodigo.setGeometry(QtCore.QRect(30, 560, 201, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 112, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_errorCodigo.setPalette(palette)
        self.label_errorCodigo.setText("")
        self.label_errorCodigo.setObjectName("label_errorCodigo")
        self.label_total_desc = QtWidgets.QLabel(ventasObject)
        self.label_total_desc.setGeometry(QtCore.QRect(250, 550, 91, 20))
        self.label_total_desc.setObjectName("label_total_desc")
        self.lineEdit_mostrarTotalConDesc = QtWidgets.QLineEdit(ventasObject)
        self.lineEdit_mostrarTotalConDesc.setGeometry(QtCore.QRect(340, 540, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_mostrarTotalConDesc.setFont(font)
        self.lineEdit_mostrarTotalConDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mostrarTotalConDesc.setReadOnly(True)
        self.lineEdit_mostrarTotalConDesc.setClearButtonEnabled(False)
        self.lineEdit_mostrarTotalConDesc.setObjectName("lineEdit_mostrarTotalConDesc")
        self.label_IVA = QtWidgets.QLabel(ventasObject)
        self.label_IVA.setGeometry(QtCore.QRect(400, 280, 41, 16))
        self.label_IVA.setObjectName("label_IVA")
        self.spinBox_IVA = QtWidgets.QSpinBox(ventasObject)
        self.spinBox_IVA.setGeometry(QtCore.QRect(400, 300, 41, 24))
        self.spinBox_IVA.setProperty("value", 19)
        self.spinBox_IVA.setObjectName("spinBox_IVA")
        self.pushButton_buscar = QtWidgets.QPushButton(ventasObject)
        self.pushButton_buscar.setGeometry(QtCore.QRect(460, 30, 71, 51))
        self.pushButton_buscar.setObjectName("pushButton_buscar")

        self.deshabilitarBotonesPrincipales()
        self.pushButton_cancelarVenta.clicked.connect(self.resetearVenta)
        self.pushButton_vincularCliente.clicked.connect(self.vincularCliente)
        self.pushButton_buscar.clicked.connect(self.buscarItem)
        self.lineEdit_codigo_Item.returnPressed.connect(self.buscarInfoCodigo)
        self.pushButton_agregarItemVenta.clicked.connect(self.agregarItem)
        self.pushButton_confirmarVenta.clicked.connect(self.confirmarVenta)
        self.getCategorias()
        self.getDescuentos()
        self.getmediosPago()
        self.retranslateUi(ventasObject)
        QtCore.QMetaObject.connectSlotsByName(ventasObject)

    def retranslateUi(self, ventasObject):
        _translate = QtCore.QCoreApplication.translate
        ventasObject.setWindowTitle(_translate("ventasObject", "Compras"))
        self.pushButton_vincularCliente.setText(_translate("ventasObject", "Vincular Proveedor"))
        self.label_ClienteActivo.setText(_translate("ventasObject", "Cliente Proveedor:"))
        self.label_id_clienteActivo.setText(_translate("ventasObject", "Id: "))
        self.label_nombre_clienteActivo.setText(_translate("ventasObject", "Nombre: "))
        self.label_errorClienteActivo.setText(_translate("ventasObject", "VINCULE PROVEEDOR EXISTENTE"))
        self.label_buscadorItems.setText(_translate("ventasObject", "Buscador de items:"))
        __sortingEnabled = self.listWidget_buscarItems.isSortingEnabled()
        self.listWidget_buscarItems.setSortingEnabled(False)
        self.listWidget_buscarItems.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_itemVentas.horizontalHeaderItem(0)
        item.setText(_translate("ventasObject", "Codigo"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(1)
        item.setText(_translate("ventasObject", "Descripcion"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(2)
        item.setText(_translate("ventasObject", "Categoria"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(3)
        item.setText(_translate("ventasObject", "Precio"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(4)
        item.setText(_translate("ventasObject", "Cantidad"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(5)
        item.setText(_translate("ventasObject", "IVA"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(6)
        item.setText(_translate("ventasObject", "Total sin IVA"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(7)
        item.setText(_translate("ventasObject", "Total + IVA"))
        item = self.tableWidget_itemVentas.horizontalHeaderItem(8)
        item.setText(_translate("ventasObject", "Borrar"))
        self.pushButton_confirmarVenta.setText(_translate("ventasObject", "Confirmar Compra"))
        self.pushButton_cancelarVenta.setText(_translate("ventasObject", "Cancelar Compra"))
        self.label_infoProducto.setText(_translate("ventasObject", "Registro e Informacion de Producto:"))
        self.pushButton_agregarItemVenta.setText(_translate("ventasObject", "Agregar Item"))
        self.label_codigo_item.setText(_translate("ventasObject", "Codigo* "))
        self.label_descripcion.setText(_translate("ventasObject", "Descripcion"))
        self.label_codigo_buscar.setText(_translate("ventasObject", "Codigo"))
        self.label_descripcion_buscar.setText(_translate("ventasObject", "Descripcion"))
        # self.comboBox_categoria_buscar.setItemText(0, _translate("ventasObject", "Frutas"))
        # self.comboBox_categoria_buscar.setItemText(1, _translate("ventasObject", "Carnes"))
        self.label_categoria_buscar.setText(_translate("ventasObject", "Categorias"))
        self.label_inventarioDisp.setText(_translate("ventasObject", "Inv Disponible"))
        self.label_categoria_item.setText(_translate("ventasObject", "Categoria"))
        # self.comboBox_itemDescuento.setItemText(0, _translate("ventasObject", "Sin Descuento"))
        # self.comboBox_itemDescuento.setItemText(1, _translate("ventasObject", "Descuento 10%"))
        self.label_cantidadItem.setText(_translate("ventasObject", "Cantidad*"))
        self.label_descuento.setText(_translate("ventasObject", "Descuento"))
        self.label_precio.setText(_translate("ventasObject", "Precio Unitario"))
        self.label_infoProducto_2.setText(_translate("ventasObject", "Seleccione Descuento y Medio de Pago para toda la venta :"))
        self.label_medioPago.setText(_translate("ventasObject", "Medio de Pago"))
        # self.comboBox_item_medioPago.setItemText(0, _translate("ventasObject", "Sin Descuento"))
        # self.comboBox_item_medioPago.setItemText(1, _translate("ventasObject", "Descuento 10%"))
        self.label_total_desc.setText(_translate("ventasObject", "TOTAL - DESC:"))
        self.lineEdit_mostrarTotalConDesc.setText(_translate("ventasObject", "0"))
        self.label_IVA.setText(_translate("ventasObject", "IVA %"))
        self.pushButton_buscar.setText(_translate("ventasObject", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventasObject = QtWidgets.QWidget()
    ui = Ui_comprasObject()
    ui.setupUi(ventasObject)
    ventasObject.show()
    sys.exit(app.exec_())
