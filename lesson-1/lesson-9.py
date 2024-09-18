# tusk_1

# number = int(input("Введите число: "))
# n = 0
# number_degree = 0
# while n < number:
#     number_degree += 1
#     n += 1
#     summ = number_degree ** 3
#     print(number_degree, "** 3 =", summ)
    

# tusk_2

# name = input("Имя должника: ")
# summ = int(input("Сколько должен: "))
# print(name + ", ваша задолженность составляет", summ, "рублей.")

# while True:
#     money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
#     if money >= summ:
#         print("Отлично,", name + "! Вы погасили долг. Спасибо!")
#         break
#     print("Маловато,", name + ". Давайте ещё раз.")



# tusk_3

# number = int(input("Введите число: "))
# if number == 0:
#     total_numbers = 1 
# else:
#     total_numbers = 0
#     while number > 0:
#         number //= 10
#         total_numbers += 1

# print(total_numbers)



# tusk_4

# positive = 0
# negative = 0 

# while True:
#     feedback = int(input("Введите число: "))
#     if feedback > 0: 
#         positive += 1
#     elif feedback < 0:
#         negative += 1
#     else:
#         break
# print("Кол-во положительных чисел:", positive)
# print("Кол-во отрицательных чисел:", negative)


#tusk_5

# print("Начался восьмичасовой рабочий день.")
# time = 0
# tusk = 0
# wife = False

# while time < 8:
#     tusk += int(input("Сколько задач решит Максим? "))
#     calls = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#     if calls == 1:
#         wife = True
#     time += 1
# print("Рабочий день закончился. Всего выполнено задач:", tusk)
# if wife == True:
#     print("Нужно зайти в магазин.")




#tusk_6

# contribution = int(input("Какой вклад: "))
# percent = int(input("Какой процент ? "))
# final_percentage = int(input("Сколько хотите ? "))
# time = 0

# while final_percentage > contribution:
#     percentage = contribution * percent // 100 
#     contribution += percentage
#     time += 1
# print("Количество лет:", time)
# print("Итоговая сумма:", contribution)




#tusk_7

# summ = 0
# while True:
#     number = int(input("Введите число: "))
#     summ += 1
#     if number == 7:
#         print("Вы угадали! Число попыток:", summ)
#         break
#     elif number < 7:
#         print("Число меньше, чем нужно. Попробуйте ещё раз!")
#     else:
#         print("Число больше, чем нужно. Попробуйте ещё раз!")




#tusk_8

def guess_number():
    low = 1
    high = 100
    attempts = 0

    print("Загадай число между 1 и 100, а я попробую его угадать.")

    while low <= high:
        # Находим среднее число
        mid = (low + high) // 2
        attempts += 1

        print(f"Твоё число равно, больше или меньше, чем {mid}?")
        print("1 — равно, 2 — больше, 3 — меньше")

        response = int(input())  # Получаем ответ от пользователя

        if response == 1:
            print(f"Угадал! Твоё число: {mid}. Число попыток: {attempts}")
            break
        elif response == 2:
            low = mid + 1  # Искомое число больше, сдвигаем нижнюю границу
        elif response == 3:
            high = mid - 1  # Искомое число меньше, сдвигаем верхнюю границу
        else:
            print("Неверный ввод, попробуй снова.")

    if low > high:
        print("Число не найдено, что-то пошло не так.")

# Запуск программы
guess_number()


