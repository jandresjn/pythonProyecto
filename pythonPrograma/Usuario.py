# -*- coding: utf-8 -*-
import sqlite3

class Usuario:
    def __init__(self,id=None,nombreUsuario=None,contrasena=None):
        self.id=id
        self.nombreUsuario=nombreUsuario
        self.contrasena=contrasena
        self.conectarBD()
        if (id is not None):
            self.activo=1
            self.generaUsuarioConId()
        else: self.activo=0

    def generaUsuarioConId(self):
        sql = "SELECT nombre, contrasena FROM usuarios where id=? and activo=1"
        self.cursor.execute(sql,[(self.id)])
        datosUsuario=self.cursor.fetchone()
        print(datosUsuario)
        print("repite?")


    def conectarBD(self):
        self.conn = sqlite3.connect("basedatos.db")
        self.cursor = self.conn.cursor()

    def buscarUsuario(self,nombre,contrasena):
        sql = "SELECT id FROM usuarios where nombre=? and contrasena=? and activo=1"
        self.cursor.execute(sql, [(nombre),(contrasena)])
        id=self.cursor.fetchone()
        if id is not None:
            self.id= id[0]
            self.nombreUsuario=nombre
            self.contrasena=contrasena
            self.activo=1
            return True
        else:
            return False
    def crearUsuario(self):

        sql = "INSERT INTO usuarios(nombre,contrasena) VALUES (?,?)"
        self.cursor.execute(sql,
            [
                (self.nombreUsuario),
                (self.contrasena),
            ]
        )
        self.conn.commit()

        self.id= self.cursor.lastrowid


    def actualizarUsuario(self,nombre,contrasena):
        sql = "UPDATE usuarios SET nombre=?, contrasena=? WHERE _rowid_=?"
        self.cursor.execute(sql,
            [
                (nombre),
                (contrasena),
                (self.id)
            ]
        )
        self.conn.commit()
