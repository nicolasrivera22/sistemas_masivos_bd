from procesar_datos import Datos


archivo = "Temperatura_Maxima_del_Aire"
path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\"
columns_fecha = ["FechaObservacion"]
dict_filtro = {"Municipio":"medellín"}

Data = Datos(archivo=archivo, path=path, columns_fecha=columns_fecha)



Data.leer_archivo_pesado(dict_filtro=dict_filtro)
Data.leer_archivo(dict_filtro=dict_filtro)


Data.procesar_fechas()

Data.df.to_csv(path+"archivo"+"procesado.csv")