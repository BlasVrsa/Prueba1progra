# Solicitando al usuario que ingrese un número entero positivo mayor que 1
numero = int(input("Por favor, introduce un número entero positivo mayor que 1: "))

# Asumimos que el número es primo hasta demostrar lo contrario
es_primo = True

# Verificando si el número es primo
if numero <= 1:
    es_primo = False
else:
    # Iterando desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            es_primo = False
            break

# Imprimiendo el resultado
if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")