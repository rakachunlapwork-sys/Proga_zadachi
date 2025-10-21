# Fridge simulator

def add(goods, name, count, date=None):
    if name not in goods:
        goods[name] = [{"amount" : count, 'expiration_date' : date}]
    else:
        name+="_batch_2"
        goods[name] = [{"amount" : count, 'expiration_date' : date}]
    return goods[name]

def amount(goods, product):
    if product in goods:
        return goods[product][0]["amount"]
    else:
        return "Продукт не найден!"
    
def main():
    goods = {}
    while True:
        print("Добро пожаловать в главное меню симулятора холодильника!")
        print("Чтобы посмотреть содержимое холодильника, введите 1")
        print("Чтобы добавить продукт в холодильник, введите 2")
        print("Чтобы количество продукта по его названию, введите 3")
        print("Чтобы выйти из холодильника, введите 4")
        while True:
            try:
                n = int(input("Введите команду: "))
                if n in [1, 2, 3, 4]:
                    break
            except:
                print("Введите число от 1 до 4 !")

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
                goods[name] = add(goods, name, count, date)
            else:
                goods[name] = add(goods, name, count)
            print(f"Добавлен новый продукт '{name}'")
        elif n==3:
            product = input("Введите название продукта : ")
            print(f" вот количество продукта {product} : {amount(goods, product)}")
        elif n==4:
            break

main()
