# -*- coding: utf-8 -*-
import sqlite3
from paquetePrincipal.BaseDatos import BaseDatos

class Cliente:

    def __init__(self,id=None,nombreUsuario=None,numero_documento=None):
        self.id=id
        self.nombreUsuario=nombreUsuario
        self.numero_documento=numero_documento
        self.bd=BaseDatos()
        self.conectarBD()
        if (id is not None):
            self.activo=1
            self.generaClienteConId()
        else: self.activo=0

    def getNombreUsuario(self):
        tabla="clientes"
        camposSelect=["nombre"]
        camposWhere=["numero_documento","activo"]
        tipoCampoWhere=[-1,1]
        datoNombre=self.bd.generarValorCampoConId(tabla,camposSelect,camposWhere,tipoCampoWhere,self.numero_documento)
        self.nombreUsuario=datoNombre[0]
        print("Dato nombre es: ")
        print(datoNombre[0])

    def buscarClienteDoc(self,numero_documento):
        # id=None
        tabla="clientes"
        campos=["numero_documento","activo"]
        tipoCampos=[-1,1]
        valorCampos=[numero_documento]
        id=self.bd.buscarValorCampo(tabla,campos,tipoCampos,valorCampos)
        # sql = "SELECT id FROM usuarios where nombre=? and contrasena=? and activo=1"
        # self.cursor.execute(sql, [(nombre),(contrasena)])
        # id=self.cursor.fetchone()
        if id is not None:
            self.id= id[0]
            self.numero_documento=numero_documento
            self.activo=1
            self.getNombreUsuario()
            return True
        else:
            return False

    def crearCliente(self):
        tabla="clientes"
        campos=["nombre","numero_documento"]
        valorCampos=[self.nombreUsuario,self.numero_documento]
        self.id=self.bd.crearValorCampo(tabla,campos,valorCampos)

    def conectarBD(self):
        self.conn = sqlite3.connect("basedatos.db")
        self.cursor = self.conn.cursor()

    def generaClienteConId(self):
        # sql = "SELECT nombre, contrasena FROM usuarios where id=? and activo=1"
        # self.cursor.execute(sql,[(self.id)])
        tabla="clientes"
        camposSelect=["nombre","numero_documento"]
        camposWhere=["id","activo"]
        tipoCampoWhere=[-1,1]
        datosUsuario=self.bd.generarValorCampoConId(tabla,camposSelect,camposWhere,tipoCampoWhere,self.id)
        # datosUsuario=self.cursor.fetchone()
        self.nombreUsuario=datosUsuario[0]
        self.numero_documento=datosUsuario[1]
        print("nombres usuario viejo: "+ str(self.nombreUsuario))
        print ("numero_documento usuario viejo: "+ str(self.numero_documento))

    def borrarCliente(self):
        tabla="clientes"
        self.bd.borrarValorCampo(tabla,self.id)
