
import random


adjectives = ["hot", "happy", "red", "small", "big", "blue"]

nouns = ["hippo", "zebra", "bat", "lion", "snake", "hadgehog"]

symbols = "%№$&*@"


adjective = random.choice(adjectives)
noune = random.choice(nouns)
symbol = random.choice(symbols)
numeral = random.randrange(0, 100)

print("Вот ваш пароль: ", adjective, symbol, noune, numeral, sep="")
