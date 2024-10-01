import math

def desordem(n, m):
    pN = n/(n+m)
    pM = m/(n+m)
    h = (-1) * (pN*(math.log2(pN)) + pM*(math.log2(pM)))
    return h

n = 30
m = 70
print("%1.5f" % desordem(n, m))