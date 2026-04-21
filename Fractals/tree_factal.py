from turtle import *
from random import *

speed(60)
ht()
left(90)

def branch(branch_length, angle):
    if branch_length < 10:
        return
    else:
        forward(branch_length)
        left(angle)
        branch(0.7 * branch_length, angle)
        right(angle * 2)
        branch(0.7 * branch_length, angle)
        left(angle)
        backward(branch_length)

def branch_1(branch_length, angle):
    angle = randint(15, 45)
    if branch_length < 10:
        return
    else:
        forward(branch_length)
        left(angle)
        branch_1(0.7 * branch_length, angle)
        right(angle * 2)
        branch_1(0.7 * branch_length, angle)
        left(angle)
        backward(branch_length)

def branch_2(branch_length, angle):
    shrink_factor = uniform(0.3, 0.9)
    angle = randint(15, 45)
    if branch_length < 10:
        return
    else:
        forward(branch_length)
        left(angle)
        branch_2(shrink_factor * branch_length, angle)
        right(angle * 2)
        branch_2(shrink_factor* branch_length, angle)
        left(angle)
        backward(branch_length)

def branch_3(branch_length, angle):
    shrink_factor = uniform(0.6, 0.9)
    angle = randint(15, 45)
    pensize(branch_length / 10)
    if branch_length < 10:
        return
    else:
        forward(branch_length)
        left(angle)
        branch_3(shrink_factor * branch_length, angle)
        right(angle * 2)
        branch_3(shrink_factor* branch_length, angle)
        left(angle)
        backward(branch_length)

def branch_4(branch_length, angle):
    shrink_factor = uniform(0.6, 0.9)
    angle = randint(15, 45)
    pensize(branch_length / 10)
    color("chocolate4")
    if branch_length < 10:
        color("chartreuse4")
        shape("circle")
        stamp()
        color("chocolate4")
    else:
        forward(branch_length)
        left(angle)
        branch_4(shrink_factor * branch_length, angle)
        right(angle * 2)
        branch_4(shrink_factor* branch_length, angle)
        left(angle)
        backward(branch_length)

# Set tree 0-4 (0 is the most basic, 4 is the most complex)
build_tree = 0

if build_tree == 1:
    branch_1(100, 30)
elif build_tree == 2:
    branch_2(100, 30)
elif build_tree == 3:
    branch_3(100, 30)
elif build_tree == 4:
    branch_4(100, 30)
else:
    branch(100, 30)
done()