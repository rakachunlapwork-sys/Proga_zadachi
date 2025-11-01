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
                print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
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
                print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
                print()
                time.sleep(2)
                k2+=1
            if knight.health<0:
                print("Вы погибли")
                sys.exit()
            elif dragon.health<0:
                print(f"Поздравляем {knight.name}, Вы победили Дракониуса!")

    elif choice_2 == "1":
        print(f'''Вас можно понять, {knight.name}, вы убили агрессивное животное, потому что побоялись за свою жизнь,
но не обернётся ли это катастрофой для вас?''')
        print()
        print('''Когда вы убили волка, он издал жалобный дотошный крик,
Вам стало не по себе, начался гром,
Вы стали слышать странные звуки приближения чего-то большого и побежали из лесу.
Перед вами поле, нэйм, путь к драконьей горе будет в несколько раз дольше через поле, но безопаснее.
Случайно вы натыкаетесь на бугорок...
О, что же это?''')
        time.sleep(2)
        open_stone = ["sword", "guitar", "eggs"]
        choice_stone = random.choice(open_stone)
        print(f"Поздравляем, {knight.name}, теперь у вас есть новый предмет {choice_stone}")
        print()
        print("Спустя неделю...")
        time.sleep(2)
        print()
        print("Вы взобрались на драконью гору, наконец-то!")
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
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
            print()
            time.sleep(2)
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
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
            print()
            time.sleep(2)
        if knight.health<0:
            print("Вы погибли")
            sys.exit()
        elif dragon.health<0:
            print(f"Поздравляем {knight.name}, Вы победили Дракониуса!")        
            print()
            time.sleep(2)
            print("Но что это так быстро движется на вас???")        
            print()
            time.sleep(2)
            print(f"Это дух убитого вами волка, {knight.name}")
            print()
            time.sleep(2)
            print("""Дракон умеют призывать души тех, кому вы навредили,
волк бросился на вас, вы попытались отбиться, но безуспешно""")
            print()
            time.sleep(2)
            print(f"""к сожалению, вы погибли, {knight.name}, волк и дракон взяли своё,
теперь вы навсегда скованы вместе в мире мёртвых...""")
            sys.exit()
