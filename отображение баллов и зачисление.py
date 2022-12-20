from turtle import*
score_1 = 0
score_2 = 0 

penup()
goto(-300,300)
write("ответы первого игрока", font=("Arial", 14, "normal"))
goto(-300,200)
write("Ответы второго игрока", font=("Arial", 14, "normal"))


ans_1 = textinput("Задание 1", "сколько месяцев в году имеют 28 дней")
if ans_1 =="1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",  14, "normal"))
else:
    res = "x"
    goto(-300,280)
    write(res,font=("Arial", 14, "normal"))


ans_2 = textinput("задание 2", "Какое слово всегда пишеться неправельно?")
if ans_2 == "неправельно":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial", 14, "normal"))
else:
    res = "x"
    goto(-300,180)
    write(res,font=("Arial", 14, "normal"))


ans_1 = textinput("Задание 3", "сколько будет 2+2*2")
if ans_1 =="6":
    res = "+"
    score_1 += 1
    goto(-310,280)
    write(res,font=("Arial",  14, "normal"))
else:
    res = "x"
    goto(-310,280)
    write(res,font=("Arial", 14, "normal"))


ans_2 = textinput("задание 4", "какая река самая страшная?")
if ans_2 == "Тигр":
    res = "+"
    score_2 +=1
    goto(-310,180)
    write(res,font=("Arial", 14, "normal"))
else:
    res = "x"
    goto(-310,180)
    write(res,font=("Arial", 14, "normal"))


ans_1 = textinput("Задание 5", "Какой узел нельзя развязать ?")
if ans_1 =="железнодорожный":
    res = "+"
    score_1 += 1
    goto(-320,280)
    write(res,font=("Arial",  14, "normal"))
else:
    res = "x"
    goto(-320,280)
    write(res,font=("Arial", 14, "normal"))


ans_2 = textinput("задание 6", "Каких каиней нет в море?")
if ans_2 == "сухих":
    res = "+"
    score_2 +=1
    goto(-320,180)
    write(res,font=("Arial", 14, "normal"))
else:
    res = "x"
    goto(-320,180)
    write(res,font=("Arial", 14, "normal"))


if score_1 > score_2:
    goto(0,0)
    write("Выграл перый игрок", font=("Arial", 14, "normal"))
elif score_1 == score_2:
    goto(0,0)
    write("Ничья", font=("Arial", 14, "normal"))
else:
    goto(0,0)
    write("Выиграл второй игрок", font=("Arial", 14, "normal"))


exitonclick()

