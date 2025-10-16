# Fridge simulator

def add(name, count, date=None):
    items = {}
    if name not in items:
        items[name] = [{"amount" : count, 'expiration_date' : date}]
    else:
        name+="_batch_2"
        items[name] = [{"amount" : count, 'expiration_date' : date}]
    return items[name]

def main():
    goods = {}
    while True:
        print("Добро пожаловать в главное меню симулятора холодильника!")
        print("Чтобы посмотреть содержимое холодильника, введите 1")
        print("Чтобы добавить продукт в холодильник, введите 2")
        print("Чтобы выйти из холодильника, введите 3")
        while True:
            try:
                n = int(input("Введите команду: "))
                if n in [1, 2, 3]:
                    break
            except:
                print("Введите число от 1 до 3 !")

        if n==1:
            print(goods)
        elif n==2:
            name = input("Введите название продукта : ")
            while True:
                try:
                    count = float(input("Введите количество продукта : "))
                    if isinstance(count, float):
                        break
                except:
                    print("Введите число !")

            print("Теперь введите срок годности продукта, Если ничего не указано, введите 0 : ")

            while True:
                try:
                    year = int(input("Введите год производства : "))
                    if isinstance(year, int):
                        break
                except:
                    print("Введите число !")

            while True:
                try:
                    month = int(input("Введите месяц производства : "))
                    if isinstance(month, int):
                        break
                except:
                    print("Введите число !")

            while True:
                try:
                    day = int(input("Введите день производства : "))
                    if isinstance(day, int):
                        break
                except:
                    print("Введите число !")
            
            if year!=0 and day!=0 and month!=0:
                date = str(day)+"-"+str(month)+"-"+str(year)
                goods[name] = add(name, count, date)
            else:
                goods[name] = add(name, count)
            print(f"Добавлен новый продукт '{name}'")
        elif n==3:
            break

main()
