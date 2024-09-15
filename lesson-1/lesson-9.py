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




#tusk_8

def guess_number():
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        mid = (low + high) // 2
        print(f"Компьютер: Твоё число равно, меньше или больше, чем {mid}?")
        response = int(input("Мальчик (1 - равно, 2 - больше, 3 - меньше): "))
        
        if response == 1:
            print(f"Компьютер: Я угадал! Твоё число - {mid}.")
            return mid
        elif response == 2:
            low = mid + 1
        elif response == 3:
            high = mid - 1
        else:
            print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")
        
        attempts += 1
        if attempts > 7:
            print("Не удалось угадать число за 7 попыток.")
            return None

# Запускаем игру
guess_number()




