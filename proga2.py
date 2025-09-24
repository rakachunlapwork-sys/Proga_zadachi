import random # работа со случайными числами
import string # за работу со строками
spec_symbols = '!@#$%^&*('

letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

#  3 случайные цифры
numbers = ''.join(random.choice(string.digits) for _ in range(3))

#  2 специальных символа

symbols = ''.join(random.choice(spec_symbols) for _ in range(3))

word = letters+numbers+symbols
a = []
for c in word:
    a.append(c)
password = ""
for c in a:
    password+=random.choice(a)
print(password)