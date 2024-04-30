# Solicitando la frase y la letra al usuario
frase = input("Por favor, introduce una frase: ")
letra = input("Ahora, introduce una letra para contar su aparición en la frase: ")

# Contando las apariciones de la letra en la frase
conteo = frase.count(letra)

# Imprimiendo el resultado
print(f"La letra '{letra}' aparece {conteo} veces en la frase.")