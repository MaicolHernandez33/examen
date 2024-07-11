
import random
import statistics
import csv


trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez",
                "Pedro Rodríguez","Laura Hernández","Miguel Sánchez",
                "Isabel Gómez","Francisco Díaz","Elena Fernández"]


def AsignarSueldosAleatorios ():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000,2500000)
        sueldos.append(sueldo)
    return sueldos

def ClasificarSueldos (sueldos):
    SueldosBajos = []
    SueldosMedios = []
    SueldosAltos = []

    for i, sueldo in enumerate(sueldos):
        NombreEmpleado = trabajadores [i]
        if sueldo < 800000:
            SueldosBajos.append((NombreEmpleado,sueldo))
        elif sueldo>= 800000 and sueldo <=2000000:
            SueldosMedios.append((NombreEmpleado,sueldo))
        else:
            SueldosAltos.append((NombreEmpleado,sueldo))

    print("Sueldos menores a $800.000 ")
    print(f"TOTAL: {len(SueldosBajos)}")
    for empleado, sueldo in SueldosBajos:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000 ")
    print(f"TOTAL: {len(SueldosMedios)}")
    for empleado, sueldo in SueldosMedios:
        print(f"{empleado}: ${sueldo}")

    print("Sueldos mayores a $2.000.000 ")
    print(f"TOTAL: {len(SueldosAltos)}")
    for empleado, sueldo in SueldosAltos:
        print(f"{empleado}: ${sueldo}")
    
    totalSueldos = sum(sueldo for _, sueldo in sueldos)
    print(f"Total Sueldos: ${totalSueldos}")
    

def VerEstadisticas (sueldos):
    SueldoMasAlto = max(sueldos)
    SueldoMasBajo = min(sueldos)
    PromedioSueldos = statistics.mean(sueldos)

    if len(sueldos) >0:
        MediaGeometrica = statistics.geometric_mean(sueldos)
    else:
        MediaGeometrica = 0

    print(f"Sueldo más Alto: ${SueldoMasAlto}")
    print(f"Sueldo más Bajo: ${SueldoMasBajo}")
    print(f"Promedio de Sueldos: ${PromedioSueldos:.2f}")
    print(f"Media Geométrica de Sueldos: ${MediaGeometrica:.2f}")


def ReporteSueldos(sueldos):
    with open ('ReporteSueldos.csv', mode='w',newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter= ',')

        writer.writerow(['Nombre Empleado','Sueldo','Descuento Salud','Descuento AFP','Sueldo Líquido'])

        for i, sueldo in enumerate(sueldos):
            nombre_empleado = trabajadores[i]
            descuento_salud = sueldo *0.07
            descuento_afp = sueldo*0.12
            sueldo_liquido = sueldo-descuento_afp-descuento_salud

            writer.writerow([nombre_empleado,sueldo,descuento_salud,descuento_afp,sueldo_liquido])



def main ():
    sueldos = AsignarSueldosAleatorios()
    while True:
        try:
            print("\n**** Bienvenidos al análisis de sueldo de trabajadores ****\n")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")

            opcion = input("\nIngrese una opcion del 1 al 5: ")

            if opcion == '1':
                sueldos=AsignarSueldosAleatorios()
                print("\n** Sueldos Asignados Correctamente **\n")
            elif opcion == '2':
                ClasificarSueldos(sueldos)
            elif opcion == '3':
                VerEstadisticas(sueldos)
            elif opcion == '4':
                ReporteSueldos(sueldos)
                print("Reporte de sueldos generado en 'ReporteSueldos.csv'")
            elif opcion == '5':
                print("\n\n Finalizando programa…\n Desarrollado por Maicol Hernández\n RUT 20.064.761-0")
            else:
                print("Ingrese una opcion del 1 al 5")

        except:
            print("Error, ingrese la opción nuevamente")

if __name__ == "__main__":
    main()

        