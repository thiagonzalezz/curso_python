# a) Pedirle al usuario que diga cualquier texto real y :
# - calcular cuanto tardaria en decir esa frase, considerando que cada persona promedio habla 2 palabras por segundo
# - ¿cuantas palabras dijo?

# b) Si se tarda mas de un minuto:
# - decirle "para flaco tampoco te pedi un testamento."

# c) Pepito habla un 30% mas rapido, ¿cuanto tardaria en decirlo?

# pedimos que ingrese el texto
texto_usuario = input("Ingrese un texto: ")

# cantidad de palabras que tiene el texto ingresado, donde split nos separa la cadena en una lista con cada palabra, y len nos devuelve la cantidad de elementos de esa lista ['hola', 'soy', 'yo']
cantidad_palabras = len(texto_usuario.split())

# cuanto tardaria en decir la frase ingresada por el usuario
tiempo_usuario = cantidad_palabras/2

print(f"El usuario tardaria en decir la frase, {tiempo_usuario:.2f} segundos")
print(f"La cantidad total de palabras dichas es de {cantidad_palabras} palabras")


# condicion si el usuario tarda mas de 60 segundos
if (tiempo_usuario>60):
    print("para flaco tampoco te pedi un testamento.")
    

# Como pepito habla un 30% mas rapido, significa que tarda 0.7 segundos en decir 2 palabras, por lo tanto el tiempo que tardaria pepito en decir la frase:

tiempo_pepito = (cantidad_palabras*0.7)/2

print(f"Pepito tardaria {tiempo_pepito} segundos en decir la frase")

