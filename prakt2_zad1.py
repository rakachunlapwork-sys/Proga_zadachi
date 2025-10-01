# Шифр Цезаря
def cesar_script(text, shift, alphabet):
    result = ''
    for symbol in text:
        index = alphabet.find(symbol)
        if "п" in alphabet:
            if abs(shift)<=32:
                next_index = index + shift
                next_symbol = alphabet[next_index]
                result+=next_symbol
            else:
                if shift<0:
                    next_index = index - (abs(shift)%len(alphabet))
                    next_symbol = alphabet[next_index]
                    result += next_symbol
                else:
                    next_index = index + (abs(shift) % len(alphabet))
                    next_symbol = alphabet[next_index]
                    result += next_symbol



        if "p" in alphabet:
            if abs(shift) <= 25:
                next_index = index + shift
                next_symbol = alphabet[next_index]
                result += next_symbol
            else:
                if shift < 0:
                    next_index = index - (abs(shift) % len(alphabet))
                    next_symbol = alphabet[next_index]
                    result += next_symbol
                else:
                    next_index = index + (abs(shift) % len(alphabet))
                    next_symbol = alphabet[next_index]
                    result += next_symbol

    return result



russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english = 'abcdefghijklmnopqrstuvwxyz'

text  = input('Введите пожалуйста вашу строку:\n').lower()
shift = int(input('Введите сдвиг:\n'))
choice = input('Вы хотите дешифровать или шифровать? (1 - ширфровать, 2 - дешифровать):\n').lower()


if text[0] in russian:
    alphabet = russian
elif text[0] in english:
    alphabet = english
else:
    print("Error unknown symbol!")


if choice == "1":
    result = cesar_script(text, shift, alphabet)
    print(result)
elif choice == '2':
    result = cesar_script(text, -shift, alphabet)
    print(result)
else:
    print('Вы что-то ввели не правильно')








