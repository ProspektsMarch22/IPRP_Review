def numeroCrit(lista, crit):
    novaLista = []
    for idade in lista:
        if(idade < crit):
            novaLista.append(idade)
    return len(novaLista)

if __name__ == "__main__":
    print(numeroCrit([2, 8, 6, 5, 3, 2], 5))
    