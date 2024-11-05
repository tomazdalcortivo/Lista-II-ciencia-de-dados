from random import randint

NUMERO_ALEATORIO = randint(1, 100)

find = True 
while find:

    num = int(input("Consegue descobrir o numero aleatorio? "))

    if NUMERO_ALEATORIO == num: 
        find = False
        print("Parabens! Você encontrou!")
    elif num < NUMERO_ALEATORIO:
        print("Tente um numero maior")
    else:
        print("Tente um numero menor")        