def amiga(a, b):
    if(len(a) == len(b)):
        total = len(a)
        parcial = 0
        for i in range(total):
            if(a[i] == b[i]):
                parcial += 1
        parece = parcial/total
        if((1 - parece) < 0.1):
            print("São amigas")
        else:
            print("Não são amigas")
            print("Diferem em: ", (1 - parece))
        return
    else:
        print("As palavras precisam ter o mesmo comprimento")
        return

a = "otorrinolaringolista"
b = "otorrinolaringolismo"

amiga(a, b)

