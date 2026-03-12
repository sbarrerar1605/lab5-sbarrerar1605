def promedio_estudiante(calificaciones):

    if len(calificaciones) == 0:
        return 0.0

    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)

    return float(promedio)