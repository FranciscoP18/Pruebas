import json
import datetime
# Diccionario de juegos disponibles en la tienda
pizzas_disponibles = {
    "cuatro quesos": [
        {"nombre": "Cuatro Quesos", "tamaño": "Pequeña", "precio": 6000},
        {"nombre": "Cuatro Quesos", "tamaño": "Mediana", "precio": 9000},
        {"nombre": "Cuatro Quesos", "tamaño": "Familiar", "precio": 12000}
    ],
    "hawaiana": [
        {"nombre": "Hawaiana", "tamaño": "Pequeña", "precio": 6000},
        {"nombre": "Hawaiana", "tamaño": "Mediana", "precio": 9000},
        {"nombre": "Hawaiana", "tamaño": "Familiar", "precio": 12000}
    ],
    "napolitana": [
        {"nombre": "Napolitana", "tamaño": "Pequeña", "precio": 5500},
        {"nombre": "Napolitana", "tamaño": "Mediana", "precio": 8500},
        {"nombre": "Napolitana", "tamaño": "Familiar", "precio": 11000}
    ],
    "peperonni": [
        {"nombre": "Peperonni", "tamaño": "Pequeña", "precio": 7000},
        {"nombre": "Peperonni", "tamaño": "Mediana", "precio": 10000},
        {"nombre": "Peperonni", "tamaño": "Familiar", "precio": 13000}
    ]
}

# Estructura para almacenar las ventas
ventas = []

# Función para registrar una venta
def registrar_venta():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    tipo_cliente = input("Ingrese el tipo de estudiante (Diurno, Vespertino, Administrativo): ").lower()
    tipo_pizza = input("Ingrese el tipo de pizza (Cuatro quesos, Hawaiana, Napolitana, Peperonni): ").lower()
    
    if tipo_pizza in pizzas_disponibles:
        print(f"Detalles para el tipo de pizza {tipo_pizza}:")
        for i, pizza in enumerate(pizzas_disponibles[tipo_pizza], start=1):
            print(f"{i}. {pizza['nombre']} - {pizza['tamaño']} - ${pizza['precio']}")
        
        indice_pizza = int(input("Seleccione el número de la pizza: ")) - 1
        if 0 <= indice_pizza < len(pizzas_disponibles[tipo_pizza]):
            pizza_seleccionada = pizzas_disponibles[tipo_pizza][indice_pizza]
            tamaño_pizza = pizza_seleccionada["tamaño"]
            precio = pizza_seleccionada["precio"]
            
            descuento = obtener_descuento(tipo_cliente)
            precio_final = precio - (precio * descuento)
            
            venta = {
                "nombre_cliente": nombre_cliente,
                "tipo_cliente": tipo_cliente,
                "tipo_pizza": tipo_pizza,
                "tamano_pizza": tamaño_pizza,
                "nombre_pizza": pizza_seleccionada["nombre"],
                "precio": precio,
                "precio_final": precio_final
            }
            ventas.append(venta)
            print("Venta registrada con éxito.")
        else:
            print("Pizza seleccionada no valida")
    else:
        print("Tipo de pizza no válido. Intente de nuevo.")

# Función para mostrar todas las ventas
def mostrar_ventas():
    for venta in ventas:
        print(venta)

# Función para buscar ventas por cliente
def buscar_ventas_por_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    for venta in ventas_cliente:
        print(venta)

# Función para guardar las ventas en un archivo
def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file)
    print("Ventas guardadas en el archivo ventas.json")

# Función para cargar las ventas desde un archivo
def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")

# Función para generar factura
def generar_boleta():
    nombre_cliente = input("Ingrese el nombre del cliente que deseas realizar la boleta: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    if ventas_cliente:
        print(f"Boleta para {nombre_cliente}:")
        total = 0
        for venta in ventas_cliente:
            total += venta["precio_final"]
            print(f"\n\n----------------------------------------------------------------------\n\t\tBoleta pizzeria - DUOC UC\n----------------------------------------------------------------------\nFecha y hora: {datetime.datetime.now()}\tCliente: {nombre_cliente}\n----------------------------------------------------------------------\nTipo de pizza: {venta["tipo_pizza"]}\t\t\tPrecio: {venta["precio"]}\n----------------------------------------------------------------------\n\nTotal a pagar: {total}\n----------------------------------------------------------------------\n\t\t¡Gracias por su compra!")
    else:
        print("No se encontraron ventas para este cliente.")

# Función para obtener el descuento según el tipo de cliente
def obtener_descuento(tipo_cliente):
    if tipo_cliente == "diurno":
        return 0.12
    elif tipo_cliente == "vespertino":
        return 0.14
    elif tipo_cliente == "administrativo":
        return 0.10
    else:
        return 0.0

def anular_venta():
    nombre_cliente = input("Ingrese el nombre del cliente que deseas realizar la anulación: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    if ventas_cliente:
        total = 0
        for venta in ventas_cliente:
            total += venta["precio_final"]
        if total == 0:
            print("No tienes compras para anular.")
        elif total > 1:
            total = 0
            return print("Su compra a sido anulada.")
    else:
        print("No se encontraron ventas para este cliente.")

# Menú interactivo
def menu():
    while True:
        print("Sistema de ventas de pizzas - DUOC UC\n[1] Registrar venta\n[2] Mostrar venta\n[3] Buscar venta por cliente\n[4] Guardar ventas en un archivo\n[5] Cargar las ventas desde un archivo\n[6] Generar boleta\n[7] Anular venta\n[8] Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            buscar_ventas_por_cliente()
        elif opcion == "4":
            guardar_ventas()
        elif opcion == "5":
            cargar_ventas()
        elif opcion == "6":
            generar_boleta()
        elif opcion == "7":
            anular_venta()
        elif opcion == "8":
            print("Gracias por usar el sistema de ventas.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
# Ejecutar el menú
menu()
