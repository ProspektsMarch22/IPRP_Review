def prefixos(cadeia):
    i = 0
    while(i <= len(cadeia)):
        print(cadeia[:i])
        i += 1

prefixos('Monty Python')