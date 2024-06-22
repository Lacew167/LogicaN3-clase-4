#contadores acumuladores de la seccion (generales)
acumulador_notas_seccion=0
contador_notas_seccion=0 #totalidad de notas de la seccion
notas_aprobadas_seccion=0 #totalidad de notas aprobadas de la seccion
for i in range(1,4):
    print(".......................................")
    print(f"Datos de cada entidad, que son unicos {i}")
    cedula=input("Ingresa la cedula del estudiante")
    nombre=input("Como se llama el estudiante?")
    print(f"Estudiante: {nombre} CI {cedula}" )
    #contador, acumulador por cada entidad ()
    sumatoria=0
    cant_notas_seccion=0
    while True:
        cant_notas=cant_notas+1
        print("")
        print("Datos que representa una serie de valores")
        nota=int(input("Ingresa la nota"))
        sumatoria=sumatoria+nota
        if nota>10:
            notas_aprobadas_seccion=notas_aprobadas_seccion+1
        print("...........................")
        resp=input("Presione espacio para detener")
        if resp==" ":
            break
    print(f"Acumulo {sumatoria} de {cant_notas}")
    acumulador_notas_seccion=acumulador_notas_seccion+sumatoria
    contador_notas_seccion=contador_notas_seccion+cant_notas
    print(f"Se lleva acumulado {acumulador_notas_seccion}")
    print(f"de {contador_notas_seccion} notas ")
    print()
    print("***************************")
