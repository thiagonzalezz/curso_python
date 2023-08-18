# Crear una funcion la cual al pasarle un numero nos genere numeros primos hasta llegar a ese numero


# Primero hacemos una funcion para determinar si cierto numero es primo o no
def primos(num):
    for i in range(2,num-1):
        if (num % i == 0):
            return False
    return True

# Reutilizamos la funcion anterior agregandole un ciclo for para asi poder hacer una lista con todos los numeros primos desde el 1 hasta el numero ingresado
def primos_iterativo(num):
    lista = []
    for i in range(1, num+1):
        if primos(i):
            lista.append(i)
    return lista

lista = primos_iterativo(7);
print(lista)