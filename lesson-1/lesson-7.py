# time = float(input("Какое сейчас время ? "))

# if (time >= 8 and time < 10) or (time >= 12 and time < 14) or (time >= 15 and time < 18) or (time >= 20 and time < 22):
#     print("Можно получить посылку")
# else:
#     print("Посылку получить нельзя")



# number = int(input('Введите число: '))
# total = 0
# while number != 0:
#     total += number
#     number = int(input('Введите новое число: '))
# print(total)




# number = 0
# while number < 98:
#     number += 7
#     print(number)



# temperature = int(input("Какая сейчас температура? "))
# number = 0
# while temperature > 15:
#     number += 20
#     temperature -= 2
#     if temperature <= 15:
#         break
#     number += 10
# print(number)


# number = int(input("Введите число: "))
# summ = 0
# while number != 0:
#     last_number = number % 10
#     print(last_number)
#     if last_number == 5:
#         print("Обнаружен разрыв")
#         break
#     summ += last_number
#     number //= 10
# print("Сумма:", summ)
    
# number = 0
# summ_numbers = 0 
# while number >= 0:
#     number = int(input("ВВедите новое число: "))
#     summ_numbers += 1
# print("Количество введенных чисел", summ_numbers)


# number = 0 
# summ_numbers = 0 
# while True:
#     number = int(input("Введите число: "))
#     if number < 0:
#         print("Найдено отрицательное число")
#         print("Введено всего чисел:", summ_numbers)
#         break
#     summ_numbers += 1




# starting_amount = int(input("Введите стартовую сумму: "))
# while starting_amount < 10000:
#     cube = int(input("Сколько выпало на кубике? "))
#     if cube == 3:
#         starting_amount = 0
#         print("Вы проиграли всё!")
#         break
#     starting_amount += 500
#     print("Выиграли 500 рублей") 
# print("Итоговый остаток:", starting_amount)




# count = 10
# while count <= 10:
#     print(count)
#     if count == 0:
#         print('Время вышло!')
#         break
#     count -= 1




# while True:
#     play = int(input("Продолжаем работать? 1/0: "))
#     if play == 0:
#         print("Приложение закрывается…")
#         break
# print("Работа завершена")



is_working = 1
while is_working:
    is_working = int(input("Продолжаем работать? 1/0: "))

print("Работа завершена")



# while True: 
#     print("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!")
#     password = int(input("Введите код: "))
#     if password == 550:
#         print("Код верный, завершаю работу...") 
#         break







