import math

def compEscada(alt, ang):
    rad = ang *(math.pi/180)
    comp = alt/math.sin(rad)
    return comp

print("%5.3f" % (compEscada(10, 45)))
