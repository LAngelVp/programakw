#########################
# DESARROLLADOR
# RMPG - LUIS ANGEL VALLEJO PEREZ
#########################
from decimal import Decimal
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os
import pandas as pd
from datetime import *
import numpy as np
from .Variables.ContenedorVariables import Variables
class OrdenesServicio(Variables):
    def OrdenesServicioKWRB(self):
        exceptoKenworth=["KENWORTH MEXICANA", "KENWORTH DEL ESTE"]
        registroos_tallerMovil = ['TM', 'Taller Movil']
        registroos_exceptoTipoServicio = ['Rescate Avalado','Rescate Carretero','TM', 'Taller Movil']
        registros_excluir = ['KENWORTH', 'PACCAR PARTS MEXICO','ALESSO','PACCAR FINANCIAL MEXICO','PACLEASE MEXICANA']
        
        path = os.path.join(Variables().ruta_Trabajo,'OSR.xlsx')

        # FIXME OBTENEMOS EL DOCUMENTO
        df = pd.read_excel(path, sheet_name='Hoja2')
        df = df.replace(to_replace=';', value='-', regex=True)
        ## NOTE Copia
        df1 = df.copy()
        df1 = df1.rename(columns={ 'Número Orden': 'num', 'Unidad':'UNI', 'Subtotal Ref Sin Facturar':'sub' })
        df1.insert(loc = 0,column = 'OS',value = 'OS',allow_duplicates = False)
        df1.insert(loc = 2, column = 'Num Orden', value = df1["OS"].map(str) + "" + df1["num"].map(str), allow_duplicates = False)
        df1.insert(loc = 3,column = 'UN',value = 'UN-',allow_duplicates = False)
        df1.insert(loc = 5, column = 'Unidad', value = df1["UN"].map(str) + "" + df1["UNI"].map(str), allow_duplicates = True)
        df1.drop(['OS', 'num', 'UN', 'UNI'], axis = 1, inplace=True)

        df1.insert(loc = 5, column = 'Clasificacion Cliente', value = 'CLIENTES GENERALES', allow_duplicates = False)
        #Clasificamos por cliente
        kenworths_concesionarios = df1.query("Cliente.str.contains('KENWORTH') and not Cliente.str.contains('|'.join(@exceptoKenworth))", local_dict={'exceptoKenworth': exceptoKenworth}).copy()
        kenworths_concesionarios["Clasificacion Cliente"] = "CONCESIONARIOS"

        garantia=df1.query("Cliente == ['KENWORTH MEXICANA', 'ALESSO', 'PACCAR PARTS MEXICO']").copy()
        garantia["Clasificacion Cliente"] = "GARANTIA"

        plm = df1.query("Cliente == ['PACCAR FINANCIAL MEXICO', 'PACLEASE MEXICANA']").copy()
        plm["Clasificacion Cliente"] = "PLM"

        ci = df1.query("Cliente == ['KENWORTH DEL ESTE']").copy()
        ci["Clasificacion Cliente"] = "CI"

        
        clientesGenerales = df1.query("~Cliente.str.contains('|'.join(@registros_excluir))", local_dict={'registros_excluir': registros_excluir}).copy()
        clientesGenerales["Clasificacion Cliente"] = "CLIENTES GENERALES"

        df_clasificado_cliente = pd.concat([kenworths_concesionarios,garantia,plm,ci,clientesGenerales], join="inner").copy()

       

        df_clasificado_cliente = df_clasificado_cliente.rename(columns={'Clasificacion Cliente':'CL','Tipo Servicio':'Tipop'})

        #Clasificamos por tipo servicio
        df_exceptoGarantia = df_clasificado_cliente.query("CL != ['GARANTIA']")

        df_soloGarantia = df_clasificado_cliente.query("CL == ['GARANTIA']")

        df_rescateAvalado = df_exceptoGarantia.query("Tipop == ['Rescate Avalado']").copy()
        df_rescateAvalado["CL"] = "RESCATES AVALADOS"

        df_rescateCarretero = df_exceptoGarantia.query("Tipop == ['Rescate Carretero']").copy()
        df_rescateCarretero["CL"] = "RESCATES CARRETEROS"

        
        df_tallerMovil = df_exceptoGarantia.query("Tipop.str.contains('|'.join(@registroos_tallerMovil))", local_dict={'registroos_tallerMovil': registroos_tallerMovil}).copy()
        df_tallerMovil["CL"] = "TALLER MOVIL"

        
        df_noClasificadosTipoServicio = df_exceptoGarantia.query("~Tipop.str.contains('|'.join(@registroos_exceptoTipoServicio))", local_dict={'registroos_exceptoTipoServicio': registroos_exceptoTipoServicio})

        df_clasificadoPorTiposervicio = pd.concat([df_soloGarantia,df_rescateAvalado,df_rescateCarretero,df_tallerMovil,df_noClasificadosTipoServicio], join="inner")

        df_clasificadoPorTiposervicio.insert(6, "Clasificacion Venta", df_clasificadoPorTiposervicio['CL'], allow_duplicates = False)

        columna = df_clasificadoPorTiposervicio.pop("sub")
        df_clasificadoPorTiposervicio.insert(21, "sub", columna)

        df_clasificadoPorTiposervicio.insert(loc=25, column = 'Total OS Pde Fact', value = df_clasificadoPorTiposervicio[['MO', 'CM', 'TOT', 'sub']].fillna(0).sum(axis=1), allow_duplicates = False)
        df_clasificadoPorTiposervicio['Total OS Pde Fact'] = pd.to_numeric(df_clasificadoPorTiposervicio['Total OS Pde Fact'], errors='coerce').fillna(0)
        df_clasificadoPorTiposervicio = df_clasificadoPorTiposervicio.rename(columns={'CL':'Clasificacion Cliente','Tipop':'Tipo Servicio','sub':'Subtotal Ref Sin Facturar'})
        

        for column_title in df_clasificadoPorTiposervicio:
            if ('Fecha' in column_title):
                try:
                    df_clasificadoPorTiposervicio[column_title] = (df_clasificadoPorTiposervicio[column_title].dt.strftime('%d/%m/%Y'))
                except:
                    pass
            else:
                pass
        
            
        columnas_bol=df_clasificadoPorTiposervicio.select_dtypes(include=bool).columns.tolist()
        df_clasificadoPorTiposervicio[columnas_bol] = df_clasificadoPorTiposervicio[columnas_bol].astype(str)

        ultima_columna = df_clasificadoPorTiposervicio.columns.get_loc("Estado Orden Global")
        
        df_clasificadoPorTiposervicio = df_clasificadoPorTiposervicio.iloc[:,:ultima_columna + 1]


        # # Guardar el libro de Excel
        df_clasificadoPorTiposervicio.to_excel(os.path.join(Variables().ruta_procesados,f'KWRB_OrdenesDeServicio_RMPG_{Variables().FechaExternsionGuardar()}.xlsx'), index=False)
