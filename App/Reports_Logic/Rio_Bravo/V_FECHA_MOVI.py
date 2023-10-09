
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Logica_Reportes.Variables.FechaMovimiento import *
import datetime


class Ui_Formulario_FechaMovimiento(object):
    def setupUi(self, Formulario_FechaMovimiento):
        Formulario_FechaMovimiento.setObjectName("Formulario_FechaMovimiento")
        Formulario_FechaMovimiento.resize(160, 140)
        Formulario_FechaMovimiento.setMinimumSize(QtCore.QSize(160, 140))
        Formulario_FechaMovimiento.setMaximumSize(QtCore.QSize(160, 140))
        self.gridLayout = QtWidgets.QGridLayout(Formulario_FechaMovimiento)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.W_Principal = QtWidgets.QWidget(Formulario_FechaMovimiento)
        self.W_Principal.setObjectName("W_Principal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.W_Principal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_FechaMovimiento = QtWidgets.QLabel(self.W_Principal)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_FechaMovimiento.setFont(font)
        self.lbl_FechaMovimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_FechaMovimiento.setObjectName("lbl_FechaMovimiento")
        self.verticalLayout.addWidget(self.lbl_FechaMovimiento)
        self.W_FechaMovimiento = QtWidgets.QWidget(self.W_Principal)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.W_FechaMovimiento.setFont(font)
        self.W_FechaMovimiento.setObjectName("W_FechaMovimiento")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.W_FechaMovimiento)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.date_edit_Movimiento = QtWidgets.QDateEdit(self.W_FechaMovimiento)
        self.date_edit_Movimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.date_edit_Movimiento.setCalendarPopup(True)
        self.date_edit_Movimiento.setDate(QtCore.QDate(2023, 1, 1))
        self.date_edit_Movimiento.setObjectName("date_edit_Movimiento")
        self.verticalLayout_2.addWidget(self.date_edit_Movimiento)
        self.verticalLayout.addWidget(self.W_FechaMovimiento)
        self.W_btn_Aceptar = QtWidgets.QWidget(self.W_Principal)
        self.W_btn_Aceptar.setObjectName("W_btn_Aceptar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.W_btn_Aceptar)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_aceptarMovimiento = QtWidgets.QPushButton(self.W_btn_Aceptar)
        self.btn_aceptarMovimiento.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_aceptarMovimiento.setFont(font)
        self.btn_aceptarMovimiento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_aceptarMovimiento.setObjectName("btn_aceptarMovimiento")
        self.verticalLayout_3.addWidget(self.btn_aceptarMovimiento)
        self.verticalLayout.addWidget(self.W_btn_Aceptar)
        self.gridLayout.addWidget(self.W_Principal, 1, 0, 1, 1)

        self.retranslateUi(Formulario_FechaMovimiento)
        QtCore.QMetaObject.connectSlotsByName(Formulario_FechaMovimiento)

    def retranslateUi(self, Formulario_FechaMovimiento):
        _translate = QtCore.QCoreApplication.translate
        Formulario_FechaMovimiento.setWindowTitle(_translate("Formulario_FechaMovimiento", "Formulario"))
        self.lbl_FechaMovimiento.setText(_translate("Formulario_FechaMovimiento", "Fecha Movimiento"))
        self.btn_aceptarMovimiento.setText(_translate("Formulario_FechaMovimiento", "Aceptar"))

class FechaMovimiento(QWidget):
    def __init__(self):
        super(FechaMovimiento, self).__init__()
        self.ui = Ui_Formulario_FechaMovimiento()
        self.ui.setupUi(self)
        self.ui.btn_aceptarMovimiento.clicked.connect(self.guardarFechaMovimiento)

        fecha_actual = datetime.date.today()
        self.ui.date_edit_Movimiento.setDate(fecha_actual)

        # Crear una instancia de la clase ContenedorVariable con la fecha actual
        self.contenedor = ContenedorVariable(fecha_actual)

    def guardarFechaMovimiento(self):
        nueva_fecha = self.ui.date_edit_Movimiento.date().toPyDate()
        clase_asignadora = ClaseParaAsignarFechaMovimiento()  # Reemplaza por tu clase adecuada
        clase_asignadora.asignacion_fecha_movimiento_hacia_contenedor(self.contenedor, nueva_fecha)

        # Mostrar la fecha inicial
        clase_mostradora = ClaseMostradora()  # Reemplaza por tu clase adecuada
        print("Fecha Inicial:")
        clase_mostradora.mostrar_fecha_desde_contenedor(self.contenedor)

        # Mostrar la fecha modificada
        print("\nFecha Modificada:")
        clase_mostradora.mostrar_fecha_desde_contenedor(self.contenedor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FechaMovimiento()
    window.show()
    sys.exit(app.exec_())
