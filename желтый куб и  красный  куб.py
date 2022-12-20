from turtle import*
from random import*
num = randint(1,10)
print(num)
col = input("Введите цвет: yellow или red ")
if num % 2 == 0:
    if col == "yellow":
        color(col)
        forward(80)
        left(90)
        forward(30)
        left(90)
        forward(80)
        left(90)
        forward(30)
        left(90)
    elif col == "red":
        color(col)
        forward(60)
        left(120)
        forward(60)
        left(120)
        forward(60)
exitonclick()