#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
# esta clase sera intermediaria entre el front con el back.
from .Logica_Reportes.SalidasEnVale import *
from .Logica_Reportes.Credito import *
from .Logica_Reportes.BackOrder import *
from .Logica_Reportes.Compras import *
from .Logica_Reportes.ResultadosFinancieros import *
from .Logica_Reportes.InventarioUnidades import *
from .Logica_Reportes.TrabajosPorEstado import *
from .Logica_Reportes.OrdenesDeServicio import *
from .Logica_Reportes.InventarioCosteadoAndDia import *
from .Logica_Reportes.PagoClientes import *
from .Logica_Reportes.Refacciones import *
from .Logica_Reportes.ServicioDetallado import *
from .Logica_Reportes.VentasOrdenesServicio import *
#-----------------------------------

#CLASE
class KenworthConnect():
    # este sera el apartado en donde se colocaran las funciones que conectaran al back.
    def __init__(self):
        pass

    def SalidaEnVale(self):
        SalidasEnVale()

    def Credito(self):
        Credito()

    def BackOrder(self):
        BackOrder()

    def Compras(self):
        Compras()
    
    def ResultadosFinancieros(self):
        ResultadosFinancieros()

    def InventarioDeUnidades(self):
        InventarioUnidades()

    def TrabajosPorEstado(self):
        TrabajosPorEstado()

    def OrdenesDeServicio(self):
        OrdenesDeServicio()

    def InventarioCosteadoAndInventarioPorDia(self):
        InventarioCosteado()

    def PagoDeClientes(self):
        PagosDeClientes()

    def Refacciones(self):
        Refacciones()

    def ServicioDetallado(self):
        ServicioDetallado()

    def VentasServicio(self):
        VentasServicio()