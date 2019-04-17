from turtle import *

def polycon(side_length = 100, sides = 3):
    for i in range(sides):
        fd(side_length)
        left(180-180*(sides-2)/sides)

sides = int(input("sides = "))
side_length = int(input("side_length = "))

polycon(side_length, sides)
