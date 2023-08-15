# b) Porcentaje de material inservible que se reduce en:
# - el promedio de los cursos (5h a 3.5h)
# - el curso actual (este curso 3.5h a 1.5)

crudo_otros_cursos = 5
final_otros_cursos = 4
crudo_curso_actual = 3.5
final_curso_actual = 1.5

# porcentaje de material inservible que se reduce en los otros cursos
material_inservible_otros_cursos =100-((100*final_otros_cursos)/crudo_otros_cursos)


# porcentaje de material inservible que se reduce en el curso actual
material_inservible_curso_actual =100-((100*final_curso_actual)/crudo_curso_actual)

print(f"Un curso promedio elimina un {material_inservible_otros_cursos}% de tiempo vacio")
print(f"Este curso elimina {material_inservible_curso_actual:.2f}% de tiempo vacio")