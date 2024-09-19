# positive = 0
# for i in range(10):
#     number = int(input("Введите число: "))
#     if (number % 2 == 0) and (number > 0):
#         positive += 1
# print("Чётными и положительные:", positive)



# total_date = 0
# summ = 0
# for i in range(12):
#     total_date += 1
#     money = int(input("Введите свою зарплату за месяц: "))
#     summ += money
# summ /= 12
# print(summ)




# number = int(input("Введите число: "))
# summ = 1
# for i in range(2, number + 1):
#     summ *= i
# print(summ)




# total_estimation = int(input("Сколько сегодня оценок получили ? "))
# summ_5 = 0 
# summ_4 = 0 
# summ_3 = 0

# for i in range(total_estimation):
#     estimation = int(input("Введите оценку: "))
#     if estimation == 5:
#         summ_5 += 1 
#     elif estimation == 4:
#         summ_4 += 1
#     else: 
#         summ_3 += 1
# if summ_5 > summ_4:
#     print("Больше отличников")
# elif summ_4 > summ_3:
#     print("Больше хорошистов")
# else:
#     print("Больше троечников")




# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# summ = 0 
# total_summ = 0

# for i in range(a, b + 1):
#     if i % 3 == 0:
#         summ += i
#         print("Число", summ)
#         total_summ += 1 
#         print("Тотал", total_summ)
# if total_summ == 0:
#     print("Такого числа нету")
# else:
#     summ //= total_summ
#     print("Среднее арифметическое чисел, кратных 3:", summ)



# for i in range(10, 100):  # Перебираем все двузначные числа
#     # Разбиваем число на десятки и единицы
#     tens = i // 10  # Цифра десятков
#     ones = i % 10   # Цифра единиц
    
#     # Вычисляем утроенное произведение цифр
#     product = 3 * (tens * ones)
    
#     # Проверяем, равно ли число этому произведению
#     if i == product:
#         print(i)
            
    



n = int(input("Введите количество карточек: "))
full_sum = 0

for i in range(1, n + 1):
    full_sum += i


# Формула общей суммы
# full_sum = n * (n + 1) // 2

remaining_sum = 0

for _ in range(n - 1):
    remaining_sum += int(input("Введите номер оставшейся карточки: "))


missing_card = full_sum - remaining_sum
print("Номер пропавшей карточки:", missing_card)




