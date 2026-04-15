import turtle

turtle.speed(75)

# Draw a square
turtle.color("blue")
for i in range(0,100):
    turtle.forward(i * 2)
    turtle.left(90)

turtle.penup()
turtle.goto(200,-200)

# Draw a triangle
turtle.color("red")
turtle.pendown()
turtle.begin_fill()

for i in range(0,100):
    turtle.forward(i * 2)
    turtle.left(120)

turtle.end_fill()
turtle.penup()
turtle.goto(-200,200)

# Draw a octagon
turtle.pencolor("green")
turtle.fillcolor("darkorchid")
turtle.pendown()

for i in range(0,50):
    turtle.forward(i * 2)
    turtle.left(45)


turtle.done()