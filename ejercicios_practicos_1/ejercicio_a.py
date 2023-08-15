#a) Diferencia de porcentaje entre el curso actual (1.5h) y
# - el mas rapido de otros cursos (2.5h)
# - el mas lento de otros cursos (7h)
# - el promedio de los cursos (4h)

curso_rapido = 2.5
curso_intermedio = 4
curso_lento = 7
curso_actual = 1.5


# diferencia de porcentaje con el curso mas rapido
diferencia_rapido = 100-(100*curso_actual)/curso_rapido

# diferencia de porcentaje con el curso intermedio
diferencia_intermedio = 100-(100*curso_actual)/curso_intermedio

# diferencia de porcentaje con el curso mas lento
diferencia_lento = 100-(100*curso_actual)/curso_lento

print(f"Este curso dura un {diferencia_rapido}% menos que el mas rapido")
print(f"Este curso dura un {diferencia_intermedio}% menos que el intermedio")
print(f"Este curso dura un {diferencia_lento:.2f}% menos que el mas lento")


