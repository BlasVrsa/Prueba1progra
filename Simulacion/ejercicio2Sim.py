numeros = [15, 22, 8, 34, 12, 29, 40]

promedio = sum(numeros) / len(numeros)
#print("Promedio: ", promedio)

mayores_que_promedio = []

for numero in numeros:
    if(numero > promedio):
        mayores_que_promedio.append(promedio)

print("Numeros mayores que el promedio: ", mayores_que_promedio)