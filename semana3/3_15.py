def prefixos(cadeia):
    i = 1
    while(i <= len(cadeia)):
        print(cadeia[:i])
        i += 1

prefixos('Monty Python')