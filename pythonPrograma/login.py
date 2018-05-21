# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from principal import *
import sqlite3

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(294, 134)
        Dialog.setMinimumSize(QtCore.QSize(294, 134))
        Dialog.setMaximumSize(QtCore.QSize(294, 134))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 84))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nombreUsuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nombreUsuario.setInputMask("")
        self.nombreUsuario.setObjectName("nombreUsuario")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nombreUsuario)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.contrasena = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.contrasena.setInputMask("")
        self.contrasena.setText("")
        self.contrasena.setMaxLength(32767)
        self.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasena.setObjectName("contrasena")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.contrasena)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.ingresar)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Iniciar"))
        self.label.setText(_translate("Dialog", "Nombre de usuario:"))
        self.label_2.setText(_translate("Dialog", "Contraseña:"))

    def ingresar(self):
        conn = sqlite3.connect("basedatos.db")
        cursor = conn.cursor()

        sql = "SELECT count(id) FROM usuarios where nombre=? and contrasena=? and activo=1"
        cursor.execute(sql, [(self.nombreUsuario.text()),(self.contrasena.text())])

        if cursor.fetchone()[0] == 1:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            Dialog.close()
        else:
            self.label_3.setText("Nombre o contraseña errada")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
