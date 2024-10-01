def sufixo(cadeia):
    i = (len(cadeia) - 1)
    while(i >= 0):
        print(cadeia[i:len(cadeia)])
        i -= 1

sufixo("Monty Python")