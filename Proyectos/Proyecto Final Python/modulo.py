#Importación de la base de datos

import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#Importar datos para el 2024

ruta_2024 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertos_Ingresos_Dic2024.csv"

df_2024 = pd.read_csv(ruta_2024, delimiter=",", encoding="latin-1")

#Importar datos para el 2023

ruta_2023 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertosDic23_Ingresos.csv"

df_2023 = pd.read_csv(ruta_2023, delimiter=",", encoding="latin-1")  

#Importar datos para el 2022  

ruta_2022 = "/Users/josefgonzalez/Documents/GitHub/2025C1-G01-FUNDAMENTOS-DE-PYTHON/Proyectos/Proyecto Final Python/DatosAbiertosIngresos2022-12.csv"

df_2022 = pd.read_csv(ruta_2022, delimiter=",", encoding="utf-8")

#Consolidacion dataframes 3 años

df_all = pd.concat([df_2023,df_2024,df_2022])

df_all["DE_Monto"] = df_all["DE_Monto"].astype(float)

df_all["Monto en miles de millones"] = df_all["DE_Monto"]/1000000000

df_all["Monto en millones"] = df_all["Monto en miles de millones"].astype(int) #Cambia el tipo de float a Int

print(df_all.shape) #comprobación de la unión de los df


def tabla_resumen ():
    
    df_totales = df_all[df_all["Mes"] == 12]
    df_summary = df_totales.groupby("Ejercicio")["Monto en miles de millones"].sum()
    print(f"El resumen de recaudación es el siguiente expresado en miles de millones de colones: {df_summary}")
     
def grafico_resumen ():
    df_grafico = df_all[["Ejercicio","Mes","Monto en miles de millones"]]
    df_grafico_totales = df_grafico[df_grafico["Mes"] == 12]
    df_grafico_summary = df_grafico_totales.groupby("Ejercicio")["Monto en miles de millones"].sum()
    plt.plot(df_grafico_summary)
    plt.title("Ingresos últimos 3 años Ministerio de Hacienda")
    plt.xticks([2022,2023,2024])
    plt.xlabel("Años")
    plt.ylabel("Miles de Millones")
    plt.ylim(10000,13000)
    plt.show()







    
