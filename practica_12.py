def procesar():
    cant_estudiante=0 
    aprobados=0
    reprobados=0
    femenino=0
    masculino=0
    while True:
        sexo=input("Ingresa tu sexo F/M")
        cant_estudiante=cant_estudiante+1
        print("Ingresa la nota")
        nota=int(input())
        if nota>=80:
            aprobados=aprobados+1
        if nota<80:
            reprobados=reprobados+1
        if sexo=="F":
            femenino=femenino+1
        if sexo=="M":
            masculino=masculino+1
        resp=input("Presiona espacio para detener el procesamiento")
        if resp==" ":
            break

    print(f"Cantidad de aprobadpos {aprobados} y reprobados fueron {reprobados}")
    return cant_estudiante, aprobados, reprobados, masculino, femenino

def calcularporc(contadorg, contadore):
    if contadorg>0:
        porcentaje=contadore/contadorg*100
    else:
        porcentaje=0
    return porcentaje

def calcular(cant_estudiante, aprobados, reprobados, masculino, femenino):
    porc_aprobados=calcularporc(cant_estudiante,aprobados)
    porc_reprobados=calcularporc(cant_estudiante, reprobados)
    porcentajeM=calcularporc(cant_estudiante, masculino)
    porcentajeF=calcularporc(cant_estudiante, femenino)
    return porc_aprobados, porc_reprobados, porcentajeM, porcentajeF
def mostrar(cant_estudiante, aprobados, reprobados, porc_aprob, porc_reprob, masculino, femenino ):
    print(f"El porcentaje de aprobados de la seccion es {porc_aprob}")
    print(f"El porcentaje de reprobados de la seccion es {porc_reprob}")
    print(f"El porcentaje de aprobados masculinos es {porcentajeM}")
    print(f"El porcentaje de aprobados femeninos es {porcentajeF}")

cant_estudiante, aprobados,reprobados, masculino, femenino=procesar()
porc_aprob, porc_reprob, porcentajeF, porcentajeM=calcular(cant_estudiante,aprobados, reprobados, masculino, femenino)
mostrar(cant_estudiante, aprobados, reprobados, porc_aprob, porc_reprob, masculino, femenino )

