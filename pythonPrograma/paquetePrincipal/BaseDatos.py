# -*- coding: utf-8 -*-
import sqlite3

class BaseDatos:

    def __init__(self,baseDatos ="basedatos.db"):
        self.baseDatos=baseDatos
        self.conectarBD()

    def conectarBD(self):
        self.conn = sqlite3.connect(self.baseDatos)
        self.cursor = self.conn.cursor()
        # return self.conn,self.cursor
    def cargarTodo(self,tabla):
        sql="SELECT * FROM "+ str(tabla)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows
    def buscarDatosLike(self,tabla,campos,valorCampos):
        sql="SELECT * FROM " +str(tabla) + " WHERE "+str(campos[0])+" LIKE'%"+str(valorCampos[0])+"%'"
        if (len(campos) > 1):
            for index in range(len(campos)-1):
                sql += " OR "+ str(campos[index+1])+ " LIKE'%" + str(valorCampos[index+1])+"%'"
        print(sql)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows
# select * from productos where codigo like'%fria%' OR nombre like  '%fria%'

    def cargarDatosValorCampo(self,tabla,camposSelect):
        sql= "SELECT "+ str(camposSelect[0])
        sql2= " FROM "+str(tabla)+" WHERE activo = 1"
        if (len(camposSelect) > 1):
            for index in range(len(camposSelect)-1):
                sql += ", "+ str(camposSelect[index+1])

        sql+=sql2
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows


    def borrarValorCampo(self,tabla,id):
        sql="UPDATE "+ str(tabla) + " SET activo=0 WHERE _rowid_=?"
        self.cursor.execute(sql, [ (id) ] )
        self.conn.commit()

    def actualizarValorCampo(self,tabla,campos,valorCampos):
        sql="UPDATE "+ str(tabla)+ " SET "+ str(campos[0])+"=?"
        sql2= " WHERE _rowid_=?"
        if (len(campos) > 1): # EL ÚLTIMO VALOR CAMPO ES EL ID SIEMPRE...
            for index in range(len(campos)-1):
                sql+=", "+str(campos[index+1])+"=?"
        sql+=sql2
        print(sql)
        self.cursor.execute(sql,valorCampos)
        self.conn.commit()



    def generarValorCampoConId(self,tabla,camposSelect,camposWhere,tipoCampoWhere,id):
        sql="SELECT "+str(camposSelect[0])
        sql2= " FROM " + str(tabla) + " where "
        sql3=str(camposWhere[0])+"="+str(self.identificaValor(tipoCampoWhere[0]))
        if (len(camposWhere) > 1):
            for index in range(len(camposWhere)-1):
                sql3 += " and "+str(camposWhere[index+1])+"="+str(self.identificaValor(tipoCampoWhere[index+1]))
        if (len(camposSelect) > 1):
            for index in range(len(camposSelect)-1):
                sql += ", "+ str(camposSelect[index+1])
        sql+=sql2+sql3
        print(sql)
        self.cursor.execute(sql, [id])
        datosUsuario=self.cursor.fetchone()
        return datosUsuario

    def crearValorCampo(self,tabla,campos,valorCampos):
        sql= "INSERT INTO " + str(tabla) + "("
        sql2= str(campos[0])
        sql3= " VALUES (?"
        if (len(campos) > 1):
            for index in range(len(campos)-1):
                sql2 += ","+str(campos[index+1])
                sql3 += ",?"
        sql2 += ")"
        sql3 += ")"
        sql+= sql2+sql3
        print(sql)
        self.cursor.execute(sql, valorCampos)
        self.conn.commit()
        id = self.cursor.lastrowid
        return id

    def buscarValorCamposGeneral(self,tabla,camposSelect,camposWhere,tipoCamposWhere,valorCamposWhere):
        id=None
        sql="SELECT "+str(camposSelect[0])
        sql2=" FROM " + str(tabla) + " where "

        sql3 = str(camposWhere[0])+"="+str(self.identificaValor(tipoCamposWhere[0]))
        if (len(camposWhere) > 1):
            for index in range(len(camposWhere)-1):
                sql3 += " and "+ str(camposWhere[index+1])+"="+str(self.identificaValor(tipoCamposWhere[index+1]))
        if (len(camposSelect) > 1):
            for index in range(len(camposSelect)-1):
                sql += ", "+ str(camposSelect[index+1])
        sql+=sql2+sql3
        # sql+=sql2
        print(sql)

        self.cursor.execute(sql, valorCamposWhere)
        row=self.cursor.fetchone()
        print(row)
        return row


    def buscarValorCampo(self,tabla,campos,tipoCampos,valorCampos):
        id=None
        sql="SELECT id FROM " + str(tabla) + " where "

        sql2 = str(campos[0])+"="+str(self.identificaValor(tipoCampos[0]))
        if (len(campos) > 1):
            for index in range(len(campos)-1):
                sql2 += " and "+ str(campos[index+1])+"="+str(self.identificaValor(tipoCampos[index+1]))
        sql+=sql2
        print(sql)
        print(campos)
        print(valorCampos)
        self.cursor.execute(sql, valorCampos)
        id=self.cursor.fetchone()
        return id

    def identificaValor(self,valorCampo):
        if (int(valorCampo) == 1):
            return valorCampo
        elif (int(valorCampo) == -1):
            return "?"
        elif (int(valorCampo)== 0):
            return valorCampo
        else:
            print("Valor de Campo con formato NO compatible: "+ str(valorCampo))


#
# #
# # ejemplo1=["admin","perro","chepe"]
# campos=["nombre","admin","perro","chepe"]
# #
# # ejemplo2=["nombre"]
# # valorEj2=[-1,0,5]
# bd=BaseDatos("basedatos.db")
# bd.buscarDatosLike("productos",["codigo","id_categoria"],["h","1"])
# # bd.generarValorCampoConId("usuarios",["nombre"],["id"],[-1])
# # bd.buscarValorCampo("usuarios",ejemplo2,valorEj2,"pedo")
# # print("------------------------------------------")
# bd.actualizarValorCampo("usuarios",campos,"caca")
