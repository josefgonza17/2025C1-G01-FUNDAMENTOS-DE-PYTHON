import csv, os, pandas as pd


def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso = input ("Ingrese el nombre del curso: ").upper()
            cantidad = int(input("Ingrese la cantidad de curso vendidos: "))
            fecha = input("Ingrese la fecha de la venta (AAA-MM-DD): ")
            precio = float(input("Ingrese el precio del curso: " ))
            cliente = input("Ingrese el nombre del cliente: ").upper()
        except ValueError:
            print("Entradas no válidas, por favor intentelo nuevamente!")
            continue
        ventas = {
            "curso" : curso,
            "cantidad" : cantidad,
            "precio": precio,
            "fecha": fecha,
            "cliente": cliente
        }
        
        lista_ventas.append(ventas)
        
        continuar = input("Desea ingresar otra venta s/n : ").lower()
        if continuar == "s":
            print(" ---- Ingresando otra venta -----")
        elif continuar == "n":
            break
        else: 
            print("opción no válida") 
    
def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append 'A'
            with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writerows(ventas)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ventas.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso
        ventas = []
        print('Datos guardados exitosamente!')
        
def analisis_ventas ():
    df = pd.read_csv("ventas.csv")
    print("\n --------- RESUMEN VENTAS ----------")
    
    df["subtotal"] = df["cantidad"] * df["precio"]
    total_ingresos = df["subtotal"].sum()
    
    print(f"total de ventas {total_ingresos:.2f}")
    
    #cursos más vendido
    curso_top = df.groupby("curso")["cantidad"].sum().idxmax()
    print("El curso más vendido es: ", curso_top)
    
    #cliente con más compras
    cliente_top = df.groupby("cliente")["cantidad"].sum().idxmax()
    print("El cliente que más compró fue: ", cliente_top)
    
    #cliente con más compras
    ventas_fechas = df.groupby("fecha")["subtotal"].sum().sort_values(ascending=False)
    print("Las ventas por fechas son las siguientes: ", ventas_fechas)
    
    