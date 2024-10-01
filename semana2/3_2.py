def triangleHeron(a, b, c):
    s = (a + b + c)/2
    area = (s * (s - a) * (s - b) * (s - c))**(1/2)
    return area

print(triangleHeron(3, 4, 5))