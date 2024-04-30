# Lista para almacenar las palabras
palabras = []

# Solicitando al usuario que ingrese tres palabras
for i in range(3):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Calculando la puntuación total
puntuacion_total = 0

for palabra in palabras:
    if len(palabra) <= 3:
        # 1 punto por cada carácter si la palabra tiene 3 o menos caracteres
        puntuacion_total += len(palabra)
    else:
        # 2 puntos por cada carácter si la palabra tiene más de 3 caracteres
        puntuacion_total += len(palabra) * 2

# Imprimiendo la puntuación total
print(f"La puntuación total de todas las palabras ingresadas es: {puntuacion_total}")