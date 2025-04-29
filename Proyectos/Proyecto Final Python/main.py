"""
Autor: José F González 
Fecha: 2025-04-27
Versión: V2 Final
Sistema para el análisis de los ingresos recaudados por el Ministerios de Hacienda de CR durante los últimos 3 años   
"""
from modulo import tabla_resumen, grafico_resumen


def pausar ():
    input('\nPresione Enter para continuar....')
    
def menu (): #Creación de un menú para ingresar al análisis
    
    while True:
        print("\n---–– Menú Principal del análisis -----")
        print("1. Tabla Resumen anual")
        print("2. Cuál fue el mayor concepto por recaudación y cuál fue el menor")
        print("3. Año con mayor recaudación")
        print("4. Salir")
        opcion = input ("Ingresar una opción: ")
        
        if opcion == "1":
            print('\n ---- Tabla Resumen Anual ----')
            tabla_resumen()
            pausar()
        elif opcion == "2":
            print('\n ---- Cuál fue el mayor concepto por recaudación y cuál fue el menor ----')
            pass
            pausar()
        elif opcion == "3":
            print('\n ---- Año con mayor recaudación ----')
            pass
            pausar()
        elif opcion == "4":
            print('\n ---- Salir ----')
            pausar()
            break #<- Cierro el sistema deteniendo el ciclo while
        else:
            print("Opción no está dentro del menú. Intente nuevamente con otra opción")
            pausar()

#Ejecuciòn del sistema si solo si el archivo es el main

if __name__ == "__main__":
    print("\n Bienvenido al Proyecto Final de Pyhton: ", 
          "\n Análisis de Ingresos del Ministerio de Hacienda")
    menu()

    
