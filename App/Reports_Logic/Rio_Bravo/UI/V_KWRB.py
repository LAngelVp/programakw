#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Kenworth Del Rio Bravo")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("")
        self.WPrincipal = QtWidgets.QWidget(MainWindow)
        self.WPrincipal.setMinimumSize(QtCore.QSize(800, 500))
        self.WPrincipal.setMaximumSize(QtCore.QSize(800, 500))
        self.WPrincipal.setStyleSheet("#WPrincipal{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#btnSubir{\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius:8px;\n"
"}\n"
"#btnSubir::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btnEliminar{\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius:8px;\n"
"}\n"
"#btnEliminar::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btnComenzar{\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius:8px;\n"
"}\n"
"#btnComenzar::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btn_Procesados{\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"#btn_Procesados::hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btn_Originales{\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"#btn_Originales::hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btn_Errores{\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"#btn_Errores::hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btnAyuda{\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius:5px;\n"
"}\n"
"#btnAyuda::hover{\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"#btnMinimizar{\n"
"background-color: transparent;\n"
"}\n"
"#btnCerrar{\n"
"background-color: transparent;\n"
"}")
        self.WPrincipal.setObjectName("WPrincipal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.WPrincipal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WCabecera = QtWidgets.QWidget(self.WPrincipal)
        self.WCabecera.setMinimumSize(QtCore.QSize(0, 50))
        self.WCabecera.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WCabecera.setObjectName("WCabecera")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.WCabecera)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.WLogo = QtWidgets.QWidget(self.WCabecera)
        self.WLogo.setMinimumSize(QtCore.QSize(200, 0))
        self.WLogo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.WLogo.setObjectName("WLogo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.WLogo)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblLogoKWRB = QtWidgets.QLabel(self.WLogo)
        self.lblLogoKWRB.setText("")
        self.lblLogoKWRB.setPixmap(QtGui.QPixmap("../Source/LOGO_KWRB.png"))
        self.lblLogoKWRB.setScaledContents(True)
        self.lblLogoKWRB.setObjectName("lblLogoKWRB")
        self.verticalLayout_2.addWidget(self.lblLogoKWRB)
        self.horizontalLayout.addWidget(self.WLogo)
        spacerItem = QtWidgets.QSpacerItem(476, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.WBotonesSalida = QtWidgets.QWidget(self.WCabecera)
        self.WBotonesSalida.setMinimumSize(QtCore.QSize(110, 0))
        self.WBotonesSalida.setMaximumSize(QtCore.QSize(110, 16777215))
        self.WBotonesSalida.setObjectName("WBotonesSalida")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.WBotonesSalida)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMinimizar = QtWidgets.QPushButton(self.WBotonesSalida)
        self.btnMinimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Source/Icon_Minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimizar.setIcon(icon)
        self.btnMinimizar.setIconSize(QtCore.QSize(30, 30))
        self.btnMinimizar.setObjectName("btnMinimizar")
        self.horizontalLayout_2.addWidget(self.btnMinimizar)
        self.btnCerrar = QtWidgets.QPushButton(self.WBotonesSalida)
        self.btnCerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrar.setMouseTracking(False)
        self.btnCerrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Source/Icon_Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setIconSize(QtCore.QSize(30, 30))
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout_2.addWidget(self.btnCerrar)
        self.horizontalLayout.addWidget(self.WBotonesSalida)
        self.verticalLayout.addWidget(self.WCabecera)
        self.WCuerpo = QtWidgets.QWidget(self.WPrincipal)
        self.WCuerpo.setMinimumSize(QtCore.QSize(0, 280))
        self.WCuerpo.setMaximumSize(QtCore.QSize(16777215, 280))
        self.WCuerpo.setObjectName("WCuerpo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WCuerpo)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.WTablaIzquierda = QtWidgets.QWidget(self.WCuerpo)
        self.WTablaIzquierda.setObjectName("WTablaIzquierda")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.WTablaIzquierda)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTextoEnCola = QtWidgets.QLabel(self.WTablaIzquierda)
        self.lblTextoEnCola.setMinimumSize(QtCore.QSize(0, 20))
        self.lblTextoEnCola.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTextoEnCola.setFont(font)
        self.lblTextoEnCola.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTextoEnCola.setObjectName("lblTextoEnCola")
        self.verticalLayout_3.addWidget(self.lblTextoEnCola)
        self.TWCola = QtWidgets.QTableWidget(self.WTablaIzquierda)
        self.TWCola.setObjectName("TWCola")
        self.TWCola.setColumnCount(0)
        self.TWCola.setRowCount(0)
        self.verticalLayout_3.addWidget(self.TWCola)
        self.horizontalLayout_3.addWidget(self.WTablaIzquierda)
        self.WTablaDerecha = QtWidgets.QWidget(self.WCuerpo)
        self.WTablaDerecha.setObjectName("WTablaDerecha")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.WTablaDerecha)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblTextoProcesado = QtWidgets.QLabel(self.WTablaDerecha)
        self.lblTextoProcesado.setMinimumSize(QtCore.QSize(0, 20))
        self.lblTextoProcesado.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTextoProcesado.setFont(font)
        self.lblTextoProcesado.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTextoProcesado.setObjectName("lblTextoProcesado")
        self.verticalLayout_4.addWidget(self.lblTextoProcesado)
        self.TWProcesado = QtWidgets.QTableWidget(self.WTablaDerecha)
        self.TWProcesado.setObjectName("TWProcesado")
        self.TWProcesado.setColumnCount(0)
        self.TWProcesado.setRowCount(0)
        self.verticalLayout_4.addWidget(self.TWProcesado)
        self.horizontalLayout_3.addWidget(self.WTablaDerecha)
        self.verticalLayout.addWidget(self.WCuerpo)
        self.WPie = QtWidgets.QWidget(self.WPrincipal)
        self.WPie.setMinimumSize(QtCore.QSize(0, 100))
        self.WPie.setMaximumSize(QtCore.QSize(16777215, 100))
        self.WPie.setObjectName("WPie")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.WPie)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.WBotones = QtWidgets.QWidget(self.WPie)
        self.WBotones.setMinimumSize(QtCore.QSize(450, 0))
        self.WBotones.setObjectName("WBotones")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.WBotones)
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.WBotonesTrabajo = QtWidgets.QWidget(self.WBotones)
        self.WBotonesTrabajo.setMinimumSize(QtCore.QSize(0, 50))
        self.WBotonesTrabajo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.WBotonesTrabajo.setObjectName("WBotonesTrabajo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.WBotonesTrabajo)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSubir = QtWidgets.QPushButton(self.WBotonesTrabajo)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSubir.setFont(font)
        self.btnSubir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubir.setStyleSheet("")
        self.btnSubir.setObjectName("btnSubir")
        self.horizontalLayout_5.addWidget(self.btnSubir)
        self.btnEliminar = QtWidgets.QPushButton(self.WBotonesTrabajo)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminar.setStyleSheet("")
        self.btnEliminar.setObjectName("btnEliminar")
        self.horizontalLayout_5.addWidget(self.btnEliminar)
        self.btnComenzar = QtWidgets.QPushButton(self.WBotonesTrabajo)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnComenzar.setFont(font)
        self.btnComenzar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnComenzar.setStyleSheet("")
        self.btnComenzar.setObjectName("btnComenzar")
        self.horizontalLayout_5.addWidget(self.btnComenzar)
        self.verticalLayout_6.addWidget(self.WBotonesTrabajo)
        self.WBotonesRutas = QtWidgets.QWidget(self.WBotones)
        self.WBotonesRutas.setObjectName("WBotonesRutas")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.WBotonesRutas)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_Procesados = QtWidgets.QPushButton(self.WBotonesRutas)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Procesados.setFont(font)
        self.btn_Procesados.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Procesados.setStyleSheet("")
        self.btn_Procesados.setObjectName("btn_Procesados")
        self.horizontalLayout_6.addWidget(self.btn_Procesados)
        self.btn_Originales = QtWidgets.QPushButton(self.WBotonesRutas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Originales.setFont(font)
        self.btn_Originales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Originales.setStyleSheet("")
        self.btn_Originales.setObjectName("btn_Originales")
        self.horizontalLayout_6.addWidget(self.btn_Originales)
        self.btn_Errores = QtWidgets.QPushButton(self.WBotonesRutas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Errores.setFont(font)
        self.btn_Errores.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Errores.setStyleSheet("")
        self.btn_Errores.setObjectName("btn_Errores")
        self.horizontalLayout_6.addWidget(self.btn_Errores)
        self.verticalLayout_6.addWidget(self.WBotonesRutas)
        self.horizontalLayout_4.addWidget(self.WBotones)
        self.WTextoProceso = QtWidgets.QWidget(self.WPie)
        self.WTextoProceso.setObjectName("WTextoProceso")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.WTextoProceso)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_TrabajandoCon = QtWidgets.QLabel(self.WTextoProceso)
        self.lbl_TrabajandoCon.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_TrabajandoCon.setFont(font)
        self.lbl_TrabajandoCon.setText("")
        self.lbl_TrabajandoCon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_TrabajandoCon.setObjectName("lbl_TrabajandoCon")
        self.verticalLayout_5.addWidget(self.lbl_TrabajandoCon)
        self.lbl_NombreReporte = QtWidgets.QLabel(self.WTextoProceso)
        self.lbl_NombreReporte.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_NombreReporte.setFont(font)
        self.lbl_NombreReporte.setText("")
        self.lbl_NombreReporte.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_NombreReporte.setObjectName("lbl_NombreReporte")
        self.verticalLayout_5.addWidget(self.lbl_NombreReporte)
        self.horizontalLayout_4.addWidget(self.WTextoProceso)
        self.WBotonAyuda = QtWidgets.QWidget(self.WPie)
        self.WBotonAyuda.setMinimumSize(QtCore.QSize(60, 0))
        self.WBotonAyuda.setMaximumSize(QtCore.QSize(60, 60))
        self.WBotonAyuda.setObjectName("WBotonAyuda")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.WBotonAyuda)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnAyuda = QtWidgets.QPushButton(self.WBotonAyuda)
        self.btnAyuda.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAyuda.setFont(font)
        self.btnAyuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAyuda.setAcceptDrops(False)
        self.btnAyuda.setToolTip("<html><head/><body><p align=\"justify\">Ayuda</p></body></html>")
        self.btnAyuda.setToolTipDuration(0)
        self.btnAyuda.setStatusTip("")
        self.btnAyuda.setWhatsThis("")
        self.btnAyuda.setAccessibleName("")
        self.btnAyuda.setAccessibleDescription("")
        self.btnAyuda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAyuda.setAutoFillBackground(False)
        self.btnAyuda.setStyleSheet("")
        self.btnAyuda.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Nicaragua))
        self.btnAyuda.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Source/Icon_Help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAyuda.setIcon(icon2)
        self.btnAyuda.setIconSize(QtCore.QSize(32, 32))
        self.btnAyuda.setObjectName("btnAyuda")
        self.verticalLayout_7.addWidget(self.btnAyuda)
        self.horizontalLayout_4.addWidget(self.WBotonAyuda)
        self.verticalLayout.addWidget(self.WPie)
        MainWindow.setCentralWidget(self.WPrincipal)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuOPCIONES = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.menuOPCIONES.setFont(font)
        self.menuOPCIONES.setObjectName("menuOPCIONES")
        self.menuPagosClientes = QtWidgets.QMenu(self.menuOPCIONES)
        self.menuPagosClientes.setObjectName("menuPagosClientes")
        MainWindow.setMenuBar(self.menuBar)
        self.Pagos_Clientes_Objetivos = QtWidgets.QAction(MainWindow)
        self.Pagos_Clientes_Objetivos.setObjectName("Pagos_Clientes_Objetivos")
        self.actionObjetivos_Mensuales = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionObjetivos_Mensuales.setFont(font)
        self.actionObjetivos_Mensuales.setObjectName("actionObjetivos_Mensuales")
        self.actionFechaMovimiento = QtWidgets.QAction(MainWindow)
        self.actionFechaMovimiento.setObjectName("actionFechaMovimiento")
        self.menuPagosClientes.addAction(self.actionObjetivos_Mensuales)
        self.menuOPCIONES.addAction(self.menuPagosClientes.menuAction())
        self.menuOPCIONES.addAction(self.actionFechaMovimiento)
        self.menuBar.addAction(self.menuOPCIONES.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Kenworth Del Rio Bravo", "Kenworth Del Rio Bravo"))
        self.btnMinimizar.setToolTip(_translate("Kenworth Del Rio Bravo", "Minimizar"))
        self.btnCerrar.setToolTip(_translate("Kenworth Del Rio Bravo", "Cerrar"))
        self.lblTextoEnCola.setText(_translate("Kenworth Del Rio Bravo", "Trabajos En Espera"))
        self.lblTextoProcesado.setText(_translate("Kenworth Del Rio Bravo", "Trabajos Realizados"))
        self.btnSubir.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Selecciona un archivo .xlsx</p></body></html>"))
        self.btnSubir.setText(_translate("Kenworth Del Rio Bravo", "Subir"))
        self.btnEliminar.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Elimina los archivos procesados</p></body></html>"))
        self.btnEliminar.setText(_translate("Kenworth Del Rio Bravo", "Eliminar"))
        self.btnComenzar.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Comenzar el proceso</p></body></html>"))
        self.btnComenzar.setText(_translate("Kenworth Del Rio Bravo", "Comenzar"))
        self.btn_Procesados.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Ruta de archivos procesados</p></body></html>"))
        self.btn_Procesados.setText(_translate("Kenworth Del Rio Bravo", "Procesados"))
        self.btn_Originales.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Ruta de archivos originales</p></body></html>"))
        self.btn_Originales.setText(_translate("Kenworth Del Rio Bravo", "Originales"))
        self.btn_Errores.setToolTip(_translate("Kenworth Del Rio Bravo", "<html><head/><body><p>Ruta de archivos erroneos</p></body></html>"))
        self.btn_Errores.setText(_translate("Kenworth Del Rio Bravo", "Erroneos"))
        self.menuOPCIONES.setTitle(_translate("Kenworth Del Rio Bravo", "OPCIONES"))
        self.menuPagosClientes.setTitle(_translate("Kenworth Del Rio Bravo", "PagosClientes"))
        self.Pagos_Clientes_Objetivos.setText(_translate("Kenworth Del Rio Bravo", "Pagos_Clientes(Objetivos)"))
        self.actionObjetivos_Mensuales.setText(_translate("Kenworth Del Rio Bravo", "Objetivos Mensuales"))
        self.actionFechaMovimiento.setText(_translate("Kenworth Del Rio Bravo", "FechaMovimiento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
