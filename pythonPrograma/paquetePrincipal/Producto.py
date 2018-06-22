# -*- coding: utf-8 -*-
import sqlite3
from paquetePrincipal.BaseDatos import BaseDatos

import os
class Producto:

    def __init__(self,id=None,codigo=None,descripcion=None,precio=None,id_categoria=None,iva=None,cantidad=None,inventario=None):
        self.id=id
        self.codigo=codigo
        self.descripcion=descripcion
        self.precio=precio
        self.id_categoria=id_categoria
        self.categoria=None
        self.iva=iva
        self.cantidad=None
        self.inventario=inventario
        self.totalConIva=None
        self.totalSinIva=None
        self.bd=BaseDatos()
        self.conectarBD()





    def borrarProducto(self):
        tabla="productos"
        self.bd.borrarValorCampo(tabla,self.id)

    def crearProducto(self):
        tabla="productos"
        campos=["codigo","descripcion","precio","inventario","id_categoria"]
        print(str(self.codigo)+str(self.descripcion)+str(self.precio)+str(self.inventario)+str(self.id_categoria))
        valorCampos=[self.codigo,self.descripcion,self.precio,self.inventario,self.id_categoria]
        self.id=self.bd.crearValorCampo(tabla,campos,valorCampos)

    def cargarDatos(self):
        print("cargarDatos")
        self.arregloBotones=[]
        tabla="usuarios"
        camposSelect=["id","nombre","contrasena"]
        self.tableWidget.setRowCount(0)
        rows=self.bd.cargarDatosValorCampo(tabla,camposSelect)
        # conn = sqlite3.connect("basedatos.db")
        # cursor = conn.cursor()
        # cursor.execute('SELECT id, nombre, contrasena FROM usuarios WHERE activo = 1')
        # rows = cursor.fetchall()

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
            self.arregloBotones[inx].clicked.connect(self.borrarUsuario)

    def actualizarInventarioVenta(self):
        tabla="productos"
        campos=["inventario"]
        inventarioAct=self.inventario-self.cantidad
        print("inventarioAct: "+str(inventarioAct))
        print("id producto: "+str(self.id))
        valorCampos=[int(inventarioAct),self.id]
        self.bd.actualizarValorCampo(tabla,campos,valorCampos)

    def actualizarInventarioVenta2(self):
        tabla="productos"
        campos=["inventario"]
        inventarioAct=self.inventario+self.cantidad
        print("inventarioAct: "+str(inventarioAct))
        print("id producto: "+str(self.id))
        valorCampos=[int(inventarioAct),self.id]
        self.bd.actualizarValorCampo(tabla,campos,valorCampos)

    def calcularTotales(self):
        self.totalSinIva=self.precio*self.cantidad
        self.totalConIva=self.totalSinIva*(1+self.iva)
        print(self.totalSinIva)
        print(self.totalConIva)


    def conectarBD(self):
        self.conn = sqlite3.connect("basedatos.db")
        self.cursor = self.conn.cursor()
    def findCategoria(self):
        tabla="categorias"
        camposSelect=["nombre"]
        camposWhere=["id"]
        tipoCamposWhere=[-1]
        valorCamposWhere=[self.id_categoria]
        row=self.bd.buscarValorCamposGeneral(tabla,camposSelect,camposWhere,tipoCamposWhere,valorCamposWhere)
        self.categoria=row[0]

    def actualizarInfoProducto(self):
        tabla="productos"
        camposSelect=["descripcion","precio","inventario","id_categoria","id"]
        camposWhere=["codigo"]
        tipoCamposWhere=[-1]
        valorCamposWhere=[self.codigo]
        print(valorCamposWhere)

        rows=self.bd.buscarValorCamposGeneral(tabla,camposSelect,camposWhere,tipoCamposWhere,valorCamposWhere)
        self.descripcion=rows[0]
        self.precio=rows[1]
        self.inventario=rows[2]
        self.id_categoria=rows[3]
        self.findCategoria()
        self.id=rows[4]
