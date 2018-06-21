# -*- coding: utf-8 -*-
import sqlite3
from paquetePrincipal.BaseDatos import BaseDatos
import os
class Venta:

    def __init__(self,id=None,id_cliente=None,id_usuario=None,fecha=None):
        self.id=id
        self.id_cliente=id_cliente
        self.id_usuario=id_usuario
        self.fecha=fecha
        self.total=0
        self.iva_total=0
        self.iva_total_desc=0
        self.items_venta=[]
        self.medioPago=None
        self.descuento=None
        self.bd=BaseDatos()
        self.conectarBD()

    def conectarBD(self):
        self.conn = sqlite3.connect("basedatos.db")
        self.cursor = self.conn.cursor()

    def clearAll(self):
        self.id_cliente=None
        self.total=0
        self.iva_total=0
        self.iva_total_desc=0
        self.items_venta=[]
        self.medioPago=None
        self.descuento=None

    def buscarItemVenta(self):
        print("cargarDatos")
        self.arregloBotones=[]
        tabla="items_venta"
        camposSelect=["id","nombre","contrasena"]
        self.tableWidget.setRowCount(0)
        rows=self.bd.cargarDatosValorCampo(tabla,camposSelect)
    def guardarVenta(self):
        tabla="ventas"
        print("id cliente: "+str(self.id_cliente))
        print("id_usuario: "+str(self.id_usuario))
        campos=["id_cliente","id_usuario","fecha","total","iva_total","medio_pago_id"]
        valorCampos=[self.id_cliente,self.id_usuario,self.fecha,self.total,self.iva_total_desc,self.medioPago]
        self.id=self.bd.crearValorCampo(tabla,campos,valorCampos)
        self.guardarItemsVenta()
    def guardarItemsVenta(self):
        tabla="items_venta"
        campos=["id_venta","precio","cantidad","iva","id_producto","total"]
        for item in self.items_venta:
            valorCampos=[self.id,item.precio,item.cantidad,item.iva,item.id,item.totalSinIva]
            id_item=self.bd.crearValorCampo(tabla,campos,valorCampos)
            item.actualizarInventarioVenta()
