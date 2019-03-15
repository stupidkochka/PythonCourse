from random import randint
b = randint(0, 100)
a = 1488
while a != b:
    a = input('Введите число ')
    if int(a) > b:
        print('Текущее число больше заданного')
    elif int(a) < b:
        print('Текущее число меньше заданного')
    else: 
        print('Вы угадали число {}'.format(a))
        break