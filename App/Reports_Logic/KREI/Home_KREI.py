#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
# IMPORTACIONES
import sys
import os
import shutil
from resources import *
import threading
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from webbrowser import *
from .Logica_Reportes.Variables.ContenedorVariables import Variables
from .Inicio_FechaMovimiento import *
from .KenworthConnect import *
from .UI.V_KREI import *
import subprocess
#----------------------------------------

class Home_KREI(QMainWindow, QDialog, Variables):
    def __init__(self):
        super(Home_KREI,self).__init__()
        # variables a las rutas de los iconos e imagenes
        Icon_Cerrar = QIcon(":/Source/Icon_Close.png")
        Icon_Minimizar = QIcon(":/Source/Icon_Minimize.png")
        Icon_Help = QIcon(":/Source/Icon_Help.png")
        Icon_Delete = QIcon(":/Source/Icon_Delete.png")
        Icon_Proccess = QIcon(":/Source/Icon_Proccess.png")
        Icon_Upload = QIcon(":/Source/Icon_Upload.png")
        logo = QPixmap(":/Source/LOGOKREI.png")
        self.setWindowIcon(QIcon(":/Source/LOGO_KREI_3.ico"))
        
        # llamamos el metodo de creacion de carpetas
        self.Creacion_Carpetas()
        # quitamos la barra superior
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Crear la instancia de la ventana y configurarla
        self.Ventana = Ui_Kenworth_KREI()
        self.Ventana.setupUi(self)
        # colocar los iconos e imagenes en su correspondiente elemento.
        self.Ventana.lblLogoKWKREI.setPixmap(logo)
        self.Ventana.btc_btc_Cerrar.setIcon(Icon_Cerrar)
        self.Ventana.btc_btc_Minimizar.setIcon(Icon_Minimizar)
        self.Ventana.btn_btn_Ayuda.setIcon(Icon_Help)
        self.Ventana.btn_btn_Eliminar.setIcon(Icon_Delete)
        self.Ventana.btn_btn_Eliminar.setIconSize(QtCore.QSize(24, 24))
        self.Ventana.btn_btn_Comenzar.setIcon(Icon_Proccess)
        self.Ventana.btn_btn_Comenzar.setIconSize(QtCore.QSize(24, 24))
        self.Ventana.btn_btn_Subir.setIcon(Icon_Upload)
        self.Ventana.btn_btn_Subir.setIconSize(QtCore.QSize(24, 24))
        # creamos el hilo
        self.Hilo = trabajohilo()
        #conexiones de los botones
        self.Ventana.btn_btn_Subir.clicked.connect(self.Cargar)
        self.Ventana.btn_btn_Comenzar.clicked.connect(self.ComenzarProceso)
        self.Ventana.btn_btn_Eliminar.clicked.connect(self.RemoveProcessed)
        self.Ventana.btn_btn_Ayuda.clicked.connect(self.Help)
        self.Ventana.btc_btc_Cerrar.clicked.connect(self.Cerrar)
        self.Ventana.btc_btc_Minimizar.clicked.connect(self.Minimizar)
        self.Ventana.btn_btn_Errores.clicked.connect(self.abrir_ruta_errores)
        self.Ventana.btn_btn_Originales.clicked.connect(self.abrir_ruta_originales)
        self.Ventana.btn_btn_Procesados.clicked.connect(self.abrir_ruta_procesados)

        self.Ventana.actionFechaMovimiento.triggered.connect(self.FechaMovimiento)

        # señales del hilo
        self.Hilo.signal.connect(self.mensajeTrabajoTerminado)
        self.Hilo.signalDocumentosErroneos.connect(self.mensajeArchivoErroneo)
        self.Hilo.signalNombreArchivo.connect(self.nombreArchivoTrabajando)
        self.Hilo.signalShowTrabajos.connect(self.Show_Data_Trabajos)
        self.Hilo.signalShowProcesados.connect(self.Show_Data_Procesado)
        

        Home_DateMovement()
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()

    def FechaMovimiento(self):
        self.ventana_obj = Home_DateMovement()
        self.ventana_obj.show()

    def abrir_ruta_errores(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileNames(self, 'Abrir Archivo Excel', Variables().ruta_errores, 'Excel Archivos (*.xlsx);; CSV Archivos (*.csv)',options=options)
        
        if file_path:
            try:
                for path in file_path:
                    subprocess.Popen(['start', 'excel', path], shell=True)
            except Exception as e:
                print("Error al abrir el archivo con Excel:", e)
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
    def abrir_ruta_originales(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileNames(self, 'Abrir Archivo Excel', Variables().ruta_origina, 'Excel Archivos (*.xlsx);; CSV Archivos (*.csv)',options=options)
        
        if file_path:
            try:
                for path in file_path:
                    subprocess.Popen(['start', 'excel', path], shell=True)
            except Exception as e:
                print("Error al abrir el archivo con Excel:", e)
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
    def abrir_ruta_procesados(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileNames(self, 'Abrir Archivo Excel', Variables().ruta_procesados, 'Excel Archivos (*.xlsx);; CSV Archivos (*.csv)',options=options)
        
        if file_path:
            try:
                for path in file_path:
                    subprocess.Popen(['start', 'excel', path], shell=True)
            except Exception as e:
                print("Error al abrir el archivo con Excel:", e)
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()

    def mensajeTrabajoTerminado(self):
        msgE = QMessageBox()
        msgE.setWindowTitle("CONTENIDO DE TRABAJOS")
        msgE.setText("La carpeta de trabajo se encuentra totalmente vacia.")
        msgE.setIcon(QMessageBox.Information)
        msgE.setStandardButtons(QMessageBox.Yes)
        msgE.button(QMessageBox.Yes).setText("Entendido")
        x = msgE.exec_() 
        if (x == QMessageBox.Yes):
            textoVacio =""
            self.nombreArchivoTrabajando(textoVacio)
#-------------------------------------------------


    def mensajeArchivoErroneo(self, mensaje):
        msgE = QMessageBox()
        msgE.setWindowTitle("TRABAJOS ERRONEOS")
        msgE.setText(f'Los documentos que no se lograron procesar son:\n{mensaje}\nPuedes corregir su nombre y volverlos a subir.\nLa ruta de los errores es:\n {Variables().ruta_error}')
        msgE.setIcon(QMessageBox.Information)
        msgE.setStandardButtons(QMessageBox.Yes)
        msgE.button(QMessageBox.Yes).setText("Entendido")
        x = msgE.exec_()

#--------------------------------------------
# MOSTRAR NOMBRE DEL DOCUMENTO QUE SE ESTA TRABAJANDO
    def nombreArchivoTrabajando(self, nombre):
        if (nombre != ""):
            self.Ventana.lbl_TrabajandoCon.setText(f'Trabajando Con:')
            self.Ventana.lbl_NombreReporte.setText(f'{nombre}')
        else:
            self.Ventana.lbl_TrabajandoCon.setText(f'TERMINADO')
            self.Ventana.lbl_NombreReporte.setText(f'')
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
#--------------------------------------------
#-------------------------------------------------------
# EVENTOS DEL MOUSE
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
    # Apartado de funciones
    #-------------------------
    # mostrar el contenido de la carpeta en la tabla de trabajos.
    def Show_Data_Trabajos(self):
        archivos_para_mostrar = os.listdir(Variables().ruta_Trabajo)
        self.Ventana.Tabla_Cola.setRowCount(len(archivos_para_mostrar))
        self.Ventana.Tabla_Cola.setColumnCount(1)
        self.Ventana.Tabla_Cola.setHorizontalHeaderLabels(["Nombre del archivo"])
        for fila, archivo in enumerate(archivos_para_mostrar):
            elemento = QTableWidgetItem(archivo)
            elemento.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Bloqueamos la edición
            elemento.setForeground(QtGui.QColor(0, 0, 0))
            self.Ventana.Tabla_Cola.setItem(fila, 0, elemento)
            # font = QtGui.QFont()
            # font.setPointSize(30)  # Establece el tamaño de la letra a 14 puntos
            # elemento.setFont(font)
        # self.Ventana.Tabla_Cola.setColumnWidth(0, 415)
        header = self.Ventana.Tabla_Cola.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    # mostrar el contenido de la carpeta en la tabla de trabajos.
    def Show_Data_Procesado(self):
        archivos_para_mostrar = os.listdir(Variables().ruta_procesados)
        self.Ventana.Tabla_Procesado.setRowCount(len(archivos_para_mostrar))
        self.Ventana.Tabla_Procesado.setColumnCount(1)
        self.Ventana.Tabla_Procesado.setHorizontalHeaderLabels(["Nombre del archivo"])
        for fila, archivo in enumerate(archivos_para_mostrar):
            elemento = QTableWidgetItem(archivo)
            elemento.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Bloqueamos la edición
            elemento.setForeground(QtGui.QColor(0, 0, 0))
            self.Ventana.Tabla_Procesado.setItem(fila, 0, elemento)
            # font = QtGui.QFont()
            # font.setPointSize(30)  # Establece el tamaño de la letra a 14 puntos
            # elemento.setFont(font)
        # self.Ventana.Tabla_Procesado.setColumnWidth(0, 415)
        header = self.Ventana.Tabla_Procesado.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


    def Creacion_Carpetas(self):
        directorio = os.listdir(Variables().directorio_raiz)
        for i in directorio:
            if not os.path.exists(f'{Variables().ruta_Trabajo}'):
                os.makedirs(f'{Variables().ruta_Trabajo}')
            elif not os.path.exists(f'{Variables().ruta_origina}'):
                os.makedirs(f'{Variables().ruta_origina}')
            elif not os.path.isdir(f'{Variables().ruta_error}'):
                os.makedirs(f'{Variables().ruta_error}')
            elif not os.path.isdir(f'{Variables().ruta_procesados}'):
                os.makedirs(f'{Variables().ruta_procesados}')
            elif not os.path.isdir(f'{Variables().ruta_documentos}'):
                os.makedirs(f'{Variables().ruta_documentos}')
            else:
                pass
    # cerrar la ventana
    def Cerrar(self):
        self.close()
    # minimizar la ventana
    def Minimizar(self):
        self.showMinimized()

    # mostrar la data en las tablas
    
    # cargar los archivos a la carpeta de trabajo
    def Cargar(self):
        self.Creacion_Carpetas()
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
        ubicacion_carga = os.chdir(Variables().directorio_raiz)
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog  # Evitar el uso del diálogo nativo del sistema operativo (opcional)
        options |= QFileDialog.ReadOnly  # Permite abrir los archivos solo en modo lectura (opcional)
        options |= QFileDialog.HideNameFilterDetails  # Ocultar detalles del filtro (opcional)
        options |= QFileDialog.DontResolveSymlinks  # No resolver enlaces simbólicos (opcional)

        selected_filter = "Hojas de Excel (*.xlsx);;Todos los archivos (*)"
        
        if os.path.isdir(Variables().ruta_Trabajo) == True:
            try:
                file_names, filter_selected = QFileDialog.getOpenFileNames(
                    self,
                    "Selecciona archivo(s)",
                    "",
                    selected_filter,
                    options=options
                )
                for nombre_archivo in file_names:
                    shutil.move(nombre_archivo, Variables().ruta_Trabajo)
            except:
                pass
        else:
            os.makedirs(Variables().ruta_Trabajo)
            try:
                file_names, filter_selected = QFileDialog.getOpenFileNames(
                    self,
                    "Selecciona archivo(s)",
                    "",
                    selected_filter,
                    options=options
                )
                for nombre_archivo in file_names:
                    shutil.move(nombre_archivo, Variables().ruta_Trabajo)
            except:
                pass
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
#----------------------------------------        
    # REALIZAR PROCESO
    # HILO DEL TRABAJO DE " KWESTE "
    def ComenzarProceso(self):
        if self.Hilo.isRunning():
            self.Hilo.requestInterruption()
        else:
            self.Hilo.start()

    # eliminamos los trabajos realizados de la carpeta de exitosos.
    def RemoveProcessed(self):
        self.Creacion_Carpetas()
        ruta_trabajos_procesados = os.listdir(Variables().ruta_procesados)
        if (len(ruta_trabajos_procesados) == 0):
            mensaje = QMessageBox()
            mensaje.setWindowTitle("HISTORIAL DE REPORTES")
            mensaje.setText("No cuentas con trabajos procesados")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.button(QMessageBox.Ok).setText("ENTENDIDO")
            x = mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("ELIMINAR REPORTES")
            mensaje.setText("¿Quieres eliminar todos los reportes que ya fueron procesados?")
            mensaje.setIcon(QMessageBox.Question)
            mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            mensaje.button(QMessageBox.Yes).setText("ELIMINAR")
            mensaje.button(QMessageBox.No).setText("CANCELAR")
            x = mensaje.exec_()
            if (x == QMessageBox.Yes):
                carpeta_contenido_eliminar = os.listdir(Variables().ruta_procesados)
                for archivo in carpeta_contenido_eliminar:
                    if (len(carpeta_contenido_eliminar) != 0):
                        try:
                            archivo_completo = os.path.join(Variables().ruta_procesados, archivo)
                            os.remove(archivo_completo)
                        except:
                            pass
                    else:
                        pass
                self.Show_Data_Procesado()
                mensaje = QMessageBox()
                mensaje.setWindowTitle("ELIMINACION LISTA")
                mensaje.setText("Todos los archivos fueron removidos")
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.button(QMessageBox.Ok).setText("ENTENDIDO")
                x = mensaje.exec_()
            else:
                pass
            self.Show_Data_Trabajos()
            self.Show_Data_Procesado()
        self.Show_Data_Trabajos()
        self.Show_Data_Procesado()
    # mostramos el apartado de ayuda
    def Help(self):
        msgA = QMessageBox()
        msgA.setWindowTitle("Información de Ayuda")
        msgA.setText('Para recibir ayuda sobre el funcionamiento del sistema o alguna aclaración, favor de contactar al desarrollador propietario del sistema:\n \nDesarrollador: Luis Ángel Vallejo Pérez\n\nCorreo: angelvallejop9610@gmail.com \n\nTelefono: 271-707-1259 \n \nSí quieres ver los nombres que deben de llevar los documentos, selecciona el boton de "Ver Ayuda"')
        msgA.setIcon(QMessageBox.Information)
        msgA.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msgA.button(QMessageBox.Cancel).setText("Entendido")
        msgA.button(QMessageBox.Ok).setText("Ver Ayuda")
        x = msgA.exec_()
        if (x == QMessageBox.Ok):
            open_new(Variables().pdf)
        else:
            pass

# CLASE DEL HILO----------------------
class trabajohilo(QThread, Variables):
# agregamos una variable de tipo señal
    signal = pyqtSignal()
    signalDocumentosErroneos = pyqtSignal(str)
    signalShowTrabajos = pyqtSignal()
    signalShowProcesados = pyqtSignal()
    signalNombreArchivo =  pyqtSignal(str)

    def run(self):
        array_errores = []
        #---------------------------------------
        # diccionario de los archivos.
        diccionario_archivos = {
            "OSEKREI.xlsx" : KenworthConnect().OrdenesServicioKREIKWESTE,
            "OSSKREI.xlsx" : KenworthConnect().OrdenesServicioKREIKWSUR,
            "CEKREI.xlsx" : KenworthConnect().CreditoKREIKWESTE,
            "CSKREI.xlsx" : KenworthConnect().CreditoKREIKWSUR,
            "ICEKREI.xlsx" : KenworthConnect().InventarioKREIKWESTE,
            "ICSKREI.xlsx" :KenworthConnect().InventarioKREIKWSUR,
            "REKREI.xlsx" : KenworthConnect().RefaccionesKREIKWESTE,
            "RSKREI.xlsx" : KenworthConnect().RefaccionesKREIKWSUR,
            "SDEKREI.xlsx" : KenworthConnect().ServicioDetalladoKREIKWESTE,
            "SDSKREI.xlsx" : KenworthConnect().ServicioDetalladoKREIKWSUR,
            "RFEKREI.xlsx" : KenworthConnect().ResultadosFinancierosKREI,
            "RFSKREI.xlsx" : KenworthConnect().ResultadosFinancierosKREI

        }
        #-----------------------------------------------
        while True:
            carpeta_de_trabajos = os.listdir(Variables().ruta_Trabajo)
            if not carpeta_de_trabajos:
                nombre_documento = ""
                self.signalNombreArchivo.emit(nombre_documento)
                return
            else:
                for nombre_archivo in carpeta_de_trabajos:
                    if (nombre_archivo in diccionario_archivos):
                        try:
                            self.signalNombreArchivo.emit(nombre_archivo)
                            Metodo = diccionario_archivos[nombre_archivo]
                            Metodo()
                            self.Comprobacion_Originales(nombre_archivo)
                            self.signalShowTrabajos.emit()
                            self.signalShowProcesados.emit()
                        except Exception as e:
                            array_errores.append(nombre_archivo)
                            self.Comprobacion_Errores(nombre_archivo)
                            self.signalShowTrabajos.emit()
                            self.signalShowProcesados.emit()
                            continue
                    else:
                        nombre_archivo_error = nombre_archivo
                        array_errores.append(nombre_archivo_error)
                        self.Comprobacion_Errores(nombre_archivo)
                        self.signalShowTrabajos.emit()
                        self.signalShowProcesados.emit()
                        continue
                self.signalShowTrabajos.emit()
                self.signalShowProcesados.emit()
            if array_errores:
                mensaje = ""
                x = 1
                for i in array_errores:
                    mensaje += f'{x}.-{i}\n'
                    x += 1
                self.signalDocumentosErroneos.emit(mensaje)
                continue
            self.signalShowTrabajos.emit()
            self.signalShowProcesados.emit()

#--------------------------------------------------
# COMPROBAR SI EXISTE EL DOCUMENTO ORIGINAL EN EL DESTINO
    def Comprobacion_Originales(self, file_name):
        ruta_origen = os.path.join(Variables().ruta_Trabajo, file_name)
        destino_archivoOriginal = os.path.join(Variables().ruta_origina, file_name)
        if not os.path.exists(destino_archivoOriginal):
            shutil.move(ruta_origen, Variables().ruta_origina)
        else:
            os.remove(destino_archivoOriginal)
            shutil.move(ruta_origen, Variables().ruta_origina)
#--------------------------------------------------
#--------------------------------------------------
# COMPRROBAR SI EXISTE EL DOCUMENTO ERRONEO EN EL DESTINO
    def Comprobacion_Errores(self, file_name):
        ruta_origen = os.path.join(Variables().ruta_Trabajo, file_name)
        destino_archivoOriginal = os.path.join(Variables().ruta_error, file_name)
        if not os.path.exists(destino_archivoOriginal):
            shutil.move(ruta_origen, Variables().ruta_error)
        else:
            os.remove(destino_archivoOriginal)
            shutil.move(ruta_origen, Variables().ruta_error)
#--------------------------------------------------------


# ------------------------------------------------------------------------
# MANDAMOS A LLAMAR A LA VENTANA
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Crear una instancia de la clase MyDialog y mostrarla
    Ventana = Home_KREI()
    Ventana.show()
    sys.exit(app.exec_())