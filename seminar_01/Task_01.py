# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def Weekday():
    num = input('введите число от 1 до 7\n')
    if num == 6 or num == 7:
        print('Yas')
    else:
        print('No')
Weekday()

