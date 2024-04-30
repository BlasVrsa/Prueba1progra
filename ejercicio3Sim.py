import random

dados = []

dados.sort()
print("Sus dados son: ", dados)

while True:
    # caso 1: Escalera real.
    escalera_real = 1
    for i in range(1, len(dados)):
        if dados[i]-1 != dados[i-1]:
            escalera_real = 0
    if escalera_real == 1:
        print("Su mano es una escalera real. Tiene 30 puntos.")
        break

    # caso 2: Escalera pequeña.
    if dados.count(1)<=1 and dados.count(2)<=1 and dados.count(3)<=1 and dados.count(4)<=1 and dados.count(5)<=1 and dados.count(6)<=1:
        print("Su mano es una escalera pequeña. tiene 20 puntos.")
        break

    # Hacer el resto de casos
    # caso 3: Full house
    # caso 4: Poker
    # caso 5: Escalera
    # caso 6: Triple
    # caso 7: Doble pareja
    # caso 8: Par
    # caso 9: Suma de los dados
 

