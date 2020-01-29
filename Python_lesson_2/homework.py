#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# i = 0
# while i < 5:
#     i += 1
#     print('Строка', i)


'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# sum = 0
# for i in range(10):
#     number = int(input('Напишите цифру от 0 до 10: '))
#     if number == 5:
#         sum += 1
#         print('Количество 5 равно ', sum)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# sum = 1
# for i in range(1,11):
#     sum *= i
# print(sum)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# number = 547
# sum = 0
# while number > 0:
#     sum += number % 10
#     number = number // 10
# print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# number = 78521
# integer = 1
# while number > 0:
#     integer *= number % 10
#     number = number // 10
# print(integer)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
number = 456
integer = 0

while number > 0:
     if number % 10 >= integer:
         integer = number % 10
     number = number // 10
print(integer)

'''
Задача 10
Найти количество цифр 5 в числе
'''
number = int(input('Введите число: '))
integer = 0

while number > 0:
    if number % 10 == 5:
        integer += 1
    number = number // 10
print(integer)