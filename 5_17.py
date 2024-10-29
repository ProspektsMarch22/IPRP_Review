def padraoA(n):
    for i in range(1, n+1):
        j = 1
        while(j < i):
            print(j, end=" ")
            j += 1
        print(i)

padraoA(10)

print()

def padraoB(n):
    while(n > 0):
        j = 1
        while(j < n):
            print(j, end=" ")
            j += 1
        print(j)
        n -= 1

padraoB(10)

print()

def padraoC(n):
    """
    print("{:>10}".format(1))
    print("{:>8}".format(2), "{:>1}".format(1))
    print("{:>6}".format(3), "{:>1}".format(2), "{:>1}".format(1))
    
    """
    decrement = 0
    for i in range(1, n + 1):
        j = i
        print("{:>{}}".format(j, ((n*2) - decrement)), end = " ")
        j -= 1
        while(j > 0):
            print("{:>1}".format(j), end =" ")
            j -= 1
        print("")
        decrement += 2

padraoC(10)