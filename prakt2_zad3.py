#задача про кондитерскую

def print_pack_report(value):
    for i in range(value, 0, -1):
        if i%15==0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i%5==0 and i%3!=0:
            print(f"{i} - расфасуем по 5")
        elif i%3==0 and i%5!=0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")

count = 0
while count<1:

    count = int(input("Введите количество товара от единицы!: "))

print_pack_report(count)