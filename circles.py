import turtle
t = turtle.Turtle()
colors = ['red', 'blue', 'yellow', 'green', 'red', 'blue']
t.speed(20) 
for i in range(36):
    t.penup()
    t.forward(200)
    for n in range(6):
        t.color(colors[n])
        t.pendown()
        t.circle(5)
        t.penup()
        t.forward(-20)
    t.forward(-80)
    t.right(10)
        
turtle.done()
