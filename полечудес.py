import random
lives = 9
words = ['Азарт', 'Бухта', 'Вираж', 'Дупло', 'Веник', 'Мороз''Адрес', 'Алтын', 'Апчхи', 'Астра', 'Абрек', 'Актив', 'Амеба', 'Арена', 'Афера', 'Автол', 'Бакен', 'Барич', 'Башка', 'Берет', 'Битюг', 'Бокал', 'Брага', 'Бугор', 'Бурда', 'Бычок', 'Вдоль', 'Весло', 'Взвар', 'Вирши',
         'Влечь', 'Возка', 'Ворот', 'Вслед', 'Выбор', 'Вырез', 'Гамма', 'Гирло', 'Говор', 'Горец', 'Грива', 'Гуляш', 'Гвалт', 'Глина', 'Голод', 'Гость', 'Дрель', 'Дупло', 'Дюшес', 'Дебет', 'Десна', 'Добре', 'Донос', 'Дотла', 'Дроги', 'Духан', 'Ежели', 'Екать', 'Егерь', 'Едкий', 'Езжай']
secret_word = random.choice(words)
clue = ['?'] * len(secret_word)
symbol = '✈'
game = True

while game:
    print()
    print("".join(clue))
    print("Осталось жизней: ", symbol*lives)
    answer = input("Введите букву или всё слово целиком: ")

    if answer == secret_word:
        print("Вы победили! Вы угадали слово -", answer)
        game = False
    else:
        if len(answer) == 1 and answer in secret_word:
            print("Вы угадали букву!")
            for index in range(len(secret_word)):
                if answer == secret_word[index]:
                    clue[index] = answer
            if secret_word == "".join(clue):
                print("Вы победили! Вы угадали слово -", answer)
                game = False
        else:
            print("Вы теряете жизнь! ")
            lives -= 1
            if lives == 0:
                print("Вы проиграли((, к  сожалению!")
                game = False
