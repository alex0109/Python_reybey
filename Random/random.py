import random

con = True

while con == True:
    x = random.randint(1, 10)

    if x > 10 or x < 1:
        print("Введите число в нужном промежутке!")
    else:
        print("Сравниваем с этим числом...")

    y = random.randint(1, 10)
    print(y)

    if x > y:
        print("Ваше число больше, вот их разница: ", x-y)
    elif x < y:
        print("Ваше число меньше, вот их разница: ", y-x)
    else:
        print("Ваши числа одинаковы! Вот их разница: ", x-y)
