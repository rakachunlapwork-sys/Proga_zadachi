def analysys(string):
    words = string.split()
    words_True = [c for c in words if c not in ".,@:;!&?d"]
    top = {}
    ans = []
    symbols = set()
    space = 0
    gl = 0
    negl = 0
    for c in string:
        if c==" ":
            space+=1
        elif c in "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY":
            gl+=1
        else:
            negl+=1
        symbols.add(c)
        top[string.count(c)] = c
        ans.append(string.count(c))
    ans = set(ans)
    ans = sorted(list(ans), reverse=1)


    print(f"Количество гласных символов: {gl}")
    print()
    print(f"Количество негласных символов: {negl}")
    print()
    print(f"Количество пробелов: {space}")
    print()
    print(f"Количество слов: {len(words_True)}")
    print()
    if len(symbols)>2:
        print("Топ символов по количеству: ")
        print()
        print(f"1 место по популярности : {top[ans[0]]}, кол-во = {ans[0]}")
        print()
        print(f"2 место по популярности : {top[ans[1]]}, кол-во = {ans[1]}")
        print()
        print(f"3 место по популярности : {top[ans[2]]}, кол-во = {ans[2]}")
    else:
        print("Количство различных символов меньше 3, топ 3 не составлен!")

string = input("Вас приветствует анализатор текста, введите строку для анализа: ")
print()

analysys(string)