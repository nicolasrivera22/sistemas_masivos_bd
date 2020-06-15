from procesar_datos import Datos

"""
1. Verificar el nombre del archivo e ingresarlo en la variable archivo.
2. Ingrese la ruta de la carpeta donde está alojado el archivo
3. Si requiere, procese las columnas con formato de datetime, para ello use la lista columns_fecha
4. Si lo requiere, filtre las columnas usando el diccionario dict_filtro. La llave es la columna a filtrar, el contenido es el filtro
5. Verificar el tamaño, si es muy grande (superior a 1M líneas) usar el método leer_archivo_pesado
"""


archivo = "Temperatura_Maxima_del_Aire"
path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\"
columns_fecha = ["FechaObservacion"]
dict_filtro = {"Municipio":"medellín"}

Data = Datos(archivo=archivo, path=path, columns_fecha=columns_fecha)



Data.leer_archivo_pesado(dict_filtro=dict_filtro)
Data.leer_archivo(dict_filtro=dict_filtro)


Data.procesar_fechas()

Data.df.to_csv(path+"archivo"+"procesado.csv")