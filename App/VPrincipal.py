# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VPrincipal(object):
    def setupUi(self, VPrincipal):
        VPrincipal.setObjectName("VPrincipal")
        VPrincipal.setEnabled(True)
        VPrincipal.resize(350, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VPrincipal.sizePolicy().hasHeightForWidth())
        VPrincipal.setSizePolicy(sizePolicy)
        VPrincipal.setMinimumSize(QtCore.QSize(350, 450))
        VPrincipal.setMaximumSize(QtCore.QSize(350, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Source/KWE.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VPrincipal.setWindowIcon(icon)
        VPrincipal.setLayoutDirection(QtCore.Qt.LeftToRight)
        VPrincipal.setAutoFillBackground(False)
        VPrincipal.setStyleSheet("[objectName^=\"btc_btc\"]{\n"
"background-color: transparent;\n"
"}\n"
"[objectName^=\"btc_btc\"]:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:4px;\n"
"}\n"
"[objectName^=\"btn_btn\"]{\n"
"background-color: rgb(232, 232, 232);\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"max-height: 35px;\n"
"max-width: 280px;\n"
"}\n"
"[objectName^=\"btn_btn\"]:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#panel_encabezado{\n"
"min-height: 35px;    \n"
"max-height: 35px;\n"
"}\n"
"#panel_img_logo{\n"
"min-height: 120px;\n"
"    max-height: 120px;\n"
"}\n"
"#panel_btn_sucursales{\n"
"margin-top:10px;\n"
"min-height: 200px;\n"
"    max-height: 300px;\n"
"}\n"
"#imgPrincipalMenu{\n"
"    margin-left: 25px;\n"
"    margin-right: 25px;\n"
"}\n"
"#VPrincipal{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#imgPrincipalMenu{\n"
"border-radius:8px;\n"
"}")
        VPrincipal.setIconSize(QtCore.QSize(45, 45))
        VPrincipal.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(VPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.panel_img_logo = QtWidgets.QWidget(self.centralwidget)
        self.panel_img_logo.setObjectName("panel_img_logo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.panel_img_logo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgPrincipalMenu = QtWidgets.QLabel(self.panel_img_logo)
        self.imgPrincipalMenu.setStyleSheet("")
        self.imgPrincipalMenu.setText("")
        self.imgPrincipalMenu.setScaledContents(True)
        self.imgPrincipalMenu.setAlignment(QtCore.Qt.AlignCenter)
        self.imgPrincipalMenu.setObjectName("imgPrincipalMenu")
        self.horizontalLayout.addWidget(self.imgPrincipalMenu)
        self.gridLayout_2.addWidget(self.panel_img_logo, 1, 0, 1, 1)
        self.panel_btn_sucursales = QtWidgets.QWidget(self.centralwidget)
        self.panel_btn_sucursales.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.panel_btn_sucursales.setObjectName("panel_btn_sucursales")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.panel_btn_sucursales)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_btn_kweste = QtWidgets.QPushButton(self.panel_btn_sucursales)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_btn_kweste.setFont(font)
        self.btn_btn_kweste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_kweste.setStyleSheet("")
        self.btn_btn_kweste.setObjectName("btn_btn_kweste")
        self.gridLayout_3.addWidget(self.btn_btn_kweste, 1, 0, 1, 1)
        self.btn_btn_kwsonora = QtWidgets.QPushButton(self.panel_btn_sucursales)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_btn_kwsonora.setFont(font)
        self.btn_btn_kwsonora.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_kwsonora.setStyleSheet("")
        self.btn_btn_kwsonora.setObjectName("btn_btn_kwsonora")
        self.gridLayout_3.addWidget(self.btn_btn_kwsonora, 3, 0, 1, 1)
        self.btn_btn_kwkrei = QtWidgets.QPushButton(self.panel_btn_sucursales)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_btn_kwkrei.setFont(font)
        self.btn_btn_kwkrei.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_kwkrei.setStyleSheet("")
        self.btn_btn_kwkrei.setObjectName("btn_btn_kwkrei")
        self.gridLayout_3.addWidget(self.btn_btn_kwkrei, 2, 0, 1, 1)
        self.btn_btn_kwrb = QtWidgets.QPushButton(self.panel_btn_sucursales)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_btn_kwrb.setFont(font)
        self.btn_btn_kwrb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_kwrb.setStyleSheet("")
        self.btn_btn_kwrb.setObjectName("btn_btn_kwrb")
        self.gridLayout_3.addWidget(self.btn_btn_kwrb, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.panel_btn_sucursales, 2, 0, 1, 1)
        self.panel_encabezado = QtWidgets.QWidget(self.centralwidget)
        self.panel_encabezado.setObjectName("panel_encabezado")
        self.gridLayout = QtWidgets.QGridLayout(self.panel_encabezado)
        self.gridLayout.setContentsMargins(0, 0, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(310, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.btc_btc_rutas = QtWidgets.QPushButton(self.panel_encabezado)
        self.btc_btc_rutas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btc_btc_rutas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../Downloads/rutas.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btc_btc_rutas.setIcon(icon1)
        self.btc_btc_rutas.setIconSize(QtCore.QSize(20, 20))
        self.btc_btc_rutas.setObjectName("btc_btc_rutas")
        self.gridLayout.addWidget(self.btc_btc_rutas, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.panel_encabezado, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        VPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VPrincipal)
        self.btn_btn_kwrb.clicked.connect(VPrincipal.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(VPrincipal)

    def retranslateUi(self, VPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VPrincipal.setWindowTitle(_translate("VPrincipal", "CONCESIONARIOS"))
        self.btn_btn_kweste.setText(_translate("VPrincipal", "KENWORTH DEL ESTE"))
        self.btn_btn_kwsonora.setText(_translate("VPrincipal", "KENWORTH SONORA"))
        self.btn_btn_kwkrei.setText(_translate("VPrincipal", "KENWORTH KREI"))
        self.btn_btn_kwrb.setText(_translate("VPrincipal", "KENWORTH RIO BRAVO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VPrincipal = QtWidgets.QMainWindow()
    ui = Ui_VPrincipal()
    ui.setupUi(VPrincipal)
    VPrincipal.show()
    sys.exit(app.exec_())
