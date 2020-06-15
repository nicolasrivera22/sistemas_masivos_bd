import pandas as pd
import csv

class Datos:
    """# Clase para leer y almacenar los Datos leídos desde un archivo plano CSV usando Pandas
    """
    def __init__(self,separador=',', archivo=None, path=None, columns_fecha=None):
        """Inicialización de Datos

        Args:
            separador (str): Separador de columnas. Defaults to ','.
            archivo (str): Nombre del archivo. Defaults to None.
            path (str): Ruta del archivo. Defaults to None.
            columns_fecha (list): Lista de columnas de fecha a procesar. Defaults to None.
        """
        self.separador = separador
        self.archivo = archivo
        self.path = path
        self.columns_fecha = columns_fecha
        self.df = pd.DataFrame([])

    def leer_archivo(self, dict_filtro=None):
        if self.archivo is None:
            return
        if dict_filtro is None:
            df = pd.read_csv(self.path+self.archivo+".csv", delimiter=self.separador)
        else:
            df = pd.read_csv(self.path+self.archivo+".csv", delimiter=self.separador)
        self.df = df
        return df
    def leer_archivo_pesado(self, dict_filtro=None):
        if self.archivo is None:
            return
        try:
            df = pd.DataFrame([])
            if dict_filtro is None:
                TextFileReader = pd.read_csv(
                    self.path+self.archivo+".csv", chunksize=1e6, delimiter=self.separador)
                for df_chunk in TextFileReader:
                    df = df.append(df)
            else:
                TextFileReader = pd.read_csv(
                    self.path+self.archivo+".csv", chunksize=1e6, delimiter=self.separador)
                for df_chunk in TextFileReader:
                    # df = df.append(df_chunk[df_chunk.columns][df_chunk["Municipio"].str.upper() == municipio.upper()])
                    for key in dict_filtro:
                        df = df.append(
                            df_chunk[df_chunk.columns][df_chunk[key].str.upper() == dict_filtro[key].upper()])
        except Exception as e:
            print('Error. Detalle: {}'.format(e.args[0]))
            raise Exception('leer_datos_pesados')
            
        self.df = df
        return df

    def procesar_fechas(self):
        for fecha in self.columns_fecha:
            self.df[fecha] = pd.to_datetime(self.df[fecha])
        return self.df
    
