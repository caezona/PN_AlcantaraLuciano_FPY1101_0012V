import random
import csv

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos aleatorios asignados correctamente.")

def clasificar_sueldos():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    sueldos_bajos = []
    sueldos_intermedios = []
    sueldos_altos = []

    for i, trabajador in enumerate(trabajadores):
        sueldo = sueldos[i]
        if sueldo < 800000:
            sueldos_bajos.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            sueldos_intermedios.append((trabajador, sueldo))
        elif sueldo > 2000000:
            sueldos_altos.append((trabajador, sueldo))
    
    total_sueldos = sum(sueldos)

    print("\nSueldos menores a $800.000")
    print(f"TOTAL: {len(sueldos_bajos)}")
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in sueldos_bajos:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(sueldos_intermedios)}")
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in sueldos_intermedios:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(sueldos_altos)}")
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in sueldos_altos:
        print(f"{nombre}\t${sueldo}")

    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def ver_estadisticas():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    producto = 1
    for sueldo in sueldos:
        producto *= sueldo
    media_geometrica = producto ** (1 / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica: ${media_geometrica:.2f}")

def generar_reporte():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    with open('reporte_sueldos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Empleado', 'Sueldo', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        
        for i, trabajador in enumerate(trabajadores):
            sueldo_base = sueldos[i]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp

            writer.writerow([trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("Reporte generado exitosamente en 'reporte_sueldos.csv'.")

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
        elif opcion == '5':
            print("¡Programa finalizado!")
            print("Desarrollado por Luciano Alcántara")
            print("RUT 22.002.535-7")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
