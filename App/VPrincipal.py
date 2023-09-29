#########################
# DESARROLLADOR
# LUIS ANGEL VALLEJO PEREZ
#########################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VPrincipal(object):
    def setupUi(self, VPrincipal):
        VPrincipal.setObjectName("VPrincipal")
        VPrincipal.setEnabled(True)
        VPrincipal.resize(350, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VPrincipal.sizePolicy().hasHeightForWidth())
        VPrincipal.setSizePolicy(sizePolicy)
        VPrincipal.setMinimumSize(QtCore.QSize(350, 400))
        VPrincipal.setMaximumSize(QtCore.QSize(350, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Source/KWE.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VPrincipal.setWindowIcon(icon)
        VPrincipal.setLayoutDirection(QtCore.Qt.LeftToRight)
        VPrincipal.setAutoFillBackground(False)
        VPrincipal.setStyleSheet("#VPrincipal{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#imgPrincipalMenu{\n"
"border-radius:8px;\n"
"}\n"
"#btnKWRB{\n"
"background-color: rgb(232, 232, 232);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"#btnKWRB::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#btnKWESTE{\n"
"background-color: rgb(232, 232, 232);\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"#btnKWESTE::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#btnKWKREI{\n"
"background-color: rgb(232, 232, 232);\n"
"    border-radius:8px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"#btnKWKREI::Hover{\n"
"background-color: rgb(209, 209, 209);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        VPrincipal.setIconSize(QtCore.QSize(45, 45))
        VPrincipal.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(VPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnKWRB = QtWidgets.QPushButton(self.centralwidget)
        self.btnKWRB.setGeometry(QtCore.QRect(40, 200, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnKWRB.setFont(font)
        self.btnKWRB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKWRB.setStyleSheet("")
        self.btnKWRB.setObjectName("btnKWRB")
        self.btnKWESTE = QtWidgets.QPushButton(self.centralwidget)
        self.btnKWESTE.setGeometry(QtCore.QRect(40, 260, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnKWESTE.setFont(font)
        self.btnKWESTE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKWESTE.setStyleSheet("")
        self.btnKWESTE.setObjectName("btnKWESTE")
        self.btnKWKREI = QtWidgets.QPushButton(self.centralwidget)
        self.btnKWKREI.setGeometry(QtCore.QRect(40, 320, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnKWKREI.setFont(font)
        self.btnKWKREI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKWKREI.setStyleSheet("")
        self.btnKWKREI.setObjectName("btnKWKREI")
        self.imgPrincipalMenu = QtWidgets.QLabel(self.centralwidget)
        self.imgPrincipalMenu.setGeometry(QtCore.QRect(60, 30, 231, 111))
        self.imgPrincipalMenu.setText("")
        self.imgPrincipalMenu.setScaledContents(True)
        self.imgPrincipalMenu.setAlignment(QtCore.Qt.AlignCenter)
        self.imgPrincipalMenu.setObjectName("imgPrincipalMenu")
        VPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VPrincipal)
        self.btnKWRB.clicked.connect(VPrincipal.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(VPrincipal)

    def retranslateUi(self, VPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VPrincipal.setWindowTitle(_translate("VPrincipal", "CONCESIONARIOS"))
        self.btnKWRB.setText(_translate("VPrincipal", "KENWORTH RIO BRAVO"))
        self.btnKWESTE.setText(_translate("VPrincipal", "KENWORTH DEL ESTE"))
        self.btnKWKREI.setText(_translate("VPrincipal", "KENWORTH KREI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VPrincipal = QtWidgets.QMainWindow()
    ui = Ui_VPrincipal()
    ui.setupUi(VPrincipal)
    VPrincipal.show()
    sys.exit(app.exec_())
