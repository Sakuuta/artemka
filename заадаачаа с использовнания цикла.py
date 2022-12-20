def cout(name):
    print(name, "сколко конфет")
    a = int(input())
    b = int(input())
    print("всего канфет:", a + b)


name = ["Коля", "Серёжа", "Катя"]


for i in range(len(name)):
    summa = cout(name[i])
