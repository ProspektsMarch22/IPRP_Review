def acronimo(cadeia):
    sigla = ""
    for char in cadeia:
        if(ord(char) >= 65 and ord(char) <= 90):
            sigla += char
    return sigla

print(acronimo("Random Access Memory"))
print(acronimo("Introdução à Programação e Resolução de Problemas"))