import Knight_and_Dragon as kd
import random
import time
import sys 

print('Добро пожаловать в игру "Dragon&Knight" !')
print()
game = input("Введите play, чтобы начать игру : ").lower()
print()
while game!="play":
    game = input("Введите play, чтобы начать игру : ").lower()
print()
print('''В давние времена было так принято, что любой рыцарь должен был совершить подвиг...
Если рыцарь не совершил подвиг, то он и не рыцарь никакой, так было принято в те времена.
Кто-то становился рыцарем, чтобы заполучить женское внимание,
Кто-то хотел богатства и признания...
Но вам не было суждено стать рыцарем для личных целей...
Вы родились в адских условиях:
Когда вы появились на свет, ваши родители сказали вам:
"Добро пожаловать в преисподнюю, сынок"''')
print()
knight = kd.Knight(input("Введите своё имя : "), random.randint(5, 8), 100, "hit")
print()
print(f'''Добро пожаловать в ДрагонХилл, {knight.name}
В место, где рыцарями становятся не по собственному желанию
В место, где убили ваших родителей...
Конечно, вы их не помните, нэйм
Вам лишь рассказывали о них, в том числе и их последнюю фразу, которую вы слышали при рождении...
Дракон испепелял город в ваш день рождения, с вами и родилось название ДрагонХилл
Теперь это просто деревня, вам всего 18, город ещё не отстроили.
Дракон больше не прилетал, но вы сами хотели отомстить за свой город, за свою семью...
Вы долго тренировались, {knight.name}, но вы ещё ребёнок
Однажды вы спросили у своего учителя:
Учитель, я готов сразить чудовище, благословите меня на смертный бой...
Учитель : Нет сын мой, не жертвуй собой по глупости, ты не готов, ты погибнешь''')
print()
print("Выбор продолжения: ")
print()
print("Нажмите 1, Чтобы ослушаться учителя и пойти искать дракона")
print("Нажмите 2, Чтобы Послушать учителя и остаться в городе")
print()
choice_1 = input("Выберите продолжение : ")
print()
while choice_1 not in ["1", "2"]:
    print("Введите 1 или 2 для продолжения!")
    print()
    choice_1 = input("Выберите продолжение : ")
    print()
