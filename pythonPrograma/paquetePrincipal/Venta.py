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
        self.descuento=None
