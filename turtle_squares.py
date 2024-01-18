import turtle
t = turtle.Turtle()

def square(s):
    for i in range(4):
        t.forward(s)
        t.left(90)

square(100)
t.forward(100)
square(200)
t.forward(200)
square(400)
