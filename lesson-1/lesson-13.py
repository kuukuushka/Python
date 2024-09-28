# number = int(input("Введите кол-во секунд: "))
# for i in range(number, 0, -1):
#     print(i)
# print("Я иду искать!")



# total_soldier = int(input("Сколько солдат: "))
# push_ups = 0
# if total_soldier >= 4:
#     for soldier in range(total_soldier - 3, 0, -4):
#         regulation_sum = int(input("Сколько правил прописано в воинском уставе: "))
#         soldier_regulation = int(input("Сколько правил устава, солдат: "))
#         if regulation_sum != soldier_regulation:
#             print("Отжиманий", soldier * 10, "сделай")
#             push_ups += soldier * 10
#     print("Всего отжиманий:", push_ups)
# else:
#     print("Слишком мало солдат для опроса")



# n = int(input("Введите кол-во секунд: "))
# even_n = n - n % 2
# for i in range(even_n, 0, -2):
#     print(i)
# print("Я иду искать!")




# buckwheat_sum = 100
# month = 0
# for i in range(buckwheat_sum -4, -1, -4):
#     month += 1
#     print("Прошело", month, "месяцев")
#     print(i, "килогрмма осталось")
#     print()



# debtors = int(input("Введите количество должников: "))
# summ = 0
# for i in range(0, debtors, 5):
#     print("Должник с номером", i)
#     money = int(input("Сколько должны? "))
#     summ += money
# print("Общая сумма долга:", summ)



# total_timer = int(input("Время таймера: "))

# for reverse_timer in range(total_timer, 0, -1):
#     print("Осталось", reverse_timer)
#     end = int(input("Хотите забрать еду ? (1 - да, 0 - нет) "))
#     if end == 1: 
#         print("Ваша еда готова, можете забрать. Остановились на:", reverse_timer)
#         break
# if end != 1:
#     print("Ваша еда готова, осторожно горячо!")




# first = int(input("Введите первое число: "))
# last = int(input("Введите второе Число: "))
# multiples = int(input("Введите кратное число: "))
# summ_namber = 0
# summ_total = 0

# for i in range(first, last + 1):
#     if i % multiples == 0: 
#         print(i)
#         summ_namber += i 
#         summ_total += 1 
    
# if summ_total == 0:
#     print("Нет кртаных чисел")
# else:
#     print(summ_namber)
#     print(summ_total)
#     print("Среднеяя арифметическая", summ_namber / summ_total)




# first = int(input("Введите начало отрезка: "))
# last = int(input("Введите конец отрезка: "))
# step = int(input("Введите шаг: "))
# y = 0

# for x in range(last, first - 1, step):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print("В точке", x, "функция равна", y)





# educational_grant = int(input("Введите стипендию: "))
# expenses = int(input("Введите расходы на проживание: "))
# summ = 0
# summ_2 = 0
# for i in range(1, 11):
#     summ = expenses - educational_grant 
#     summ_2 += summ
#     print(i, "месяц траты", f"{expenses:.2f}", "не хватает", f"{summ_2:.2f}")
#     expenses = expenses * 0.03 + expenses

# print(f"Нужно попросить у родителей {summ_2:.2f} рублей.")

    


# N = int(input("Введите N: "))  # Запрашиваем ввод натурального числа N
# total_sum = 0  # Инициализируем переменную для хранения суммы

# # Используем цикл для вычисления элементов последовательности и их суммы
# for n in range(N):
#     element = (-1) ** n * (1 / 2) ** n  # Вычисляем текущий элемент
#     total_sum += element  # Добавляем элемент к общей сумме

# print(f"Ответ: {total_sum}")  # Выводим итоговую сумму





# Получаем ввод данных
X = int(input("Введите количество мальчиков: "))
Y = int(input("Введите количество девочек: "))

# Проверяем, если рассадить мальчиков и девочек невозможно
if X > Y + 1 or Y > X + 1:
    print("Нет решения")
else:
    result = []
    total = X + Y  # Общее количество мест
    for i in range(total):
        if X > Y:  # Если мальчиков больше, сажаем мальчика
            result.append('B')
            X -= 1
        elif Y > X:  # Если девочек больше, сажаем девочку
            result.append('G')
            Y -= 1
        else:  # Если мальчиков и девочек поровну, чередуем
            if i % 2 == 0:
                result.append('B')
                X -= 1
            else:
                result.append('G')
                Y -= 1
    # Выводим результат в виде строки
    print(''.join(result))





