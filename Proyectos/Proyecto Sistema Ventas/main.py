"""
Autor: José F González Salgado
Fecha: 2025-04-16
Versión: 0.1
Sistema de Gestión de Ventas que nos permita ingresar, almacenar y analizar datos de ventas.
"""

import os 
from modulo import ingresar_ventas, guardar_ventas, analisis_ventas



def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    
    input('\nPresione Enter para continuar....')


def menu ():
    #Variables del sistema
    ventas = []
    while True:
        print("--- Menú Principal -----")
        print("1. Ingresar Ventas de cursos UMCA")
        print("2. Guardar datos en un archivo CSV")
        print("3. Analizar Ventas")
        print("4.  Salir")
        opcion = input ("Ingresar una opción: ")
        
        if opcion == "1":
            print('\n ---- Ingreso de Ventas de Cursos ----')
            ingresar_ventas(ventas)
            print(ventas)
            pausar()
        elif opcion == "2":
            limpiar_pantalla()
            print('\n ---- Guardar datos en un archivo CSV ----')
            guardar_ventas(ventas)
            pausar()
        elif opcion == "3":
            limpiar_pantalla()
            print('\n ---- Analizar Ventas ----')
            analisis_ventas()
            pausar()
        elif opcion == "4":
            print('\n ---- Salir ----')
            pausar()
            break #<- Cierro el sistema deteniendo el ciclo while
        else:
            print('Opción no válida. Intente nuevamente una opción!')
            pausar()
        

#Ejecuciòn del sistema si solo si el archivo es el main

if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Ventas")
    menu()
