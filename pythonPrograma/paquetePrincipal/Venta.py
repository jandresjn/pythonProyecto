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
        self.total=None
        self.iva_total=None
        self.items_venta=[]
        self.bd=BaseDatos()
        self.conectarBD()

    def conectarBD(self):
        self.conn = sqlite3.connect("basedatos.db")
        self.cursor = self.conn.cursor()
