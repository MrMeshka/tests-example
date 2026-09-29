from minimize import minimize

if minimize("HELLO") != "hello":
    raise Exception("Функция работает неверно!")

if minimize("HeLlO") != "hello":
    raise Exception("Функция работает неверно!")

if minimize("HELLO WORLD") != "hello world":
    raise Exception("Функция работает неверно!")

if minimize("") != "":
    raise Exception("Функция работает неверно!")

print("Все тесты пройдены!")