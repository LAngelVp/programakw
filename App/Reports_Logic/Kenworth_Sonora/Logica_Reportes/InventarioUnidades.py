#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
import os
import pandas as pd
from datetime import *
from .Variables.ContenedorVariables import Variables
class InventarioUnidades(Variables):
    def __init__(self):
        super().__init__()
        self.nombre_doc = 'IUS.xlsx'
        path = os.path.join(Variables().ruta_Trabajo,self.nombre_doc)
        df = pd.read_excel(path, sheet_name="Hoja2")
        df1 = df.copy()
        df1.columns = df1.columns.str.replace(" ", "_")
        df1.drop(["Serie_Motor","Int._Diario","Fecha_Vencimiento","Fact._Compra_TipoCambio","Fact._Compra_Moneda"], axis=1, inplace=True)
        df1.insert(
            loc = 5,
            column = "Año Modelo",
            value = "AM"+df1["Año_Modelo"].map(str),
            allow_duplicates = True
        )
        col_serie = "S-" + df1["Serie"].map(str)
        df1["Serie"] = col_serie
        
        df1["TipoInv"] = df1["Tipo_Docto."].apply(lambda x:self.ClasificacionTipoInv(x))
        
        for i in df1:
            try:
                if ("f." in i.lower()):
                    df1[i] = pd.to_datetime(df1[i], errors="coerce")
                    df1[i] = df1[i].dt.strftime("%d/%m/%Y")
                else:
                    continue
            except:
                continue

        df1.drop(["Año_Modelo"], axis=1, inplace=True)
        columnas_bol=df1.select_dtypes(include=bool).columns.tolist()
        df1[columnas_bol] = df1[columnas_bol].astype(str)
        df1.columns = df1.columns.str.replace("_", " ")

        # COMMENT: COMPROBACION DEL NOMBRE DEL DOCUMENTO PARA GUARDARLO
        if (os.path.basename(Variables().comprobar_reporte_documento_rutas(self.nombre_doc)).split(".")[1] == self.nombre_doc.split(".")[1]):
            df1.to_excel(Variables().comprobar_reporte_documento_rutas(self.nombre_doc), index=False )
        else:
            df1.to_csv(Variables().comprobar_reporte_documento_rutas(self.nombre_doc), encoding="utf-8", index=False )
    
    def ClasificacionTipoInv(self, valor):
        if (valor == "Factura"):
            return "Propia"
        else:
            return "Consigna"