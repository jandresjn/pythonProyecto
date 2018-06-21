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
        self.inventario=None
        self.totalConIva=None
        self.totalSinIva=None
        self.bd=BaseDatos()
        self.conectarBD()

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
        camposSelect=["descripcion","precio","inventario","id_categoria"]
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
