# 1- Задайте список из нескольких чисел. Напишите программу, которая
#  найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# def some_list():
#     some_list = [randint(1, 10)for _ in range(5)]
#     summa = 0

#     print(some_list)
#     for i in range(1, len(some_list), 2):
#         summa += some_list[i]

#     print(summa)

# some_list()

# 2-Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний
#  и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# from random import randint

# def some_list():
#     some_list = [randint(1, 10)for _ in range(6)]
#     new_list = []
#     print(some_list)

#     for i in range(0, (len(some_list) - 1) // 2 + 1):
#         new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])

#     print(new_list)

# some_list()


# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

# def some_list():
   
#   some_list = list(map(float, input("Введите числа через пробел:\n").split()))
#   diff = [round(i % 1,2) for i in some_list if i % 1 != 0]
#   print(max(diff) - min(diff))
# some_list()



# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# def dec_num (n, k = ''):
#   if n != 0:
#     k+= dec_num (n // 2, k) + str (n % 2)
#   return k
# n = int (input ('Введите десятичное число: '))
# k = dec_num(n)
# print(k)


# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
#  индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def fibonacci_list(k: int) -> list:
    fib_list = [-1, 1, 0, 1, 1]
    for i in range(3, k+1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        fib_list.insert(0, fib_list[1] - fib_list[0])
    return fib_list

k = 0
while k < 2:
    k = int(input('Введите число: '))
    fib_list = fibonacci_list(k)
print(fib_list)