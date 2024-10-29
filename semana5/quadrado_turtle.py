import turtle
"""
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
"""
"""
def quadrado(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
"""

def quadrado(lado, x_cor, y_cor, angulo):
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.setheading(angulo)
    turtle.pendown()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()

def triangulo(lado, x_cor, y_cor, angulo):
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.setheading(angulo)
    turtle.pendown()
    for i in range(3):
        turtle.forward(lado)
        turtle.right(120)
    turtle.hideturtle()

def pentagono(lado, x_cor, y_cor, angulo):
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.setheading(angulo)
    turtle.pendown()
    for i in range(5):
        turtle.forward(lado)
        turtle.right(72)
    turtle.hideturtle()



quadrado(200, 40, 0, 45)
triangulo(150, -100, 0, 0)
pentagono(80, -200, -10, 78)

turtle.exitonclick()