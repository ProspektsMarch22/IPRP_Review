import random

def temDadoEmCasa(n):
    pares = 0
    for i in range(n):
        face = random.randint(1, 6)
        if(face % 2 == 0):
            pares += 1
    percent = pares/n
    return percent

print("{0:.4f}".format(temDadoEmCasa(10000000)))
