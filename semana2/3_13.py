def rancaVogal(name):
    vogais = 'aeiou'
    for a in name:
        if(vogais.find(a) >= 0):
            name = name.replace(a, " ")
    return name

nome = "isaac"
print(nome)
print(rancaVogal(nome))
