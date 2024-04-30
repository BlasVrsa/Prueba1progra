# Solicitando la frase y la letra al usuario
frase = input("Por favor, introduce una frase: ")
letra = input("Ahora, introduce una letra para contar su aparición en la frase: ")

# Contando las apariciones de la letra en la frase
conteo = frase.count(letra)

# Imprimiendo el resultado
print(f"La letra '{letra}' aparece {conteo} veces en la frase.")
print("La letra '", letra, "' aparece ", conteo, " veces en la frase.")


numeros = []

for i in range(3):
    numero = int(input("Ingrese el numero: "))
    numeros.append(numero)

numero_usuario = int(input("Que numero quieres ver si esta en la lista:"))

contador = numeros.count(numero_usuario)

print("el numero '",numero_usuario, "' aparece ", contador, " veces en la")