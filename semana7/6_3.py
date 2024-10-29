def alternaElementos(lst1, lst2):
    #assumindo que as duas listas tenham a mesma quantidade de elementos
    alterna = []
    for i in range(len(lst1)):
        alterna.append(lst1[i])
        alterna.append(lst2[i])
    return alterna

if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = ['a', 'b', 'c']
    print(alternaElementos(l1, l2))