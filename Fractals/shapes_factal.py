from turtle import * # Import the turtle module

speed(10)
ht()
fillcolor("darkslategray1")

def polygon(sides, side_length, richardson, t_right, t_left, t_forward):
    begin_fill()
    for i in range(0,sides):
        forward(side_length)
        left(360 / sides)
    end_fill()

    if side_length > richardson:
        right(t_right)
        left(t_left)
        forward(t_forward)
        polygon(sides, side_length - 1, richardson, t_right, t_left, t_forward)

# sides, length, loop,right,left,forward
polygon(6, 100, 0,3,0,6)
done()

