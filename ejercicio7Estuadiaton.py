import random

# La computadora "piensa" en un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
print(numero_secreto)
# Inicializamos la variable para el número que introduce el usuario
numero_usuario = 0

# Bucle mientras el usuario no adivine el número
while numero_usuario != numero_secreto:
    # Solicitamos al usuario que ingrese un número
    numero_usuario = int(input("Introduce un número entre 1 y 100: "))
    
    # Comprobamos si el número es el correcto o proporcionamos una pista
    if numero_usuario < numero_secreto:
        print("Más alto. Intenta con un número mayor.")
    elif numero_usuario > numero_secreto:
        print("Más bajo. Intenta con un número menor.")

# Cuando el usuario adivina el número, se sale del bucle
print(f"¡Felicidades! Has adivinado el número, era {numero_secreto}.")