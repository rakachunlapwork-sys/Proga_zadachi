#Rock paper scissors

import random

again = "yes"

while again == "yes":
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага' !")
    choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
    comp_count = 0
    your_count = 0
    var = ["камень", "ножницы", "бумага"]
    comp_var = random.choice(var)
    while comp_count!=3 and your_count!=3:
        if comp_var == choice:
            print("Ничья!")
            choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ")
            comp_var = random.choice(var)
        if comp_var=="камень" and choice=="ножницы":
            your_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                comp_count+=1
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)
            
        if choice=="камень" and comp_var=="ножницы":
            your_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)
            
        if choice=="камень" and comp_var=="бумага":
            comp_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)
            
        if comp_var=="камень" and choice=="бумага":
            your_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)

        if choice=="ножницы" and comp_var=="бумага":
            your_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)
            
        if comp_var=="ножницы" and choice=="бумага":
            comp_count+=1
            if comp_count==3:
                print(f"Вы проиграли со счётом {comp_count} - comp : {your_count} - you ")
            elif your_count==3:
                print(f"Вы победили со счётом {your_count} - you : {comp_count} - comp ")
            else:
                print(f"Счёт : вы = {your_count}, comp = {comp_count}")
                choice = input("Выберите 1 из вариантов (Камень, Ножницы, Бумага) : ").lower()
                comp_var = random.choice(var)
    print()        
    again = input("Если хотите играть ещё раз, введите 'yes', иначе любые другие символы : ").lower()
