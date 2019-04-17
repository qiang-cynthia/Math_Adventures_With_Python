from turtle import *

def star(side_length):
    for i in range(5):
        fd(side_length)
        rt(144)

side_length = int(input('side_length = '))
degree = int(input('degree = '))
number = int(input('number = '))

for i in range(number):
    side_length += 5
    star(side_length)
    rt(degree)
