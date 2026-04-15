from turtle import *

speed(20)
right(30)

def sierpinski(length, depth, type):
    if depth == 0:
        for i in range(0,3):
            if type != 2:
                forward(length)
                left(120)
            else:
                stamp()
                ht()
    elif type == 1:
        # Best value (200,4,1)
        sierpinski(length / 2, depth - 1, type)
        forward(length / 2)
        sierpinski(length / 2, depth - 1, type)
        backward(length/ 2)
        left(60)
        forward(length / 2)
        right(60)
        sierpinski(length / 2, depth - 1, type)
        left(60)
        backward(length / 2)
        right(60)
    elif type == 2:
        # Best value (100, 4, 2)
        penup()
        shape("triangle")
        for i in range(0,3):
            forward(length)
            sierpinski(length / 2, depth - 1, type)
            backward(length)
            left(120)       
    else:
        # Best value (80,5,0)
        for i in range(0,3):
            forward(length)
            sierpinski(length / 2, depth - 1, type)
            backward(length)
            left(120)

sierpinski(100, 4, 2)
done()