def natLog(precision):
    e = 0
    for i in range(precision):
        fatorial = 1
        while(i > 0):
            fatorial *= i
            i -= 1
        e += 1/fatorial
    return e

print(natLog(10000))