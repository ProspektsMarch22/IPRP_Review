def subCadeia(cadeia, indice):
    i = 0
    while(len(cadeia) - i >= indice):
        print(cadeia[i:(i+indice)])
        i += 1

cadeia = 'Monty Python'
subCadeia(cadeia, 3)