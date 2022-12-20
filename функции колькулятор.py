
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": pow
}


try:
    first = float(input('first number:'))
    operation = input('operations:')
    second = float(input('second number:'))
    result = operations[operation](first, second)
except ValueError:
    print("Incorrect input")
except KeyError:
    print("Usopparted operations")
except ZeroDivisionError:
    print("Divison by zero")
else:
    print('Result:', result)
