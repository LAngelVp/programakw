#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
import os
import pandas as pd
from .Variables.ContenedorVariables import Variables

class SeguimientoCores(Variables):
    def __init__(self):
        super().__init__()
        self.nombre_doc = 'SCE.xlsx'
        path = os.path.join(Variables().ruta_Trabajo,self.nombre_doc)
        df = pd.read_excel(path, sheet_name='Hoja2')
        df = df.replace(to_replace=';', value='-', regex=True)

        df_SeguimientoCores = df.copy()

        columna_FechaFactura = df_SeguimientoCores.pop("FechaFactura")
        df_SeguimientoCores.insert(5, "FechaFactura", columna_FechaFactura)

        columna_FechaRecEnSucProcCores = df_SeguimientoCores.pop("FechaRecEnSucProcCores")
        df_SeguimientoCores.insert(6, "FechaRecEnSucProcCores", columna_FechaRecEnSucProcCores)

        df_SeguimientoCores.insert(7,"Fecha Hoy", Variables().date_movement_config_document(), allow_duplicates=False)

        Antiguedad = df_SeguimientoCores.apply(self.OperacionAntiguedad, axis = 1)

        df_SeguimientoCores.insert(8,"Antigüedad", Antiguedad, allow_duplicates=False)

        df_SeguimientoCores["EstadoFact"] = df_SeguimientoCores.apply(self.EstadoFactura, axis = 1)

        df_SeguimientoCores.drop(["TE","TR","FechaRecEnSuc"], axis = 1)

        for i in df_SeguimientoCores:
            if ("fecha" in i.lower()):
                df_SeguimientoCores[i] = pd.to_datetime(df_SeguimientoCores[i] , errors = 'coerce')
                try:
                    df_SeguimientoCores[i] = df_SeguimientoCores[i].dt.strftime("%d/%m/%Y")
                except:
                    pass

        columnas_bol=df_SeguimientoCores.select_dtypes(include=bool).columns.tolist()
        df_SeguimientoCores[columnas_bol] = df_SeguimientoCores[columnas_bol].astype(str)
        df_SeguimientoCores['Antigüedad'] = pd.to_numeric(df_SeguimientoCores['Antigüedad'].dt.days, downcast='integer')

        # COMMENT: COMPROBACION DEL NOMBRE DEL DOCUMENTO PARA GUARDARLO
        if (os.path.basename(Variables().comprobar_reporte_documento_rutas(self.nombre_doc)).split(".")[1] == self.nombre_doc.split(".")[1]):
            df_SeguimientoCores.to_excel(Variables().comprobar_reporte_documento_rutas(self.nombre_doc), index=False )
        else:
            df_SeguimientoCores.to_csv(Variables().comprobar_reporte_documento_rutas(self.nombre_doc), encoding="utf-8", index=False )

    def EstadoFactura(self, row):
        if pd.notna(row["FechaFactura"]):
            return "Facturado"
        else:
            return "Pendiente"

    def OperacionAntiguedad(self, row):
        if pd.notna(row["FechaFactura"]):
            return row["Fecha Hoy"] - row["FechaFactura"]
        else:
            return row["Fecha Hoy"] - row["Fecha"]
