#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Ui_Formulario(object):
    def setupUi(self, Formulario):
        Formulario.setObjectName("Formulario")
        Formulario.resize(156, 60)
        Formulario.setMinimumSize(QtCore.QSize(0, 60))
        Formulario.setMaximumSize(QtCore.QSize(16777215, 60))
        self.gridLayout = QtWidgets.QGridLayout(Formulario)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Formulario)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.date_edit_fechamovimiento = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.date_edit_fechamovimiento.setFont(font)
        self.date_edit_fechamovimiento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_edit_fechamovimiento.setWrapping(False)
        self.date_edit_fechamovimiento.setFrame(False)
        self.date_edit_fechamovimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.date_edit_fechamovimiento.setReadOnly(False)
        self.date_edit_fechamovimiento.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.date_edit_fechamovimiento.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date_edit_fechamovimiento.setCalendarPopup(True)
        self.date_edit_fechamovimiento.setDate(QtCore.QDate(2023, 1, 1))
        self.date_edit_fechamovimiento.setObjectName("date_edit_fechamovimiento")
        self.verticalLayout.addWidget(self.date_edit_fechamovimiento)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Formulario)
        QtCore.QMetaObject.connectSlotsByName(Formulario)

    def retranslateUi(self, Formulario):
        _translate = QtCore.QCoreApplication.translate
        Formulario.setWindowTitle(_translate("Formulario", "Formulario"))



class FechaMovimiento(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario()
        self.ui.setupUi(self)

        self.ui.btn_aceptar.clicked.connect(self.cambiar_fecha)
        self.fecha_movimiento = QDate.currentDate()
    @property
    def fecha_movimiento(self):
        return self.ui.date_edit.date()
    
    @fecha_movimiento.setter
    def fecha_movimiento(self, fecha_nueva):
        self.ui.date_edit.setDate(fecha_nueva)

    def cambiar_fecha(self):
        # Puedes usar self.fecha_movimiento para obtener la fecha actual
        fecha_actual = self.fecha_movimiento
        # Hacer algo con la fecha actual (por ejemplo, mostrarla en un QLabel)
        self.ui.lbl_mostrar.setText(fecha_actual.toString("dd-MM-yyyy"))

if __name__ == '__main__':
    app = QApplication (sys.argv)
    Ventana = FechaMovimiento()
    Ventana.show()
    sys.exit(app.exec_())