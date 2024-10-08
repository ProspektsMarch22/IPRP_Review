alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def codificar(cadeia, parametro):
    for a in cadeia:
        if(alfabeto.find(a) >= 0):
            indice = alfabeto.find(a)
            if((indice + parametro) > len(alfabeto)):
                indice = indice - 26
            elif((indice + parametro) < 0):
                indice = indice + 26
            cadeia = cadeia.replace(a, alfabeto[indice + parametro])
    return cadeia

teste = "zzz"
print(teste)
print(codificar(teste, 2))
codificado = codificar(teste, 2)

def decodificar(cadeia, parametro):
    for a in cadeia:
        if(alfabeto.find(a) >= 0):
            indice = alfabeto.find(a)
            if((indice + parametro) > len(alfabeto)):
                indice = indice - 26
            elif((indice + parametro) < 0):
                indice = indice + 26
            cadeia = cadeia.replace(a, alfabeto[indice - parametro])
    return cadeia

print(codificado)
print(decodificar(codificado, 2))