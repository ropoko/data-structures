import turtle
def shape():
    window = turtle.Screen()
    window.bgcolor("white")
    
    asdf = turtle.Turtle()
    asdf.shape("turtle")
    
    asdf.speed(20000)
    for j in range(120):
        asdf.color("gray")
        for i in range(5):
            asdf.forward(50)
            asdf.right(90)
        asdf.right(1)
    for j in range(120):
        asdf.color("black")
        for i in range(5):
            asdf.forward(70)
            asdf.right(180)
        asdf.right(1)
    for j in range(120):
        asdf.color("yellow")
        for i in range(5):
            asdf.forward(100)
            asdf.right(180)
        asdf.right(1)
    window.exitonclick()
shape()