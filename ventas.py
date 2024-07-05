import os
import random
import globales
os.system("cls")


def precargar_ventas():
    empleados = globales.leer_archivo_json('trabajadores.json')
    ventas = globales.leer_archivo_json('ventas.json')
    for i in range(10):
        empleado= random.choice(empleados)
        venta= random.randint(150, 500)*10000

        nueva_venta = {
            "nombre": empleado,
            "ventas": venta
        }

        ventas.append(nueva_venta)
    
    globales.guardar_archivo_json('ventas.json', ventas)
    input("Ventas cargadas")

