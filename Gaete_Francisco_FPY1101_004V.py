import random
import time

# Función para generar los 10 sueldos aleatorios (según el conteo de trabajadores en la lista)
def generar_sueldos(a):
    sueldos = []
    for i in range(a):
        sueldos.append(random.randint(300000, 2500000))
    return sueldos

# Función para clasificar sueldos
def clasificar_y_mostrar_sueldos(trabajadores, sueldos):
    menores_800k = []
    entre_800k_2M = []
    mayores_2M = []

    for empleado, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            menores_800k.append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2M.append((empleado, sueldo))
        else:
            mayores_2M.append((empleado, sueldo))
    
    total_sueldos = sum(sueldos)
    
    print("Sueldos menores a $800.000 Cantidad:", len(menores_800k))
    print("Nombre empleado\tSueldo")
    for empleado, sueldo in menores_800k:
        print(f"{empleado}\t${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000 Cantidad:", len(entre_800k_2M))
    print("Nombre empleado\tSueldo")
    for empleado, sueldo in entre_800k_2M:
        print(f"{empleado}\t${sueldo}")

    print("\nSueldos superiores a $2.000.000 Cantidad:", len(mayores_2M))
    print("Nombre empleado\tSueldo")
    for empleado, sueldo in mayores_2M:
        print(f"{empleado}\t${sueldo}")

    print("\nTOTAL SUELDOS: $", total_sueldos)

# Función para ver estadísticas y utilizamos la función sqrt para disminuir decimales del resultado
def ver_estadisticas(sueldos):
    sueldo_alto = max(sueldos)
    sueldo_bajo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica = (sueldo_alto * sueldo_bajo) ** 0.5
    
    print(f"Sueldo más alto: ${sueldo_alto}")
    print(f"Sueldo más bajo: ${sueldo_bajo}")
    print(f"Promedio de sueldos: ${promedio}")
    print(f"Media geométrica: ${media_geometrica:.0f}")

# Función para mostrar y exportar reporte de sueldos
def reporte_sueldos(trabajadores, sueldos):
    print("Nombre empleado\tSueldo Base \tDescuento Salud \tDescuento AFP \tSueldo Líquido\n")
    
    with open('reporte_sueldos.csv', 'w') as file:
        file.write('Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido\n')
        
        for empleado, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            #No pude alinear esto :C
            print(f"{empleado}      ${sueldo}          ${descuento_salud:.0f}                       ${descuento_afp:.0f}         ${sueldo_liquido:.0f}")
            
            file.write(f"{empleado},{sueldo},{descuento_salud},{descuento_afp},{sueldo_liquido}\n")

# Menú interactivo
def menu():
    trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]  
    sueldos = generar_sueldos(len(trabajadores))
    
    while True:
        print("\nMenú:")
        print("1. Generar sueldos aleatorios")
        print("2. Clasificar y mostrar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sueldos = generar_sueldos(len(trabajadores))
            print("Sueldos generados:")
            print(sueldos)
        elif opcion == '2':
            clasificar_y_mostrar_sueldos(trabajadores, sueldos)
        elif opcion == '3':
            ver_estadisticas(sueldos)
        elif opcion == '4':
            reporte_sueldos(trabajadores, sueldos)
            print("Reporte de sueldos exportado a 'reporte_sueldos.csv'.")
        elif opcion == '5':
            print("Desarrollado por Francisco Gaete")
            print("RUT 22.086.627-0")
            print("Finalizando programa...")
            time.sleep(2)
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
menu()