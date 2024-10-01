import math

def convertCoord(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.acos(x/r)
    polar = (r, theta)
    return polar

cartesiana = (1, 1)
polar = convertCoord(cartesiana[0], cartesiana[1])
print(polar)
