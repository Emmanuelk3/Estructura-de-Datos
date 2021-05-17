import os
import datetime
import pandas as pd
import sqlite3
from sqlite3 import Error
Borrador = lambda: os.system('clear')
try:
    with sqlite3.connect("Registro_venta.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS totales (clave INTEGER PRIMARY KEY, total TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS venta (clave INTEGER PRIMARY KEY, descripcion TEXT NOT NULL, unidades INTEGER NOT NULL ,   precio TEXT NOT NULL, fecha_venta DATE,idcuenta INTEGER NOT NULL);")

        def datos():
            monto_total = 0
            print("Registro de ventas")
            print("Presione enter si no agregara mas articulos!")

            while True:
                factura = ("select count(clave) from venta")
                c.execute(factura)
                n_registros = c.fetchone()          
                total_factura = ("select count(clave) from totales")
                c.execute(total_factura)
                cuenta_total = c.fetchone()
                for registro in n_registros:
                    clave = registro
                if registro:
                    clave = clave + 1
                else:
                    clave = 1            
                for claves in cuenta_total:
                    clave_total = claves
                if claves:
                    clave_total = clave_total + 1
                else:
                    clave_total = 1
                print(clave)
                print(clave_total)
                descripcion=str(input("Descripcion del articulo:"))
                
                if descripcion == "":
                    break
                else:
                    venta_unidades=int(input("Numero de piezas vendidas:"))
                    precio_uni=str(input("Precio de venta:"))
                    cTotal= float(precio_uni)
                    fecha_vta = datetime.date.today()
                    suma = (cTotal*venta_unidades)
                    monto_total = suma + monto_total
                    valores = {"clave": clave, "nombre":descripcion, "unidades":venta_unidades, "precio": precio_uni, "fecha": fecha_vta, "idcuenta": clave_total}
                    c.execute("INSERT INTO venta VALUES(:clave, :nombre, :unidades, :precio, :fecha, :idcuenta)", valores)
            totales ={"clave_total": clave_total, "total": monto_total}
            c.execute("INSERT INTO totales VALUES(:clave_total, :total)",totales)
            c.execute("SELECT clave, total FROM totales WHERE clave = :clave_total",totales)
            cuenta_final = c.fetchall()
            for Id, total in cuenta_final:
                print(f"Su total es: ${total}")
        
        def consulta():            
            print("Consultar ventas")           

            cuenta = ("select count(clave) from venta")
            c.execute(cuenta)
            n_registros = c.fetchone()
            if n_registros:
                buscar=int(input("Ingrese la clave de venta:"))
                clave_buscar = {"clave_b":buscar}
                c.execute("SELECT clave, descripcion, piezas, precio, fecha_venta FROM venta WHERE idcuenta = :clave_b",clave_buscar)
                resultado = c.fetchall()
                for Id, nombre, cantidad, precio, fecha in resultado:
                    print(f"Se compro {cantidad} unidades de {nombre} a un precio de ${precio} el día {fecha}")
            else:
                print("No  se encontaron ventas")
        
        def reporte():           
            print("Consulta de ventas")            

            cuenta = ("select count(clave) from venta")
            c.execute(cuenta)
            n_registros = c.fetchone()
            if n_registros:
                fecha_consultar = input("Ingresa la fecha (aaa-mm-dd): ")
                fecha_consultar = datetime.datetime.strptime(fecha_consultar, "%Y-%m-%d").date()
                fecha_buscar = {"fecha_b":fecha_consultar}
                c.execute("SELECT clave, descripcion, piezas, precio, fecha_venta FROM venta WHERE DATE(fecha_venta) = :fecha_b",fecha_buscar)
                resultado = c.fetchall()
                print("Descripción | Piezas vendidas | Precio | Fecha")
                print("*" * 60)
                for Id, nombre, cantidad, precio, fecha in resultado:
                    print(f"{nombre}\t\t {cantidad}\t\t {precio}\t {fecha} ")
            else:
                print("No se encontraron ventas registradas")
        
        def menu():
            while (True):
                    opcion = int(input("[1] Registrar una venta \t[2] Consultar una venta \t[3] Reporte de venta \t[4]Salir: "))
                    if opcion <= 4:
                        if opcion==1:
                            productos=datos()
                        if opcion==2:
                            consulta()
                        if opcion==3:
                            reporte()
                        if opcion==4:
                            break

                        input("Presiona enter para continuar...")
                    else:
                        print("Ingresa una opcion valida.")
                        input("Presiona enter para continuar...")


        menu()
except Error as e:
    print (e)
finally:
    if (conn):
        conn.close()
        print("Fin del programa")