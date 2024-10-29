#Assumindo que o programa receba apenas números de 100 a 999

def somaNúmeros():
    numero = input()
    soma = 0
    for a in numero:
        a = int(a)
        soma += a
    if(soma % 2 == 0):
        print(True)
    else:
        print(False)

somaNúmeros()