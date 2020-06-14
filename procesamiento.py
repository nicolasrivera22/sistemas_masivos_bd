import pandas as pd
import numpy as np

municipio = "medellín"

# path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\temperatura_test.csv"
path = "G:\\Mi unidad\\Nicolás\\Universidad Nacional\\Especializacion_analitica\\1er Semestre\\Sistemas_masivos_bd\\Trabajo_Final\\Datos\\Temperatura_Maxima_del_Aire.csv"

TextFileReader = pd.read_csv(path, chunksize=1e6)  # the number of rows per chunk

df = pd.DataFrame([])
for df_chunk in TextFileReader:
    # df_chunkList.append(df_chunk)
    df = df.append(df_chunk[df_chunk.columns][df_chunk["Municipio"].str.upper() == municipio.upper()])

print(df)
df.to_csv('test.csv')
print('fin')
# df = pd.concat(dfList,sort=False)


# df_data = pd.read_csv(path, encoding='UTF', chunksize = 2e6)

# test = df_data[df_data.columns][df_data["Municipio"].str.upper() == municipio.upper()]


