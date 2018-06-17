# -*- coding: utf-8 -*-
import sqlite3
from paquetePrincipal.BaseDatos import BaseDatos
import os
class Usuario:
    def __init__(self,id=None,nombreUsuario=None,contrasena=None):
        self.id=id
        self.nombreUsuario=nombreUsuario
        self.contrasena=contrasena
        self.bd=BaseDatos()
        self.conectarBD()
        if (id is not None):
            self.activo=1
            self.generaUsuarioConId()
        else: self.activo=0

    def conectarBD(self):
        self.conn = sqlite3.connect("paquetePrincipal/basedatos.db")
        self.cursor = self.conn.cursor()
        # self.conn,self.cursor=self.bd.conectarBD()

    def generaUsuarioConId(self):
        # sql = "SELECT nombre, contrasena FROM usuarios where id=? and activo=1"
        # self.cursor.execute(sql,[(self.id)])
        tabla="usuarios"
        camposSelect=["nombre","contrasena"]
        camposWhere=["id","activo"]
        tipoCampoWhere=[-1,1]
        datosUsuario=self.bd.generarValorCampoConId(tabla,camposSelect,camposWhere,tipoCampoWhere,self.id)
        # datosUsuario=self.cursor.fetchone()
        self.nombreUsuario=datosUsuario[0]
        self.contrasena=datosUsuario[1]
        print("nombres usuario viejo: "+ str(self.nombreUsuario))
        print ("contrasena usuario viejo: "+ str(self.contrasena))
        # print(datosUsuario)
        # print("repite?")


    def buscarUsuario(self,nombre,contrasena):
        # print("---------------------------")
        # cwd = os.getcwd()
        # print(cwd)

        # id=None
        tabla="usuarios"
        campos=["nombre","contrasena","activo"]
        tipoCampos=[-1,-1,1]
        valorCampos=[nombre,contrasena]
        id=self.bd.buscarValorCampo(tabla,campos,tipoCampos,valorCampos)
        # sql = "SELECT id FROM usuarios where nombre=? and contrasena=? and activo=1"
        # self.cursor.execute(sql, [(nombre),(contrasena)])
        # id=self.cursor.fetchone()
        if id is not None:
            self.id= id[0]
            self.nombreUsuario=nombre
            self.contrasena=contrasena
            self.activo=1
            return True
        else:
            return False

    def borrarUsuario(self):
        tabla="usuarios"
        self.bd.borrarValorCampo(tabla,self.id)

    def crearUsuario(self):
        tabla="usuarios"
        campos=["nombre","contrasena"]
        valorCampos=[self.nombreUsuario,self.contrasena]
        self.id=self.bd.crearValorCampo(tabla,campos,valorCampos)
        # sql = "INSERT INTO usuarios(nombre,contrasena) VALUES (?,?)"
        # self.cursor.execute(sql,
        #     [
        #         (self.nombreUsuario),
        #         (self.contrasena),
        #     ]
        # )
        # self.conn.commit()

        # self.id= self.cursor.lastrowid


    def actualizarUsuario(self,nombre,contrasena):
        tabla="usuarios"
        campos=["nombre","contrasena"]
        valorCampos=[nombre,contrasena,self.id]
        self.bd.actualizarValorCampo(tabla,campos,valorCampos)
        # sql = "UPDATE usuarios SET nombre=?, contrasena=? WHERE _rowid_=?"
        # self.cursor.execute(sql,
        #     [
        #         (nombre),
        #         (contrasena),
        #         (self.id)
        #     ]
        # )
        # self.conn.commit()
