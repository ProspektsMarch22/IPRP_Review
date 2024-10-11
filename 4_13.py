def kmToMiles(a, b):
    print("{0:<15s}{1:<15s}".format("Milhas", "Quilómetros"))
    print("{0:^30s}".format("-"*30))
    for i in range(a, b):
        print("{0:<15.2f}{1:^15.2f}".format(a, a*1.609))
        a+=1

kmToMiles(10, 20)