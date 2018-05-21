# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modoAdmin_3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# from PyQt5.QtCore import Qt
import sqlite3

class Ui_Form(object):

    def crearUsuario(self):
        print("crearUsuario")

        conn = sqlite3.connect("basedatos.db")
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios(nombre,contrasena) VALUES (?,?)"
        cursor.execute(sql,
            [
                (self.lineEdit.text()),
                (self.lineEdit_2.text()),
            ]
        )
        conn.commit()

        idUsuario = cursor.lastrowid
        print(idUsuario)

        filasTabla = self.tableWidget.rowCount()

        boton = QtWidgets.QPushButton()
        boton.setText('Borrar')
        boton.clicked.connect(self.borrarUsuario)

        id = QtWidgets.QTableWidgetItem(str(idUsuario))
        id.setFlags(id.flags()  & ~Qt.ItemIsEditable)

        self.tableWidget.blockSignals(True)

        self.tableWidget.insertRow( filasTabla )
        self.tableWidget.setItem( filasTabla, 0, QtWidgets.QTableWidgetItem(id))
        self.tableWidget.setItem( filasTabla, 1, QtWidgets.QTableWidgetItem(self.lineEdit.text()))
        self.tableWidget.setItem( filasTabla, 2, QtWidgets.QTableWidgetItem(self.lineEdit_2.text()))
        self.tableWidget.setCellWidget( filasTabla, 3, boton)

        self.tableWidget.blockSignals(False)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        print("termina")


    def actualizarUsuario(self, fila):
        print("actualizarUsuario")
        id = self.tableWidget.item(fila,0).text()
        nombre = self.tableWidget.item(fila,1).text()
        contrasena= self.tableWidget.item(fila,2).text()

        conn = sqlite3.connect("basedatos.db")
        cursor = conn.cursor()
        sql = "UPDATE usuarios SET nombre=?, contrasena=? WHERE _rowid_=?"
        cursor.execute(sql,
            [
                (nombre),
                (contrasena),
                (id)
            ]
        )
        conn.commit()

    def borrarUsuario(self):
        print("borrarUsuario")
        ArregloBotonClicked=QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(ArregloBotonClicked.pos())
        if index.isValid():
            id = self.tableWidget.item(index.row(),0).text()

            conn = sqlite3.connect("basedatos.db")
            cursor = conn.cursor()
            sql = "UPDATE usuarios SET activo=0 WHERE _rowid_=?"
            cursor.execute(sql, [ (id) ] )
            conn.commit()
            self.tableWidget.removeRow(index.row())


    def cargarDatos(self):
        print("cargarDatos")
        self.arregloBotones=[]

        conn = sqlite3.connect("basedatos.db")
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, contrasena FROM usuarios WHERE activo = 1')
        self.tableWidget.setRowCount(0)
        rows = cursor.fetchall()

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


    def setupUi(self, Form):
        print("setupUi")
        Form.setObjectName("Form")
        Form.resize(450, 534)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(450, 0))
        Form.setMaximumSize(QtCore.QSize(450, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        self.tableWidget.cellChanged['int','int'].connect(self.actualizarUsuario)
        self.pushButton.clicked.connect(self.crearUsuario)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        print("retranslateUi")
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modo Administrador"))
        self.label.setText(_translate("Form", "Nombre"))
        self.label_2.setText(_translate("Form", "Contraseña"))
        self.pushButton.setText(_translate("Form", "Crear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Usuario"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Contraseña"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Opciones"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.tableWidget.blockSignals(True)
    ui.cargarDatos()
    ui.tableWidget.blockSignals(False)
    Form.show()
    sys.exit(app.exec_())
