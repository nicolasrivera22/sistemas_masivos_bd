import pandas as pd

municipio = "medellín"
archivo = "Temperatura_Maxima_del_Aire"
# path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\temperatura_test.csv"
path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\"

TextFileReader = pd.read_csv(path+archivo+".csv", chunksize=1e6)  # the number of rows per chunk
df = pd.DataFrame([])
for df_chunk in TextFileReader:
    # df_chunkList.append(df_chunk)
    df = df.append(df_chunk[df_chunk.columns][df_chunk["Municipio"].str.upper() == municipio.upper()])

df['FechaObservacion'] = pd.to_datetime(df['FechaObservacion'])
df.to_csv(path + archivo + "_procesados.csv")