if choice_1 == "1":
    print(f'''А вы смелый, {knight.name}, вы всё-таки решили ослушаться учителя...
Вы пошли на поиски дракона.
Вы взяли немного еды, лук своего отца, который достался вам в наследство и стрелы
Вы вышли из ДрагонХилла, перед вами густой волшебный лес
Поговаривают, что там пропадали люди и происходили странные вещи...''')
    print()
    print("Но у вас есть цель всей вашей жизни")
    print("Вам страшно, но вы пошли в лес...")
    print()
    print("Спустя несколько дней...")
    print(f"""{knight.name}, у вас почти не осталось еды, вы измотаны и напуганы, но вам нужно идти дальше
Полдень, вы спокойно идёте, и вдруг...
Вы слышите рычание...
На вас бежит волк, он агрессивен, потому что голодный, он ранен, но хочет есть, поэтому нападает на вас
{knight.name}, вы достаёте лук, волк уже готов прыгать...
Но вы резко понимаете, что у вас остался кусочек жаренного мяса,
Вас терзают сомнения, убить агрессивное животное, или дать ему надежду, покормив его,
может он станет вашим другом , кто знает???""")
    print()
    print("Выберите продолжение : ")
    print()
    print("Нажмите 1, чтобы убить волка")
    print("Нажмите 2, чтобы покормить волка")
    print()
    choice_2 = input("Выберите продолжение : ")
    while choice_2 not in ["1", "2"]:
        print()
        print("Введите 1 или 2 для продолжения!")
        print()
        choice_2 = input("Выберите продолжение : ")
        print()
    
    if choice_2 == "2":
        print()
        print(f'''Вы сделали доброе дело, {knight.name}
Вы бросили кусок мяса волку,
Он учуял запах и очень быстро накинулся на еду
Он очень жадно ел, вы хотели погладить его...
Сперва он побоялся, но потом принюхался и подошёл...''')
        woolf = kd.Woolf(input("Введите имя волка : "), random.randint(2, 5), 50, random.choice(["bite", "auf"]))
        print()
        print(f"Поздравляем, {knight.name}, теперь у вас есть друг {woolf.name}.")
        print()
        print("Но говорят, что мы в ответе за тех, кого приручили...")
        print()
        print(f'''Прошла ночь, волчок принёс мёртвого зайца, вы пожарили его и съели,
долго вы пробирались через лес,
но ничего особенного и странного в нём не увидели
И вот, вы уже видите драконью гору
Красные облака, чёрные молнии, запах пепла...
Вам страшно, вы хотите погладить волка, но он уже рычит позади...
Вы оборачиваетесь и видите страшное каменное, чудовище,
оно обросло растениями и грязью, на нём сидели летучие мыши, у которых глаза были цвета крови
Поздравляем, {knight.name}, вы встретили голема!''')
        gollem = kd.Gollem("Голлем", random.randint(8, 12), 125, random.choice(["hit", "jump"]))
        print()
        print("Голем:")
        print()
        print('''Кто ты странник, и что делаешь здесь с этой шавкой?
Я хозяин этого леса, зря ты сюда пришёл, отсюда ещё никто не выходил!!!
Я жду, когда придёт воин, который сможет освободить меня из этой каменной оболочки, но ты выглядишь щуплым!
А твоя шавка даже укусить меня не сможет!
Я стар, очень стар, я устал охранять этот лес...
Если ты победишь меня, я дарую тебе подарок,
Я знаю, куда ты направляешься, дракона без моих волшебных предметов тебе не победить...''')
        print()
        print("Битва с големом : ")
        print()
        print("Голем:")
        print()
        print("Нападай, ты всё равно не победишь!")
        print()
        print(f"Ваш ход, {knight.name}")
        print()
        hit = input("Нажмите 1, чтобы ударить : ")
        while hit!="1":
            hit = input("Нажмите 1, чтобы ударить : ")
        k = 0
        while knight.health>0 or gollem.health>0:
            knight.attack_power = random.randint(5, 8)
            if knight.health<0 or gollem.health<0:
                break
            print("Ваша атака : ")
            print()
            knight.attack_power = random.randint(5, 8)
            gollem.attack_power = random.randint(8, 12)
            gollem.choice = random.choice(["hit", "jump"])
            gollem.health-=knight.attack_power
            if knight.health<0 or gollem.health<0:
                break
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {gollem.health}")
            print()
            time.sleep(2)
            print("Атака волка: ")
            print()
            print("Подсказка ^на Голема волк может только рычит, но это даёт свои плоды^")
            print()
            if k%2==0:
                woolf.choice = "auf"
                print("Волчий рык!")
                gollem.attack_power = random.randint(6, 9)
                gollem.health-=2
            print()
            print("Атака голема: ")
            print()
            if gollem.choice=="hit":
                print("Обычный удар голема")
                print()
                knight.health-=gollem.attack_power
                if knight.health<0 or gollem.health<0:
                    break
            else:
                knight.health-=gollem.attack_power
                print("хаха, теперь твоя атака ослабла!")
                print()
                knight.attack_power = random.randint(2, 5)
                if knight.health<0 or gollem.health<0:
                    break
            
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {gollem.health}")
            print()
            time.sleep(2)
            print("Ваша атака : ")
            gollem.health-=knight.attack_power
            if knight.health<0 or gollem.health<0:
                break
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {gollem.health}")
            print()
            time.sleep(2)
            k+=1
        if knight.health<0:
            print("Вы погибли")
            sys.exit()
        elif gollem.health<0:
            print(f"Поздравляем {knight.name}, Вы победили Голема!")
            print()
            print("Голем: ")
            print()
            print("Тыыы...")
            time.sleep(2)
            print("Неужели это сделал ты")
            time.sleep(2)
            print("Ты силён, дитя человека!")
            time.sleep(2)
            print("Спасибо, что освободил меня, теперь я отправлюсь в другой мир!")
            time.sleep(2)
            print("Как и обещал, я дарую тебе подарок")
            print("Сломай этот валун, там ты найдёшь 1 из волшебных предметов")
            print("Тебе придётся придётся тяжко против Дракониуса, удачи...")
            time.sleep(2)
            print("После смерти Голема закат побагровел и вокруг каменных груд выросли розы и тюльпаны")
            open_stone = ["sword", "guitar", "eggs"]
            choice_stone = random.choice(open_stone)
            open = input("Введите open, чтобы сломать валун : ").lower()
            knight.health = 120
            while open!="open":
                open = input("Введите open, чтобы сломать валун : ").lower()
            print(f"Поздравляем, {knight.name}, теперь у вас есть новый предмет {choice_stone}")
            knight.choice = random.choice(open_stone)
            print()
            print("Голем повержен, но главный враг ещё впереди!")
            print()
            print("Спустя несколько дней скитаний вы всё таки взобрались на драконью гору, поздравляем!")
            print("Добро пожаловать в логово Дракониуса!")
            print()
            dragon = kd.Dragon("Дракониус", random.randint(10, 15), 200, random.choice(["Файрбол", "Пинок"]))
            print("Дракониус: ")
            print()
            print("Я знал, что кто-то придёт по мою душу, но никто уже отсюда не уйдёт!")
            print()
            print("Битва с Дракониусом: ")
            print()
            print(f"Ваш ход, {knight.name}")
            print()
            hit2 = input("Нажмите 1, чтобы ударить : ")
            while hit2!="1":
                hit2 = input("Нажмите 1, чтобы ударить : ")
            k2 = 0
            while knight.health>0 or dragon.health>0:
                knight.attack_power = random.randint(5, 8)
                if knight.health<0 or dragon.health<0:
                    break
                print("Ваша атака : ")
                print()
                knight.attack_power = random.randint(5, 8)
                dragon.attack_power = random.randint(10, 15)
                if knight.choice=="eggs":
                    print("Eggs!")
                    print()
                    dragon.health-=10
                    knight.health+=2
                    if knight.health<0 or dragon.health<0:
                        break
                elif knight.choice=="guitar":
                    print("Guitar!")
                    print()
                    dragon.health-=12
                    dragon.attack_power = random.randint(5, 8)
                    if knight.health<0 or dragon.health<0:
                        break
                else:
                    dragon.health-=15
                    print("Sword!")
                    print()
                    dragon.attack_power = random.randint(8, 10)
                    if knight.health<0 or dragon.health<0:
                        break
                if knight.health<0 or dragon.health<0:
                    break
                dragon.choice = random.choice(["Файрбол", "Пинок"])
                if knight.health<0 or dragon.health<0:
                    break
                print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {dragon.health}")
                print()
                time.sleep(2)
                print("Атака волка: ")
                print()
                print("Подсказка ^на Голема волк может только рычит, но это даёт свои плоды^")
                print()
                if k2%2==0:
                    woolf.choice = "auf"
                    print("Волчий рык!")
                    dragon.attack_power = random.randint(6, 9)
                    dragon.health-=2
                print()
                print("Атака Дракониуса: ")
                print()
                if dragon.choice=="Файрбол":
                    print("Fireball !")
                    print()
                    knight.health-=dragon.attack_power
                    if knight.health<0 or dragon.health<0:
                        break
                else:
                    knight.health-=dragon.attack_power
                    print("хаха, теперь твоя атака ослабла!")
                    print()
                    knight.attack_power = random.randint(2, 5)
                    if knight.health<0 or dragon.health<0:
                        break
                print("Ваша атака : ")
                dragon.health-=knight.attack_power
                print("Обычный удар!")
                print()
                print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {dragon.health}")
                print()
                time.sleep(2)
                
                print(f"Здоровье {knight.name} : {knight.health}, Здоровье Голема : {dragon.health}")
                print()
                time.sleep(2)
                k2+=1
            if knight.health<0:
                print("Вы погибли")
                sys.exit()
            elif dragon.health<0:
                print(f"Поздравляем {knight.name}, Вы победили Дракониуса!")