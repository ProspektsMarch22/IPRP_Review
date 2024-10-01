def areaQuadrado(lado):
    area = pow(lado, 2)
    return area

def areaCircunferencia(diametro):
    area = 3.14*(pow((diametro/2), 2))
    return area

burguerA = areaQuadrado(7.62)
burguerB = areaCircunferencia(8.89)

print(f"Area antiga era {burguerA}")
print(f"Area nova: {burguerB}")