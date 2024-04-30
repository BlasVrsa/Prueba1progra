# Declarando las variables enteras
a = 5
b = 5

# Verificando si son iguales
if(a == b):
    print("Son iguales")
else:
    print("Son distintos")

# Solicitando el nombre y la edad del usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

# Comprobando si el usuario es mayor de edad
if edad >= 18:
    print(f"{nombre}, eres mayor de edad.")
else:
    print(f"{nombre}, no eres mayor de edad.")