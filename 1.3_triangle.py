from turtle import *

def triangle(side_length = 100):
    for i in range(3):
        fd(side_length)
        left(120)

triangle()
triangle(40)
