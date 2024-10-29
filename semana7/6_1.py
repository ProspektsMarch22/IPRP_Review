def numeroIdades(lista):
    numero = len(lista)
    print(numero)
    return

def exibeIdades(lista):
    for idade in lista:
        print(idade)
    return

def exibeIdadesInversa(lista):
    lista.reverse()
    exibeIdades(lista)

def exibeIdadesException(lista):
    lista.pop(0)
    lista.pop()
    exibeIdades(lista)

def somaValoresLista(lista):
    soma = 0
    for idade in lista:
        soma += idade
    print(soma)
    return

def numeroIdadesCrit(lista, crit):
    novaLista = []
    for idade in lista:
        if(idade < crit):
            novaLista.append(idade)
    numeroIdades(novaLista)

def existeDezessete(lista):
    if(lista.count(17) > 0):
        return True
    return False

if __name__ == '__main__':
    lista = [11, 12, 13, 14, 15, 16, 17]

    #numeroIdades(lista)
    #exibeIdades(lista)
    #exibeIdadesInversa(lista)
    #somaValoresLista(lista)
    #numeroIdadesCrit(lista, 15)
    exibeIdadesException(lista)
    print(existeDezessete(lista))
    