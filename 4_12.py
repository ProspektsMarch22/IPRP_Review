def quadrado(x):
    rep = 5
    print("{0:>15s}{1:>15s}".format("Número", "Quadrado"))
    for i in range(rep):
        print("{0:15d}{1:15d}".format(x, x**2))
        x += 1

quadrado(1)
