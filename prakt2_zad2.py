#Задача про олимпиаду
import random

values = set([random.randint(0, 100) for _ in range(int(input("Введите количество участников: ")))])
student = int(input("Баллы ученика: "))

def check_winners(scores, student_score):
    winners = sorted(list(scores)[-1:-4])
    if student_score in winners:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")
check_winners(values, student)

