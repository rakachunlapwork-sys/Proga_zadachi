number = int(input('Введите ваше число: '))
if number % 2 ==0:
    print('Число четное')
else:
    print('Число нечетное')
if number > 10 and number < 50:
    print('Число принадлежит диапазону')
else:
    print('Не принадлежит диапазону')
if number>0:
    print("число больше нуля")
elif number<0:
    print("число меньше нуля")
elif number==0:
    print("число равно нуля")
else:
    print("некорректное число")
