import math

def volumeCone(r, h):
    volume = (math.pi*(r**2)*h)/3
    return volume

raio = 1
altura = 1
print(volumeCone(raio, altura))