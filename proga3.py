# Принимает строку от пользователя

text = input('Введите вашу строку: ').lower()
char_list = []
char_count = {}
for char in text:
    if char in char_count.keys():
        char_count[char] +=1
    else:
        char_count[char]=1
for char, count in char_count.items():
    char_list.append((char, count))
for i in range(len(char_list)):
    for j in range(i+1, len(char_list)):
        if char_list[i][1] < char_list[j][1]:
            char_list[i], char_list[j] = char_list[j], char_list[i]
if len(char_list)==1:
    print("1)", char_list[0])
elif len(char_list) == 2:
    print("1)", char_list[0])
    print("2)", char_list[1])
else:
    for i in range(3):
        char, count = char_list[i]
        print(f"{i+1}){char}:{count}")