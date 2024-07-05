import globales
import math

def buscar_venta_mas_alta():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    todos_los_empleados = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['ventas'], reverse=True)
    
    print("| empleado | total venta |")
    for venta in ventas_ordenadas[:1]:
        nombre_empleado = ""
        for empleado in todos_los_empleados:
            if empleado['nombre'] == venta['nombre']:
                nombre_empleado = f"{empleado['nombre']}"
    
        print(f"| {nombre_empleado} | {venta['ventas']}")

def buscar_venta_mas_baja():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    todos_los_empleados = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['ventas'], reverse=False)
    
    print("| empleado | total venta |")
    for venta in ventas_ordenadas[:1]:
        nombre_empleado = ""
        for empleado in todos_los_empleados:
            if empleado['nombre'] == venta['nombre']:
                nombre_empleado = f"{empleado['nombre']}"
    
        print(f"| {nombre_empleado} | {venta['ventas']}")

def  obtener_promedio_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += venta['ventas']
        cantidad_ventas += 1
    promedio_ventas = suma_ventas / cantidad_ventas
    
    print(f"El Promedio de las ventas es ${int(promedio_ventas)}")

def obtener_media_geometrica():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += math.log(venta['ventas'])
        cantidad_ventas += 1
    
    media_geometrica = math.exp(suma_ventas / cantidad_ventas)

    print(f"La media geometrica de las ventas es ${int(media_geometrica)}")

obtener_media_geometrica()