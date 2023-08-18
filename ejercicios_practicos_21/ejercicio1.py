# Falto el profesor, por lo que se debe elegir a un alumno para que sea el profesor y a otro para que sea el asistente

# Pedir la edad y el nombre de los compañeros que fueron a la clase, para luego determinar que el mas joven sea el asistente y el mas viejo sea el profesor

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    # ordena la lista de tuplas de menor a mayor segun la edad, por eso [1]
    compañeros.sort(key=lambda x : x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    # devuelve una tupla
    return asistente,profesor

# llamamos a la funcion con 2 variables, asi podemos desempaquetar la tupla
asistente, profesor = obtener_compañeros(5)

print(f"El profesor es {profesor} y el asistente es {asistente}")
    