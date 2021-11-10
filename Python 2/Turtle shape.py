import turtle

turtle.speed(100)
turtle.bgcolor("white")

for i in range(5):
    for colors in ["red","cyan","green","orange","blue","Lime","Lightblue"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.lt(12)
        for i in range(4):
            turtle.fd(200)
            turtle.lt(90)
turtle.done()
