def tabuada(x):
    if (x <= 10 and x > 0):
        print("Tabuada do número {0}".format(x))
        print("{0:^}".format("-"*15))
        for i in range(1, 11):
            print("{0} x   {1:>3} = {2:>3}".format(x, i, x*i))

tabuada(7)