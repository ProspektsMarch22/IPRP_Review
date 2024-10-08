def pontoMedio(k, p):
    medio = (k + p)/2
    return medio

def polyTeste(x):
    y = x**3 - x - 1
    return y

def bissection(k, p):
    while(polyTeste(k) * polyTeste(p) < 0):
        x = pontoMedio(k, p)
        if(int(polyTeste(x)) == 0):
            break
        else:
            if(polyTeste(x) * polyTeste(p) < 0):
                k = x
                continue
            else:
                p = x
                continue
    return x

print(bissection(0.5, 2.0))