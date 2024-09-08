# num_1 = int(input("Введите первое значение: "))
# num_2 = int(input("Введите второе значение: "))
# num_3 = int(input("Введите третье значение: "))

# if (num_1 > num_3) and (num_1 > num_2): 
#     max = num_1
#     print("Первый", max)
# elif num_2 > num_3:
#     max = num_2
#     print("Второй", max)
# else: 
#     max = num_3
#     print("Третий", max)

# print(max)



# x = int(input("Введите икс:"))
# y = int(input("Введите игрек:"))

# if x > y:
#     print("x больше y")
# elif x < y: 
#     print("x меньше y")
# else:
#     print("x равне y")



# bank = int(input("Сколько денег на счету? "))

# if bank >= 75000:
#     bank -= 75000
#     if bank < 5000:
#         bank += 1000
#         print("Сделана скидка")
#     print("Остаток на счету:", bank)
# else:
#     print("Не хватает денег на счету")
# print("Хорошего дня!")



total_money = int(input("Всего денег: "))
cheese = 60  
ice_cream = 20

if total_money >= cheese:
    total_money -= cheese
    print("На сыр денег хватило")
    if total_money >= ice_cream:
        print("И на мороженое тоже!")
    else: 
        print("Денег маловато")
else:
    print("Денег не хватило даже на сыр!")












