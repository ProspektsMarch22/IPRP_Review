def somaParesImpares(lista):
    somaPares = 0
    somaImpares = 0
    for num in lista:
        if(num % 2 == 0):
            somaPares += num
        else:
            somaImpares += num
    somas = (somaPares, somaImpares)
    return somas

if __name__ == "__main__":
    lista = [1, 4, 7, 9, 3, 2, 8, 5, 6]
    print(somaParesImpares(lista))