else:
    time.sleep(4)
    print()
    print(f"""Вы послушались своего учителя, {knight.name}, и остались в городе, но вас нельзя назвать трусом,
Вы всё ещё хотите победить дракона, вы приняли мудрое решение под руководством мудрого человека.
Вам нужно много тренироваться !!!""")
    print()
    time.sleep(2)
    print("Спустя несколько лет...")
    print()
    time.sleep(2)
    print(f"""{knight.name}, вы только посмотрите на себя!!
Да вы просто Геракл, все женщины восхищаются вами, у вас много друзей, вам даже не нужно идти за драконом...""")
    print()
    time.sleep(2)
    print("В один прекрасный день вы идёте на очередную тренировку с друзьями...")
    print()
    time.sleep(2)
    print()
    print(f"""Когда вы остались наедине со своей подругой, она признаётся вам в любви и просит не идти за драконом,
потому что боится потерять вас...""")
    time.sleep(2)
    print()
    print(f"Вы отвечаете ей взаимностью, хотя всё равно намерены в будущем сразить дракона.")
    time.sleep(2)
    print()
    print(f"Прошло несколько лет, {knight.name}, у вас уже красавица жена и... пивоварня...")
    time.sleep(2)
    print()
    print(f"""Но в один день вы слышите рёв дракона, который проснулся,
Есть риск того, что он нападёт на город...""")
    time.sleep(2)
    print()
    print(f"""У вас есть несколько вариантов, {knight.name}:
Чтобы остаться в городе, нажмите 1
Чтобы Выйти за город и отвести дракона подальше, нажмите 2""")
    print()
    time.sleep(2)
    choice_2 = input("Выберите продолжение : ")
    print()
    while choice_2 not in ["1", "2"]:
        print("Введите 1 или 2 для продолжения!")
        print()
        choice_2 = input("Выберите продолжение : ")
        print()
    if choice_2=="1":
        time.sleep(2)
        print()
        print("Вы выбрали остаться в городе, потому что не хотите оставлять свою жену и дело всей жизни - пивоварение.")
        time.sleep(2)
        print()
        print("""в один день в город прилетает дракон...
    Он очень зол..""")
        time.sleep(2)
        print()
        print("Дракониус: давненько я не развлекался, пора повеселиться и отомстить вам, за то, что вы мешали мне спать своими шумными праздниками!")
        time.sleep(2)
        print()
        print(f"Ваша жена говорит вам: 'Драться не вариант, может задобрим его твоим пивом, {knight.name}?'")
        time.sleep(2)
        print()
        print(f"Дракон хорошо различает запахи и летит к вам!")
        time.sleep(2)
        print()
        print(f"Дракониус: Вот черти, даже когда их жизни под угрозой пытаются напиться!")
        print()
        for i in range(10):
            pivo = input("Нажмите 'enter', чтобы открыть бочку с пивом")
            print()
            while pivo!="":
                print("Введите 'enter' для продолжения!")
                print()
                pivo = input("Нажмите 'enter', чтобы открыть бочку с пивом")
                print()
        time.sleep(2)
        print()
        print(f"""Дракон подлетает к пивоварне, но вы берёте топор {knight.name}, и рубите самую большую бочку с пивом под давлением,
    оно летит прямо в лицо дракону!""")
        time.sleep(2)
        print()
        print(f"""Дракониус: вот чёрт, как же вкусно, мхымххмы
    Пжлуй отпщу ваас
    НУ что встал, человечина, давай втрую бочкууу""")
        time.sleep(2)
        print()
        print(f"""Теперь дракон самый главный заводила и пьяница в вашем городе,
    но вам же лучше, теперь он жарит своим огнём шашлыки, катает детишек у себя  на хребте и пляшет на праздниках...""")
        time.sleep(2)
        print()
        print(f"""Поздравляем, {knight.name}, это очень хороший вариант для вас всех!
    Никто не мог предположить, что всё так закончится...""")
        sys.exit()
    else:
        time.sleep(4)
        print()
        print(f"""Вы захотели отвести дракона подальше от города, {knight.name}, похвальное решение
Вы тренируетесь за городом уже несколько месяцев, все просят вас вернуться, особенно жена,
так как дракон успокоился и вроде как не собирается прилетать.
В один вечер вы решили сходить домой.""")
        time.sleep(2)
        print()
        print(f"""Жена: {knight.name}, ты наконец-то вернулся, где же ты пропадал?
Ты герой, тренируешься, чтобы мы жили спокойно!
Но я не хочу больше, чтобы ты уходил, я хочу, чтобы ты был со мной""")
        time.sleep(3)
        print()
        print(f"""ЧТО? Ты опять хочешь уйти, нет, пожалуйста, останься, он не прилетит..
Но у вас другое, предчувствие, {knight.name}, вы целуете жену, уходите, но обещаете вернуться.""")
        time.sleep(2)
        print()
        print(f"Вы выходите из дома, открываете сундук и вытаскиваете оттуда первую попавшуюся вещь...")
        time.sleep(2)
        open_stone = ["sword", "guitar", "eggs"]
        choice_stone = random.choice(open_stone)
        print(f"Поздравляем, {knight.name}, вы взяли с собой {choice_stone}!")
        print()
        time.sleep(2)
        print(f"Спустя несколько дней вы слышите рёв дракона где-то возле горы...")
        print()
        time.sleep(2)
        print(f"Дракониус: Кто ты воин? Ты всё равно не остановишь меня, я спалю этот город до тла!!!")
        dragon = kd.Dragon("Дракониус", random.randint(10, 15), 200, random.choice(["Файрбол", "Пинок"]))
        print("Битва с Дракониусом: ")
        print()
        print(f"Ваш ход, {knight.name}")
        print()
        hit2 = input("Нажмите 1, чтобы ударить : ")
        while hit2!="1":
            hit2 = input("Нажмите 1, чтобы ударить : ")
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
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
            print()
            time.sleep(2)
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
            print(f"Здоровье {knight.name} : {knight.health}, Здоровье Дракониуса : {dragon.health}")
            print()
            time.sleep(2)
        if knight.health<0:
            print("Вы погибли")
            sys.exit()
        elif dragon.health<0:
            print()
            time.sleep(2)
            print(f"Дракониус: НЕЕт, этого не может Быыыыть...")
            print()
            time.sleep(2)
            print(f"""вы уже рады, что свергли дракона, но он оборачивается и протыкает вас когтем в самое сердце
Дракониус: ты уйдёшь вместе со мной...""")
            print()
            time.sleep(2)
            print(f"""{knight.name}, вы герой, вы сразили дракона, у вас даже есть силы идти домой!!!
С вас бежит сильный ручей крови,
вы задыхаетесь, но хотите ещё раз увидеть жену,
В городе тихо, потому что все попрятались по домам.""")
            print()
            time.sleep(2)
            print(f"""Вы подходите к двери своего дома, вы вот вот потеряете сознание.
Вы открываете, дверь нэйм, и видете мужчину с голым торсом, который сидит на вашей кровати...
Ваша жена видит вас и начинает плакать!""")
            print()
            time.sleep(4)
            print(f"""Жена: Простиии, неееет, нэйм, простии меня, тебя не было так долго, я, яя не хотела этого, я никогда не прощу себя, неет, пожалуйста не умирай
Вы падаете на колени, {knight.name}, кашляете сгустками крови, плачете, и падаете замертво...""")
            print()
            time.sleep(5)
            print(f"""Вы открываете глаза, {knight.name}, где же вы???
Остров, пляж, Дракониус??
Дракониус: Как же мне жаль тебя парень, ты ведь правда герой, зачем мы вообще всё это делали...
Зачем бились? Ради чего?
Ну, раз уж мы теперь здесь, давай выпьем пива на этом чудесном острове...""")
            print()
            time.sleep(5)
            print(f"""Прошло много лет, жена живёт теперь с тем мужчиной, но всё ещё не может простить себя за измену,
Люди благословляют вас, некоего {knight.name},
который спас их от дракона, и именно в этот день, каждый год чувствуется запах пиво в воздухе и слышится откуда-то рык дракона,
а моряки, которые проплывают около деревни, поговаривают, что видят странные силуэты рыцаря и огромного чудища, которые сидят на одном из островов и пьют что-то...""")
            sys.exit()