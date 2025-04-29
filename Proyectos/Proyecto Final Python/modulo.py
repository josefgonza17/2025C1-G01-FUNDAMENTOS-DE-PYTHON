#Importación de la base de datos

import pandas as pd

#Importar datos para el 2024

ruta_2024 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertos_Ingresos_Dic2024.csv"

df_2024 = pd.read_csv(ruta_2024, delimiter=",", encoding="latin-1")

#Importar datos para el 2023

ruta_2023 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertosDic23_Ingresos.csv"

df_2023 = pd.read_csv(ruta_2024, delimiter=",", encoding="latin-1")  

#Importar datos para el 2022  

ruta_2022 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertosIngresos2022-12.csv"

df_2022 = pd.read_csv(ruta_2024, delimiter=",", encoding="latin-1")


#Consolidacion dataframes 3 años

df_all = pd.concat([df_2022,df_2023,df_2024])

print(df_all.shape) #comprobación de la unión de los df



