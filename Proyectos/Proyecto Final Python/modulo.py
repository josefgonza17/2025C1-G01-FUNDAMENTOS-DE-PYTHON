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

df_all["Monto en miles de millones"] = df_all["DE_Monto"]/1000000000 #Convertir montos en miles de millones

df_all["Monto en millones"] = df_all["Monto en miles de millones"].astype(int) #Cambia el tipo de float a Int

#print(df_all.shape) #comprobación de la unión de los df


def tabla_resumen (): 
    
    df_totales = df_all[df_all["Mes"] == 12] #Se filtra el mes 12 debido a que la información es acumulada
    df_summary = df_totales.groupby("Ejercicio")["Monto en miles de millones"].sum() #Agrupación por año
    print(f"\n El resumen de recaudación es el siguiente expresado en miles de millones de colones: {df_summary}")
     
def grafico_resumen ():
    df_grafico = df_all[["Ejercicio","Mes","Monto en miles de millones"]] #Se seleccionan las columnas necesarias para el analisis
    df_grafico_totales = df_grafico[df_grafico["Mes"] == 12] #Se filtra el mes 12 debido a que la información es acumulada
    df_grafico_summary = df_grafico_totales.groupby("Ejercicio")["Monto en miles de millones"].sum() #Agrupación por año
    
    #Configuración de gráfico
    
    plt.plot(df_grafico_summary, marker="o", markersize="7", ls="-.")
    plt.title("Ingresos últimos 3 años Ministerio de Hacienda \n Incluye Ingresos y Financimientos ")
    plt.xticks([2022,2023,2024])
    plt.xlabel("Años")
    plt.ylabel("Miles de Millones")
    plt.ylim(10000,13000)
    
    plt.show() #Para mostrar gráfico


def max_min_recaudacion ():
    df_recaudacion = df_all[["Ejercicio","Mes", "CI_Grupo_Descripcion", "CI_Clase_Descripcion","Monto en miles de millones"]]  #Se seleccionan las columnas necesarias para el analisis  
    df_recaudacion = df_recaudacion[df_recaudacion["Mes"] == 12]
    df_recaudacion = df_recaudacion[df_recaudacion["CI_Clase_Descripcion"] == "INGRESOS CORRIENTES"] #Se filtra por los ingresos corrientes del MH
    df_recaudacion_max = df_recaudacion.groupby(["Ejercicio","CI_Grupo_Descripcion"])["Monto en miles de millones"].sum().idxmax() #Se determina el mayor concepto de recaudación
    df_recaudacion_min = df_recaudacion.groupby(["Ejercicio","CI_Grupo_Descripcion"])["Monto en miles de millones"].sum().idxmin() #Se determina el menor concepto de recaudación

    print(f"\n El mayor concepto de recaudación fue: {df_recaudacion_max}")
    print(f"\n El menor concepto de recaudación fue: {df_recaudacion_min}")
    
def mayor_recaudacion ():
    df_mayor_recaudacion = df_all[["Ejercicio","Mes", "CI_Grupo_Descripcion", "CI_Clase_Descripcion","Monto en miles de millones"]]  #Se seleccionan las columnas necesarias para el analisis  
    df_mayor_recaudacion = df_mayor_recaudacion[df_mayor_recaudacion["Mes"] == 12]
    df_mayor_recaudacion = df_mayor_recaudacion[df_mayor_recaudacion["CI_Clase_Descripcion"] == "INGRESOS CORRIENTES"] #Se filtra por los ingresos corrientes del MH
    df_mayor_recaudacion_year = df_mayor_recaudacion.groupby("Ejercicio")["Monto en miles de millones"].sum().idxmax()  
    df_mayor_recaudacion_amount = df_mayor_recaudacion.groupby("Ejercicio")["Monto en miles de millones"].sum().max()   
    print(f"\n El año con mayor recaudación fue el {df_mayor_recaudacion_year} con un monto de {df_mayor_recaudacion_amount:.2f} miles de millones de colones")



