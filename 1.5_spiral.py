from turtle import *

def square(side_length, degree):
    for i in range(4):
        fd(side_length)
        rt(90)

side_length = int(input('side_length = '))
degree = int(input('degree = '))
number = int(input('number = '))

for i in range(number):
    side_length += 5
    square(side_length, degree)
    rt(degree)
