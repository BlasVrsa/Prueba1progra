import random

dados = []

for i in range(5):     
    dado = random.randint(1,6) 
    dados.append(dado)

total = sum(dados)

dados.sort()
print("Sus dados son: ", dados)

#Definimos variables globales que nos van a servir en varias jugadas

while True:
    # caso 1: Escalera real.
    # Posible mejora
    escalera_real = 1
    for i in range(1, len(dados)):
        if dados[i]-1 != dados[i-1]:
            escalera_real = 0
    if escalera_real == 1:
        print("Su mano es una escalera real. Tiene 30 puntos.")
        break

    #CASO 2 ESTA RARO PORQUE ES LO MISMO QUE ESCALERA O NO TENER NADA

    # caso 2: Escalera pequeña.
    if dados.count(1)<=1 and dados.count(2)<=1 and dados.count(3)<=1 and dados.count(4)<=1 and dados.count(5)<=1 and dados.count(6)<=1:
        print("Su mano es una escalera pequeña. tiene 20 puntos.")
        break

    # Hacer el resto de casos

    # caso 3: Full house

    full_house = False
    hay_3 = False
    hay_2 = False

    for valor in set(dados):
        if dados.count(valor) == 3:
            hay_3 = True
        elif dados.count(valor) == 2:
            hay_2 = True

        if(hay_2 and hay_3):
            print(f"Su mano es un Full House, Tiene {total} puntos" )
            break

    # caso 4: Poker
    poker = False
    hay_4 = False

    for valor in set(dados):
        if dados.count(valor) == 4:
            hay_4 = True
        if(hay_4):
            print(f"Su mano es un Poker, Tiene {total} puntos")
            break

    # caso 5: Escalera
    #DUDOSAAAA!!!

    # caso 6: Triple
    valor_triple = 0
    hay_3 = False
    for valor in set(dados):
        if dados.count(valor) == 3:
            hay_3 = True
            valor_triple = valor 
        if(hay_3):
            print(f"Su mano es un Triple de {valor}s. Tienes {(valor)*3} puntos")
            break

    # caso 7: Doble pareja
    pares = []
    for valor in set(dados):
        if dados.count(valor) == 2:
            pares.append(valor)
        if len(pares) == 2:
            print(f"Su mano tiene doble pareja: {pares[0]}s y {pares[1]}s. Tienes {(pares[0]*2) + pares[1]*2}")
            break

    # caso 8: Par
    
    if len(pares) == 1:
        print(f"Su mano es un par de {pares[0]}s. Tiene {pares[0]*2} puntos")
        break

    # caso 9: Suma de los dados
    # print(f"No obtuvo ninguna combinacion, Tiene {total} puntos")
    break

