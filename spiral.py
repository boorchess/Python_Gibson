import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.color('yellow')
repeat = 0
for i in range(300):
    repeat = repeat + 5
    t.forward(repeat)
    t.left(90)
    
