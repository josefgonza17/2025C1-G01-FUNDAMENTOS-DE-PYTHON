
import pandas as pd

ruta_archivo_csv = "DatosAbiertos_Ingresos_Dic2024.csv" #Se define la ruta del archivo

df = pd.read_csv(ruta_archivo_csv, delimiter=',')

df

