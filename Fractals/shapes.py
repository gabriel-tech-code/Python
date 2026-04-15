import turtle

# Draw a square
turtle.color("blue")
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(150,0)

# Draw a triangle
turtle.color("red")
turtle.pendown()
turtle.begin_fill()
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,0)

# Draw a circle
turtle.pencolor("green")
turtle.fillcolor("darkorchid")
turtle.begin_fill()
turtle.pendown()
turtle.circle(50)
turtle.end_fill()

turtle.done()