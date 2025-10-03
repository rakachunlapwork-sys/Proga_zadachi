# Генератор паролей
import random

def generator(lenght, low, high, num, dig):

    alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_small = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    digits = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    a = []
    proof = low+high+num+dig
    if proof==lenght:
        if low > 0:
            for i in range(low):
                a.append(random.choice(alphabet_small))
        if high > 0:
            for i in range(high):
                a.append(random.choice(alphabet_big))
        if num > 0:
            for i in range(num):
                a.append(random.choice(numbers))
        if dig > 0:
            for i in range(dig):
                a.append(random.choice(digits))
    else:
        print("Неверная длина пароля, уберите или добавьте несколько символов!")

    s = ""
    for c in a:
        s+=random.choice(a)
    print(s)

lenght = 1
low = 0
high = 0
numbers = 0
digits = 0

proof = low+high+numbers+digits

while proof!=lenght:
    print("Добро пожаловать в генератор паролей!")
    lenght = int(input("Введите желаемую длину пароля: "))
    low = int(input("Введите количество символов в нижнем регистре: "))
    high = int(input("Введите количество символов в верхнем регистре: "))
    numbers = int(input("Введите количество цифр: "))
    digits = int(input("Введите количество специальных символов: "))
    proof = low + high + numbers + digits

    generator(lenght, low, high, numbers, digits)
