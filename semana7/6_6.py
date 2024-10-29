def somaCumulativa(lista):
    cumula = []
    cumula.append(lista[0])
    i = 1
    while(i < len(lista)):
        cumula.append(lista[i] + cumula[i - 1])
        i += 1
    return cumula

if __name__ == "__main__":
    lst = [1, 2, 3]
    print(somaCumulativa(lst))
