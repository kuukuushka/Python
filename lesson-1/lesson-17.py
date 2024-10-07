# for row in range(6):
#     for col in range(6):
#         print(row + 2 * col, end="\t")
#     print()


# n = int(input("Введите число: "))
# for row in range(1, n + 1):
#     for col in range(row):
#         print(row, end="\t")
#     print()


# for row in range(20):
#     for col in range(50):
#         if (row == 0 or row == 19) and (col > 0 and col < 49):
#             print("-", end="")
#         elif col == 0 or col == 49:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()



# # Запрашиваем у пользователя количество чисел
# count = int(input("Введите количество чисел: "))

# # Инициализируем счетчик простых чисел
# prime_count = 0

# # Цикл для ввода чисел
# for _ in range(count):
#     number = int(input("Введите число: "))
    
#     # Проверка, является ли число простым
#     if number > 1:  # Простые числа больше 1
#         is_prime = True
#         for i in range(2, int(number**0.5) + 1):  # Проверяем делимость
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_count += 1  # Увеличиваем счетчик, если число простое

# # Вывод результата
# print(f"Количество простых чисел в последовательности: {prime_count}.")



# n = int(input("Введите количество чисел: "))
# max_divided = 0 # Переменная для хранения числа с максимальной суммой цифр
# max_sum_divided = 0 # Переменная для хранения максимальной суммы цифр

# for i in range(n):
#     number = int(input("Введите число: "))
#     divided = 0 # Сброс суммы цифр для текущего числа
#     temp = number # Считаем сумму цифр числа
#     while temp > 0:
#         divided += temp % 10
#         temp //= 10
#     if divided > max_divided: # Проверяем, является ли текущая сумма цифр максимальной
#         max_divided = divided # Обновляем максимальную сумму цифр
#         max_sum_divided = number # Обновляем число с максимальной суммой цифр
        
# print("Число:", max_divided)
# print("Число с наибольшей суммой цифр:", max_sum_divided)




