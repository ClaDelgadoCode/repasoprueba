import os
import ventas
import globales
import estadisticas
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Generar Venta alatoria")
        print("2. Ver estadisticas")
        print("3. Salir del programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            ventas.precargar_ventas()
        elif opcion == 2:
            print("estadisticas")
            print("**** Venta mas alta ****")
            estadisticas.buscar_venta_mas_alta()
            print("**** Venta Mas Baja ****")
            estadisticas.buscar_venta_mas_baja()
            estadisticas.obtener_promedio_ventas()
            estadisticas.obtener_media_geometrica()
        elif opcion == 3:
            return
        input()

if __name__ == "__main__":
    menu_general()