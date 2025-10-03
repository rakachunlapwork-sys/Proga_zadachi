# конвертер римских чисел

def convert(choice, num):
    s = ""
    if choice==1:
        num = int(num)
        slow = {1: "I", 2: "II", 3: "III", 4: "IV", 5: 'V', 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: 'X', 50: 'L',
                100: 'C', 500: 'D', 1000: 'M'}
        raz = []
        k = 0
        while num != 0:
            last = num % 10
            raz.append(last * 10 ** k)
            k += 1
            num = num // 10
        sorted(raz, reverse=1)
        if len(raz) > 1:
            if raz[-1] == 4:
                raz2 = raz[:-1]
                for c in raz2:
                    try:
                        s += slow[c][::-1]
                    except:
                        s += slow[c // int(str(c)[0])] * int(str(c)[0])
                s += slow[4]
            elif raz[-1] == 9:
                raz2 = raz[:-1]
                for c in raz2:
                    try:
                        s += slow[c][::-1]
                    except:
                        s += slow[c // int(str(c)[0])] * int(str(c)[0])
            else:
                for c in raz:
                    try:
                        s += slow[c][::-1]
                    except:
                        s += slow[c // int(str(c)[0])] * int(str(c)[0])
            s = s[::-1]
        else:
            s += slow[raz[0]]
        s = s.replace("XXXXX", "L")
        print(s)
    else:
        s = num
        slow = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, "IX": 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = []
        for c in range(len(s)):
            while 'M' in s:
                a.append(1000)
                s = s.replace("M", "", 1)
            while 'D' in s:
                a.append(500)
                s = s.replace("D", "", 1)
            while 'C' in s:
                a.append(100)
                s = s.replace("C", "", 1)
            while 'L' in s:
                a.append(50)
                s = s.replace("L", "", 1)
            while 'X' in s:
                a.append(10)
                s = s.replace("X", "", 1)
            while 'IX' in s:
                a.append(9)
                s = s.replace("IX", "", 1)
            while 'VIII' in s:
                a.append(8)
                s = s.replace("VIII", "", 1)
            while 'VII' in s:
                a.append(7)
                s = s.replace("VII", "", 1)
            while 'VI' in s:
                a.append(6)
                s = s.replace("M", "", 1)
            while 'V' in s:
                a.append(5)
                s = s.replace("V", "", 1)
            while 'IV' in s:
                a.append(4)
                s = s.replace("IV", "", 1)
            while 'III' in s:
                a.append(3)
                s = s.replace("III", "", 1)
            while 'II' in s:
                a.append(2)
                s = s.replace("II", "", 1)
            while 'I' in s:
                a.append(1)
                s = s.replace("I", "", 1)
        print(sum(a))



val = "yes"

while val.lower()=="yes":
    print("Добро пожаловать в конвертер римских чисел!")
    choice = int(input("Если вы хотите конвертировать римское число, нажмите 1, если арабское, нажмите 2 : "))
    num = input("Введите ваше число : ")
    convert(choice, num)
    val = input("Если хотите продолжить работу, введите 'yes', иначе введите любой набор символов : ")
