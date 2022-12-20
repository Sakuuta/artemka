from turtle import*
from random import*
num = randint(0,1000)
print(num)
col = input("Веди цвет red или green ")
if num > 9 and num < 100:
    if col == "red":
        color(col)
        width(3)
    elif col == "grenn":
        color(col)
        width(5)
    fd(100)
    penup()
    goto(0,-50)
    pendown()
    fd(100)
elif num > 99 and num < 1000:
    if col == "red":
        color(col)
        width(5)
    elif col == "green":
        color(col)
        width(3)
    fd(100)
    penup()
    goto(0,-50)
    pendown()
    fd(100)
    penup()
    goto(0,-100)
    pendown()
    fd(100)
else:
    penup()
    goto(-340,200)
    pendown()
    right(45)
    fd(600)
exitonclick()

