from turtle import *

def star(side_length):
    for i in range(5):
        fd(side_length)
        rt(144)

side_length = int(input('side_length = '))
star(side_length)
