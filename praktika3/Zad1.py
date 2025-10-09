import random

def chot(num):
    if num%2==0:
        return "Загаданное число чётное"
    else:
        return "Загаданное число нечётное"

again = "yes"

while again=="yes":
    print('Добро подаловать в игру "Угадайка чисел"!')
    diap1 = int(input("Введите первое число диапазона: "))
    diap2 = int(input("Введите второе число диапазона: "))
    num = random.randint(diap1, diap2+1)
    k = 3
    choice = int(input("Введите ваше число: "))
    while choice!=num and k!=0:
        if choice>num:
            if k==2:
                k-=1
                print("Загаданное число меньше введённого!")
                print(f"Подсказка: {chot(num)}")
                print(f"Оставшееся кол-во попыток = {k}")
                choice = int(input("Введите ваше число: "))
            elif k==1:
                k-=1
                print("Вы не отгадали число!")
                print(f"Загаданное число {num}")
                again = input("Чтобы играть снова, введите 'yes', иначе другую последовмтельность символов: ").lower()

            else:
                k-=1
                print("Загаданное число меньше введённого!")
                print(f"Оставшееся кол-во попыток = {k}")
                choice = int(input("Введите ваше число: "))
        elif choice<num:
            if k==2:
                k-=1
                print("Загаданное число больше введённого!")
                print(f"Подсказка: {chot(num)}")
                print(f"Оставшееся кол-во попыток = {k}")
                choice = int(input("Введите ваше число: "))
            elif k==1:
                k-=1
                print("Вы не отгадали число!")
                print(f"Загаданное число {num}")
                again = input("Чтобы играть снова, введите 'yes', иначе другую последовмтельность символов: ").lower()

            else:
                k-=1
                print("Загаданное число больше введённого!")
                print(f"Оставшееся кол-во попыток = {k}")
                choice = int(input("Введите ваше число: "))
        else:
            print(f"Вы отгадали, загаданное число = {num}")
            again = input("Чтобы играть снова, введите 'yes', иначе другую последовмтельность символов: ").lower()
